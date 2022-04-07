from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ..._ParamsBase import ParamsBase


class ReplaceServiceParams(ParamsBase):
    @property
    def to_replace_item_id(self):
        self._get_nullable("toReplaceItemId")

    @to_replace_item_id.setter
    def to_replace_item_id(self, value):
        self._set_nullable("toReplaceItemId", value)

    @property
    def replacement_item_id(self):
        self._get_nullable("replacementItemId")

    @replacement_item_id.setter
    def replacement_item_id(self, value):
        self._set_nullable("replacementItemId", value)

    @property
    def replaced_service_name(self):
        self._get_nullable("replacedServiceName")

    @replaced_service_name.setter
    def replaced_service_name(self, value):
        self._set_nullable("replacedServiceName", value)

    @property
    def replace_metadata(self):
        self._get_nullable("replaceMetadata")

    @replace_metadata.setter
    def replace_metadata(self, value):
        self._set_nullable_bool("replaceMetadata", value)
