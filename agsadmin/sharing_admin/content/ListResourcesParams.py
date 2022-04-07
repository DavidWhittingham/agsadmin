from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

# local imports
from .._params_mixins.PagingParamsMixin import PagingParamsMixin
from .._ParamsBase import ParamsBase
from .SortFieldType import SortFieldType
from .SortOrderType import SortOrderType


class ListResourcesParams(PagingParamsMixin, ParamsBase):
    """Holds parameter values for the "resources" content user item request."""
    @property
    def sort_field(self):
        """Gets or sets the output type of the published service."""

        return self._get_nullable_enum("sortField", SortFieldType)

    @sort_field.setter
    def sort_field(self, value):
        self._set_nullable_enum("sortField", value, SortFieldType)

    @property
    def sort_order(self):
        """Gets or sets the output type of the published service."""

        return self._get_nullable_enum("sortOrder", SortOrderType)

    @sort_order.setter
    def sort_order(self, value):
        self._set_nullable_enum("sortOrder", value, SortOrderType)