import pytest

import agsadmin.exceptions

@pytest.mark.parametrize(("ex", "expected_output", "construction_message"), [
    (agsadmin.exceptions.InvalidServiceTypeError, agsadmin.exceptions.InvalidServiceTypeError.DEFAULT_ERROR_MESSAGE, None),
    (agsadmin.exceptions.InvalidServiceTypeError, "New Error Message", "New Error Message"),
    (agsadmin.exceptions.UnknownServiceError, agsadmin.exceptions.UnknownServiceError.DEFAULT_ERROR_MESSAGE, None),
    (agsadmin.exceptions.UnknownServiceError, "New Error Message", "New Error Message")
])
def test_exception_message(ex, expected_output, construction_message):
    instantiated_exception = ex() if construction_message == None else ex(construction_message)
    assert instantiated_exception.message == expected_output