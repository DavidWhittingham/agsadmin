from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)


class RolesResponse(object):
    @property
    def num(self):
        return self._num

    @property
    def next_start(self):
        return self._next_start

    @property
    def start(self):
        return self._start
    
    @property
    def total(self):
        return self._total

    @property
    def roles(self):
        return self._roles

    def __init__(self, start, num, total, next_start, roles):
        super().__init__()
        self._start = start
        self._num = num
        self._total = total
        self._next_start = next_start
        self._roles = roles
