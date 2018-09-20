from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ...._endpoint_base import EndpointBase
from ...._utils import send_session_request

class User(EndpointBase):

    @property
    def username(self):
        return self._pdata["username"]

    @property
    def _url_full(self):
        return "{0}/{1}".format(self._url_base, self.username)

    def __init__(self, requests_session, url_base, username):
        super().__init__(requests_session, url_base)

        self._pdata = {
            "username": username
        }

    def get_properties(self):
        """
        Gets the properties of the item.
        """
        return self._get()