from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ..._endpoint_base import EndpointBase
from ..._utils import send_session_request
from .Item import Item

class UserItem(Item):

    @property
    def username(self):
        return self._pdata["username"]

    @property
    def _url_full(self):
        return "{0}/users/{1}/items/{2}".format(self._url_base, self.username, self.id)

    def __init__(self, requests_session, content_url, username, item_id):
        super().__init__(requests_session, content_url, item_id)

        self._pdata["username"] = username