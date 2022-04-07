from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

# local imports
from ..._params_mixins.ItemParamsMixin import ItemParamsMixin
from ..._ParamsBase import ParamsBase


class UpdateItemParams(ItemParamsMixin, ParamsBase):
    """Holds parameter values for the "addItems" user content operation."""
    @property
    def asynchronous(self):
        return self._props.get("async")

    @asynchronous.setter
    def asynchronous(self, value):
        self._set_nullable_bool("async", value)

    @property
    def file(self):
        self._get_nullable("file")

    @file.setter
    def file(self, value):
        self._set_nullable("file", value)

    @property
    def file_name(self):
        self._get_nullable("filename")

    @file_name.setter
    def file_name(self, value):
        self._set_nullable("filename", value)

    @property
    def multipart(self):
        self._get_nullable("multipart")

    @multipart.setter
    def multipart(self, value):
        self._set_nullable_bool("multipart", value)