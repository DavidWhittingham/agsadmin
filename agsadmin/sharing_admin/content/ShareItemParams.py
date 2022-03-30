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
from ..._utils import truthy
from .._ParamsBase import ParamsBase


class ShareItemParams(ParamsBase):
    """Holds parameter values for the "share" content item request."""
    @property
    def groups(self):
        value = self._props.get("groups")

        if not value:
            return []

        return value.split(",")

    @groups.setter
    def groups(self, value):
        if isinstance(value, Sequence) and not isinstance(value, basestring):
            # got some kind of list, process to JSON-native format
            value = ",".join(value)

        if value is None:
            self._props.pop("groups", None)
        else:
            self._props["groups"] = value

    @property
    def confirm_item_control(self):
        return self._props.get("confirmItemControl")

    @confirm_item_control.setter
    def confirm_item_control(self, value):
        if value is None:
            self._props.pop("confirmItemControl", None)
        else:
            value = truthy(value)
            self._props["confirmItemControl"] = value
