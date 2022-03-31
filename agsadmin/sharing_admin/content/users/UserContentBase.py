from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ...._utils import send_session_request
from ..._PortalEndpointBase import PortalEndpointBase
from .ListItemsParams import ListItemsParams
from .UserItem import UserItem


class UserContentBase(PortalEndpointBase):
    def __init__(self, requests_session, url_base, username):
        super().__init__(requests_session, url_base)

        self._pdata = {"username": username}

    @property
    def _url_full(self):
        return "{0}/{1}".format(self._url_base, self.username)

    @property
    def username(self):
        return self._pdata["username"]

    def add_item(self, new_item):
        r = self._create_operation_request(self, "addItem", method="POST", data=new_item)
        return send_session_request(self._session, r).json()

    def get_item(self, item_id):
        """
        Gets a link to a content item in the portal owned by a particular user.
        """

        return UserItem(self._session, self._url_full, self.username, item_id)

    def list_items(self, list_items_params=None):
        """
        Gets a list of item details.
        """

        list_items_params = None if list_items_params == None else list_items_params._get_params() if isinstance(
            list_items_params, ListItemsParams) else list_items_params

        r = self._create_operation_request(self, data=list_items_params)
        return send_session_request(self._session, r).json()

    def publish(self, item_info):
        r = self._create_operation_request(self, "publish", method="POST", data=item_info)
        return send_session_request(self._session, r).json()

    def replace_service(self, replace_service_request):
        r = self._create_operation_request(self, "replaceService", method="POST", data=replace_service_request)
        return send_session_request(self._session, r).json()