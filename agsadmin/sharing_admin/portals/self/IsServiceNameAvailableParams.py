from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ..._ParamsBase import ParamsBase


class IsServiceNameAvailableParams(ParamsBase):
    @property
    def service_name(self):
        self._get_nullable("name")

    @service_name.setter
    def service_name(self, value):
        self._set_nullable("name", value)

    @property
    def service_type(self):
        self._get_nullable("type")

    @service_type.setter
    def service_type(self, value):
        self._set_nullable("type", value)
