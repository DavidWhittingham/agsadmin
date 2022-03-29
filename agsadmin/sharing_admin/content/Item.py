from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ..._utils import send_session_request
from ._ItemBase import ItemBase


class Item(ItemBase):

    def get_data(self):
        r = self._create_operation_request(self, "data", method="POST")
        response = send_session_request(self._session, r)
        try:
            return response.json()
        except ValueError as ve:
            return response.content
    
    def get_related_items(self, related_items_params):
        r = self._create_operation_request(self, "relatedItems", method="POST")
        r.data = {"f": "zip"}
        return send_session_request(self._session, r).content
    
    def get_data_as_zip(self):
        r = self._create_operation_request(self, "data", method="POST")
        r.data = {"f": "zip"}
        return send_session_request(self._session, r).content

    def get_dependencies(self):
        r = self._create_operation_request(self, "dependencies", method="POST")
        r.data = {"f": "json"}
        return send_session_request(self._session, r).json()