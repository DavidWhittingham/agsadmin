from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from .._PortalEndpointBase import PortalEndpointBase
from .Item import Item
from .users import Users


class Content(PortalEndpointBase):
    def __init__(self, requests_session, url_base):
        super().__init__(requests_session, url_base)

        self._pdata = {"users": Users(self._session, self._url_full)}

    @property
    def _url_full(self):
        return "{0}/content".format(self._url_base)

    @property
    def users(self):
        return self._pdata["users"]

    def get_item(self, item_id):
        """
        Gets a content item in the portal.
        """

        return Item(self._session, self._url_full, item_id)