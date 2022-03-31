from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ...._utils import send_session_request
from ..._PortalEndpointBase import PortalEndpointBase
from .AddItemParams import AddItemParams
from .ListItemsParams import ListItemsParams
from .PublishParams import PublishParams
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

    def add_item(self, add_item_params):
        add_item_params = add_item_params._get_params() if isinstance(add_item_params,
                                                                      AddItemParams) else add_item_params
        r = self._create_operation_request(self, "addItem", method="POST", data=add_item_params)
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

    def publish(self, publish_params):
        publish_params = publish_params._get_params() if isinstance(publish_params, PublishParams) else publish_params
        r = self._create_operation_request(self, "publish", method="POST", data=publish_params)
        return send_session_request(self._session, r).json()

    def replace_service(self, replace_service_request):
        r = self._create_operation_request(self, "replaceService", method="POST", data=replace_service_request)
        return send_session_request(self._session, r).json()