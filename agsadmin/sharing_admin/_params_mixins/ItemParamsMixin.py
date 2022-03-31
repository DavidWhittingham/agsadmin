from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)


class ItemParamsMixin(object):
    @property
    def description(self):
        self._get_nullable("description")

    @description.setter
    def description(self, value):
        self._set_nullable("description", value)

    @property
    def snippet(self):
        self._get_nullable("snippet")

    @snippet.setter
    def snippet(self, value):
        self._set_nullable("snippet", value)

    @property
    def thumbnail(self):
        self._get_nullable("thumbnail")

    @thumbnail.setter
    def thumbnail(self, value):
        self._set_nullable("thumbnail", value)

    @property
    def title(self):
        self._get_nullable("title")

    @title.setter
    def title(self, value):
        self._set_nullable("title", value)