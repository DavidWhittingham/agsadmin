from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ..._endpoint_base import EndpointBase
from ..._utils import send_session_request
from .Item import Item
from .UserItem import UserItem

class Content(EndpointBase):
    
    def __init__(self, requests_session, url_base):
        super().__init__(requests_session, url_base)

    @property
    def _url_full(self):
        return "{0}/content".format(self._url_base)
    
    def get_user_item(self, username, item_id):
        """
        Gets a link to a content item in the portal owned by a particular user.
        """

        return UserItem(self._session, self._url_full, username, item_id)

    def get_item(self, item_id):
        """
        Gets a content item in the portal.
        """

        return Item(self._session, self._url_full, item_id)