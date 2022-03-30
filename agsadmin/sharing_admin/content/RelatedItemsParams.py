from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

try:
    from collections.abc import Sequence
except ImportError:
    # try older import location
    from collections import Sequence

# third-party lib imports
from past.builtins import basestring

# local imports
from .._ParamsBase import ParamsBase
from .ItemRelationshipType import ItemRelationshipType
from .ItemRelationshipDirection import ItemRelationshipDirection


class RelatedItemsParams(ParamsBase):
    """Holds parameter values for the "relatedItems" content item request."""
    @property
    def direction(self):
        """Gets or sets the relationship direction."""

        value = self._props.get("direction")

        if value is None or len(value) == 0:
            return None

        return ItemRelationshipDirection(value)

    @direction.setter
    def direction(self, value):

        if isinstance(value, basestring):
            if len(value.strip()) == 0:
                value = None

        if not value:
            self._props.pop("direction", None)
        else:
            self._props["direction"] = ItemRelationshipDirection(value).value

    @property
    def relationship_types(self):
        """Gets or sets the access relationship types to query for."""

        value = self._props.get("relationshipTypes")

        if value is None or len(value) == 0:
            return []

        return [ItemRelationshipType(rt.strip()) for rt in value.split(",")]

    @relationship_types.setter
    def relationship_types(self, value):

        if isinstance(value, basestring):
            if len(value.strip()) == 0:
                value = []
            else:
                # turn string into string list
                value = [rt.strip() for rt in value.split(",")]

        # should now have a list of strings or enums
        # make sure all the values are valid by making them enums before serializing
        # check for empty list
        self._props["relationshipTypes"] = "" if len(value) == 0 else ",".join(
            [ItemRelationshipType(rt).value for rt in value])
