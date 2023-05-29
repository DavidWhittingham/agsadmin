from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from agsadmin.sharing_admin.content.users.UpdateItemParams import UpdateItemParams

# local imports
from ..ItemType import ItemType
from .UpdateItemParams import UpdateItemParams


class AddItemParams(UpdateItemParams):
    """Holds parameter values for the "addItems" user content operation."""
    
    @property
    def type(self):
        self._get_nullable_enum("type", ItemType)

    @type.setter
    def type(self, value):
        self._set_nullable_enum("type", value, ItemType)

    @property
    def item_id_to_create(self):
        """Gets or sets the item ID of the Portal Item to be published."""
        
        return self._props.get("itemIdToCreate")
    
    @item_id_to_create.setter
    def item_id_to_create(self, value):
        self._set_nullable("itemIdToCreate", value)