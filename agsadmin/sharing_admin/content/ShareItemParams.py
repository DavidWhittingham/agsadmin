from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

# standard lib imports
try:
    from collections.abc import Sequence
except ImportError:
    # try older import location
    from collections import Sequence

# third-party lib imports
from past.builtins import basestring

# local imports
from .._ParamsBase import ParamsBase


class ShareItemParams(ParamsBase):
    """Holds parameter values for the "share" content item request."""
    @property
    def groups(self):
        return self._get_nullable_csv_list("groups")

    @groups.setter
    def groups(self, value):
        self._set_nullable_csv_list("groups", value, lambda v: v.strip())

    @property
    def confirm_item_control(self):
        return self._props.get("confirmItemControl")

    @confirm_item_control.setter
    def confirm_item_control(self, value):
        self._set_nullable_bool("confirmItemControl", value)
