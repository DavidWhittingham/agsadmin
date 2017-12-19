from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

import sys
import agsadmin

import pytest

from json import loads

@pytest.mark.parametrize(("data", "rsa_key", "modulus"), [
    ({"key1": "value1", "key2": "value2", "key3": "value3"}, 
     long("06DE8", 16),
     long("AD24236B572696888F2BF0D4C0FA64574104F5D3AF20A7A422D02551699734B6FC79ABD9E8C319AA7915752AB48313B021DDB3A0CDB5974C8549885F971A9F09A", 16)),
    ({"key1": "value1", "key2": "value2", "key3": "value3"}, 
     long("06DE8", 16),
     long("AD24236B572696888F2BF0D4C0FA64574104F5D3AF20A7A422D02551699734B6FC79ABD9E8C319AA7915752AB48313B021DDB3A0CDB5974C8549885F971A9F09A", 16))
])
def test_encrypt_request_data_rsa(data, rsa_key, modulus):
    """
    Tests that a dictionary that is submitted for encryption returns with the correct fields, and that the values 
    'look' encrypted (i.e. are modified).  It doesn't test the encryption algorithm itself.
    """

    encrypted_data = agsadmin._utils.encrypt_request_data(data, rsa_key, modulus)

    assert len(set(data.keys()) - set(encrypted_data.keys())) == 0

    for key, value in data.iteritems():
        assert value != encrypted_data[key]

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