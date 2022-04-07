from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

# local imports
from .UpdateResourcesParams import UpdateResourcesParams


class AddResourcesParams(UpdateResourcesParams):
    """Holds parameter values for the "addResources" operation on a user content item."""
    @property
    def archive(self):
        self._get_nullable("archive")

    @archive.setter
    def archive(self, value):
        self._set_nullable_bool("archive", value)