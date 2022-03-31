from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

# local imports
from ..._params_mixins.ItemParamsMixin import ItemParamsMixin
from ..._ParamsBase import ParamsBase
from ..ItemType import ItemType


class AddItemParams(ItemParamsMixin, ParamsBase):
    """Holds parameter values for the "addItems" user content operation."""
    @property
    def file(self):
        self._get_nullable("file")

    @file.setter
    def file(self, value):
        self._set_nullable("file", value)

    @property
    def type(self):
        self._get_nullable_enum("type", ItemType)

    @type.setter
    def type(self, value):
        self._set_nullable_enum("type", value, ItemType)