from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

# third-party lib imports
from past.builtins import basestring

# local imports
from .._ParamsBase import ParamsBase
from .._params_mixins.ClearEmptyFieldsMixin import ClearEmptyFieldsMixin
from .ContentStatusType import ContentStatusType


class SetContentStatusParams(ClearEmptyFieldsMixin, ParamsBase):
    """Holds parameter values for the "setContentStatus" content item request."""
    def __init__(self):
        super().__init__()

        # set default values, ensuring minimum structure exists for JSON
        self.status = None

    @property
    def status(self):
        """Gets or sets the content status value for the request."""

        value = self._props.get("status")

        if not value:
            return None

        return ContentStatusType(value)

    @status.setter
    def status(self, value):
        """Sets status.  JSON structure exists explictly with blank value."""

        if isinstance(value, basestring) and len(value.strip()) == 0:
            value = None

        self._props["status"] = "" if value is None else ContentStatusType(value).value
