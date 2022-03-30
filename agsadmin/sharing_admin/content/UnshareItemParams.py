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


class UnshareItemParams(ParamsBase):
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