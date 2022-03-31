from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from future.utils import iteritems

import abc
import copy


class ParamsBase(object):
    """
    Abstract base class for all function paramater objects for Sharing REST API.
    """

    __metaclass__ = abc.ABCMeta

    _props = None

    def __init__(self, **kwargs):
        self._props = {}

        # get obj properties
        self_type = type(self)
        obj_properties = [p for p in dir(self_type) if isinstance(getattr(self_type, p), property)]

        # assign kwargs to properties, if they exist
        for (key, value) in iteritems(kwargs):
            if key in obj_properties:
                setattr(self, key, value)

    def _get_params(self):
        return copy.deepcopy(self._props)

    def _set_params(self, params):
        self._props = copy.deepcopy(params)
