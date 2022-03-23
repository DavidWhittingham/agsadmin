from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

import abc
import copy


class ParamsBase(object):
    """
    Abstract base class for all function paramater objects for Sharing REST API.
    """

    __metaclass__ = abc.ABCMeta

    _props = None

    def __init__(self):
        self._props = {}
    
    def _get_params(self):
        return copy.deepcopy(self._props)

    def _set_params(self, params):
        self._props = copy.deepcopy(params)
