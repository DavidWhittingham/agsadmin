from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ...._endpoint_base import EndpointBase
from ...._utils import send_session_request
from ..Item import Item

class UserItem(Item):

    @property
    def username(self):
        return self._pdata["username"]

    @property
    def _url_full(self):
        return "{0}/items/{1}".format(self._url_base, self.id)

    def __init__(self, requests_session, content_url, username, item_id):
        super().__init__(requests_session, content_url, item_id)

        self._pdata["username"] = username

    def delete(self):
        r = self._create_operation_request(self, "delete", method = "POST")

        return send_session_request(self._session, r).json()

    def update(self, updated_item_info):
        r = self._create_operation_request(self, "update", method = "POST", data = updated_item_info)

        return send_session_request(self._session, r).json()