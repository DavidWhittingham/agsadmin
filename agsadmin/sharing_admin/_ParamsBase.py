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
from future.utils import iteritems
from past.builtins import basestring

import abc
import copy

# local imports
from .._utils import truthy


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

    def _get_nullable(self, key, value_lambda=lambda v: v):
        value = self._props.get(key)

        return value_lambda(value) if value else None

    def _get_nullable_csv_list(self, key, value_lambda=lambda v: v):
        value = self._props.get(key)

        if not value:
            return []

        return [value_lambda(v) for v in value.split(",")]

    def _get_nullable_enum(self, key, enum_type):
        return self._get_nullable(key, enum_type)

    def _get_params(self):
        return copy.deepcopy(self._props)

    def _set_nullable(self, key, value):
        if value is None:
            self._props.pop(key, None)
        else:
            self._props[key] = value

    def _set_nullable_bool(self, key, value):
        value = truthy(value, True)

        self._set_nullable(key, value)

    def _set_nullable_csv_list(self, key, value, value_lambda=lambda v: v):
        if isinstance(value, basestring):
            if len(value.strip()) == 0:
                value = []
            else:
                # turn string into string list
                value = [v.strip() for v in value.split(",")]

        self._set_nullable(key, ",".join([value_lambda(v) for v in value]) if value else None)

    def _set_nullable_enum(self, key, value, enum_type):
        if isinstance(value, basestring):
            if len(value.strip()) == 0:
                value = None

        value = enum_type(value).value if value else None

        self._set_nullable(key, value)

    def _set_params(self, params):
        self._props = copy.deepcopy(params)