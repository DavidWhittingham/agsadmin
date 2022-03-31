from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

# local imports
from ..._params_mixins.PagingParamsMixin import PagingParamsMixin
from ..._ParamsBase import ParamsBase


class ListItemsParams(PagingParamsMixin, ParamsBase):
    """Holds parameter values for the "share" content user item request."""
    pass
