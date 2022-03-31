from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

# third-party lib imports
from past.builtins import basestring

# local imports
from ..._utils import truthy
from .._ParamsBase import ParamsBase
from .ContentStatusType import ContentStatusType


class SetContentStatusParams(ParamsBase):
    """Holds parameter values for the "setContentStatus" content item request."""
    def __init__(self):
        super().__init__()

        # set default values, ensuring minimum structure exists for JSON
        self.status = None

    @property
    def clear_empty_fields(self):
        """Gets or sets the clear empty status value for the request."""

        return self._props.get("confirmItemControl")

    @clear_empty_fields.setter
    def clear_empty_fields(self, value):
        if value is None:
            self._props.pop("confirmItemControl", None)
        else:
            value = truthy(value)
            self._props["confirmItemControl"] = value

    @property
    def status(self):
        """Gets or sets the content status value for the request."""

        value = self._props.get("status")

        if not value:
            return None

        return ContentStatusType(value)

    @status.setter
    def status(self, value):

        if isinstance(value, basestring) and len(value.strip()) == 0:
            value = None

        self._props["status"] = "" if value is None else ContentStatusType(value).value
