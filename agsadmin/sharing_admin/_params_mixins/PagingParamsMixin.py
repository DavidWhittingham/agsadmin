from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)


class PagingParamsMixin(object):
    """Params mixin for paging parameters."""
    @property
    def num(self):
        return self._props.get("num")

    @num.setter
    def num(self, value):
        if value is None:
            self._props.pop("num", None)
        else:
            self._props["num"] = value

    @property
    def start(self):
        return self._props.get("start")

    @start.setter
    def start(self, value):
        if value is None:
            self._props.pop("start", None)
        else:
            self._props["start"] = value
