from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)


class ClearEmptyFieldsMixin(object):
    """Params mixin for 'clearEmptyFields'."""
    @property
    def clear_empty_fields(self):
        """Gets or sets the clear empty status value for the request."""

        return self._props.get("clearEmptyFields")

    @clear_empty_fields.setter
    def clear_empty_fields(self, value):
        self._set_nullable_bool("clearEmptyFields", value)