from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ...._utils import send_session_request
from ..._PortalEndpointBase import PortalEndpointBase
from .User import User


class Users(PortalEndpointBase):
    def __init__(self, requests_session, url_base):
        super().__init__(requests_session, url_base)

    @property
    def _url_full(self):
        return "{0}/users".format(self._url_base)

    def get(self, username=None):
        if username == None:
            username = self._session.auth._username

        return User(self._session, self._url_full, username)