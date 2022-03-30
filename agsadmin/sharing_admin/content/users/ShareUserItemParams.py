from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

# local imports
from ...._utils import truthy
from ..ShareItemParams import ShareItemParams


class ShareUserItemParams(ShareItemParams):
    """Holds parameter values for the "share" content user item request."""
    @property
    def everyone(self):
        return self._props.get("everyone")

    @everyone.setter
    def everyone(self, value):
        if value is None:
            self._props.pop("everyone", None)
        else:
            value = truthy(value)
            self._props["everyone"] = value

    @property
    def org(self):
        return self._props.get("org")

    @org.setter
    def org(self, value):
        if value is None:
            self._props.pop("org", None)
        else:
            value = truthy(value)
            self._props["org"] = value
