from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

# local imports
from ..._ParamsBase import ParamsBase
from ..ItemType import ItemType


class AddPartParams(ParamsBase):
    """Holds parameter values for the "addItems" user content operation."""
    @property
    def file(self):
        self._get_nullable("file")

    @file.setter
    def file(self, value):
        self._set_nullable("file", value)

    @property
    def part_num(self):
        self._get_nullable("partNum")

    @part_num.setter
    def part_num(self, value):
        self._set_nullable("partNum", value)