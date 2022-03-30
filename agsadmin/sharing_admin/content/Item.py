from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ..._utils import send_session_request
from ._ItemBase import ItemBase
from .ShareItemParams import ShareItemParams
from .RelatedItemsParams import RelatedItemsParams


class Item(ItemBase):
    def get_data(self):
        r = self._create_operation_request(self, "data", method="POST")
        response = send_session_request(self._session, r)
        try:
            return response.json()
        except ValueError as ve:
            return response.content

    def get_related_items(self, related_items_params):
        related_items_params = related_items_params._get_params() if isinstance(
            related_items_params, RelatedItemsParams) else related_items_params

        r = self._create_operation_request(self, "relatedItems", method="POST", data=related_items_params)
        return send_session_request(self._session, r).content

    def get_data_as_zip(self):
        r = self._create_operation_request(self, "data", method="POST")
        r.data = {"f": "zip"}
        return send_session_request(self._session, r).content

    def get_dependencies(self):
        r = self._create_operation_request(self, "dependencies", method="POST")
        return send_session_request(self._session, r).json()

    def share(self, share_item_params):
        share_item_params = share_item_params._get_params() if isinstance(share_item_params,
                                                                          ShareItemParams) else share_item_params

        return super().share(share_item_params)