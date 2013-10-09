import sys
import agsadmin

import pytest

from json import loads

@pytest.mark.parametrize(("data", "rsa_key", "modulus", "use_pycrypto"), [
    ({"key1": "value1", "key2": "value2", "key3": "value3"}, 
     long("06DE8", 16),
     long("AD24236B572696888F2BF0D4C0FA64574104F5D3AF20A7A422D02551699734B6FC79ABD9E8C319AA7915752AB48313B021DDB3A0CDB5974C8549885F971A9F09A", 16),
     True),
    ({"key1": "value1", "key2": "value2", "key3": "value3"}, 
     long("06DE8", 16),
     long("AD24236B572696888F2BF0D4C0FA64574104F5D3AF20A7A422D02551699734B6FC79ABD9E8C319AA7915752AB48313B021DDB3A0CDB5974C8549885F971A9F09A", 16),
     False)
])
def test_encrypt_request_data_rsa(data, rsa_key, modulus, use_pycrypto):
    """
    Tests that a dictionary that is submitted for encryption returns with the correct fields, and that the values 
    'look' encrypted (i.e. are modified).  It doesn't test the encryption algorithm itself.

    :param use_pycrypto: If set to true, blocks Python-RSA from importing, forcing the fallback to PyCrypto
    :type use_pycrypto: bool
    """

    if use_pycrypto == True:
        sys.modules["rsa"] = None

    encrypted_data = agsadmin._utils.encrypt_request_data(data, rsa_key, modulus)

    if use_pycrypto == True:
        del sys.modules["rsa"]

    assert len(set(data.keys()) - set(encrypted_data.keys())) == 0

    for key, value in data.iteritems():
        assert value != encrypted_data[key]


@pytest.mark.parametrize(("base_url", "service_name", "service_type", "operation", "folder_name", "method", "exceptected_url"), [
    ("http://arcgisserver:6080/arcgis/admin", "fake_service", "MapServer", None, None, None, 
     "http://arcgisserver:6080/arcgis/admin/services/fake_service.MapServer/"),
    ("http://arcgisserver:6080/arcgis/admin", "fake_service", "MapServer", "Start", None, None, 
     "http://arcgisserver:6080/arcgis/admin/services/fake_service.MapServer/Start"),
    ("http://arcgisserver:6080/arcgis/admin", "fake_service", "MapServer", "Start", "FakeFolder", None, 
     "http://arcgisserver:6080/arcgis/admin/services/FakeFolder/fake_service.MapServer/Start"),
    ("http://arcgisserver:6080/arcgis/admin", "fake_service", "MapServer", "Start", "FakeFolder", "GET", 
     "http://arcgisserver:6080/arcgis/admin/services/FakeFolder/fake_service.MapServer/Start")
])
def test_create_operation_request(base_url, service_name, service_type, operation, folder_name, method, exceptected_url):
    """
    Tests the create operation request function, primarily to ensure that URL's are formed correctly based on input 
    parameters.
    """

    opr = agsadmin._utils.create_operation_request(base_url, service_name, service_type, operation, folder_name, method)
    if method == None:
        method == "POST"

    assert opr.url == exceptected_url
    assert opr.method == method

def test_decode_ags_operation():
    """
    Tests to ensure that ArcGIS Server JSON that indicates faults is correctly decoded, and raises the appropriate 
    error.
    """
    class FakeResponse(object):
        status_code = None,
        reason = None
        _json = None

        def __init__(self, json):
            self._json = json
            self.status_code = 200

        def json(self):
            return loads(self._json)

    ags_err_response = agsadmin._utils.decode_ags_operation(
        FakeResponse('{"code": 502,"messages": ["Error #1","Error #2","Error #3"]}'))
    assert ags_err_response.status_code == 502
    assert ags_err_response.reason == "Error #1 | Error #2 | Error #3"

    bad_json_response = agsadmin._utils.decode_ags_operation(FakeResponse('Very {Wrong}'))
    assert bad_json_response.status_code == 500
    assert bad_json_response.reason == agsadmin._utils.JSON_DECODE_ERROR

    ags_success_response = agsadmin._utils.decode_ags_operation(
        FakeResponse('{"success": true}'))
    assert ags_success_response.status_code == 200