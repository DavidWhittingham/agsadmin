from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ...._utils import send_session_request
from .._ItemBase import ItemBase


class UserItem(ItemBase):
    @property
    def username(self):
        return self._pdata["username"]

    @property
    def _url_full(self):
        return "{0}/items/{1}".format(self._url_base, self.id)

    def __init__(self, requests_session, content_url, username, item_id):
        super().__init__(requests_session, content_url, item_id)

        self._pdata["username"] = username

    def move(self, folder_id):
        r = self._create_operation_request(self, "move", method="POST", data={"folder": folder_id})
        return send_session_request(self._session, r).json()

    def delete(self):
        r = self._create_operation_request(self, "delete", method="POST")
        return send_session_request(self._session, r).json()

    def get_properties(self):
        """
        Gets the properties of the item.
        """
        return self._get()["item"]

    def get_sharing(self):
        """
        Gets the sharing details of the item.
        """
        return self._get().get("sharing")

    def update(self, updated_item_info):
        r = self._create_operation_request(self, "update", method="POST", data=updated_item_info)
        return send_session_request(self._session, r).json()

    def update_thumbnail(self, updated_thumbnail_info):
        r = self._create_operation_request(self, "updateThumbnail", method="POST", data=updated_thumbnail_info)
        return send_session_request(self._session, r).json()