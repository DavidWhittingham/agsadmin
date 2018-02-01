import agsadmin

import pytest

@pytest.mark.parametrize(("hostname", "instance", "port", "use_ssl", "expected_url"), [
    ("agsserver", "agstest", None, False, "http://agsserver:6080/agstest/admin"),
    ("agsserver", "agstest", None, True, "https://agsserver:6080/agstest/admin"),
    ("agsserver", "agstest", 1234, False, "http://agsserver:1234/agstest/admin"),
    ("agsserver", "agstest", 1234, True, "https://agsserver:1234/agstest/admin")
])
def test_rest_admin(hostname, instance, port, use_ssl, expected_url):
    if port == None:
        ra = agsadmin.RestAdmin(hostname, "blah", "blah", instance_name = instance, use_ssl = use_ssl)
    else:
        ra = agsadmin.RestAdmin(hostname, "blah", "blah", instance_name = instance, port = port, use_ssl = use_ssl)

    assert ra.url == expected_url