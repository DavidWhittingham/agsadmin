from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ._ParamsBase import ParamsBase

class SearchParams(ParamsBase):

    @property
    def query(self):
        """Gets or sets the query string used to search."""
        return self._props.get("q")

    @query.setter
    def query(self, value):
        self._props["q"] = str(value)

