from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

# standard lib imports
from enum import Enum

# local imports
from ..._utils import truthy
from .._ParamsBase import ParamsBase


class ClearEmptyFieldsMixin(object):
    """Params mixin for 'clearEmptyFields'."""
    @property
    def clear_empty_fields(self):
        """Gets or sets the clear empty status value for the request."""

        value = self._props.get("clearEmptyFields")

        if not value:
            return None

        return value

    @clear_empty_fields.setter
    def clear_empty_fields(self, value):
        if value is None:
            self._props.pop("clearEmptyFields", None)
        else:
            value = truthy(value)
            self._props["clearEmptyFields"] = value