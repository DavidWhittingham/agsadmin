from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

# local imports
from ..._ParamsBase import ParamsBase
from .ResourceAccessType import ResourceAccessType


class UpdateResourcesParams(ParamsBase):
    """Holds parameter values for the "updateResources" operation on a user content item."""
    @property
    def access(self):
        self._get_nullable_enum("access", ResourceAccessType)

    @access.setter
    def access(self, value):
        self._set_nullable_enum("access", value, ResourceAccessType)

    @property
    def file(self):
        self._get_nullable("file")

    @file.setter
    def file(self, value):
        self._set_nullable("file", value)

    @property
    def file_name(self):
        self._get_nullable("fileName")

    @file_name.setter
    def file_name(self, value):
        self._set_nullable("fileName", value)

    @property
    def resources_prefix(self):
        self._get_nullable("resourcesPrefix")

    @resources_prefix.setter
    def resources_prefix(self, value):
        self._set_nullable("resourcesPrefix", value)

    @property
    def text(self):
        self._get_nullable("text")

    @text.setter
    def text(self, value):
        self._set_nullable("text", value)