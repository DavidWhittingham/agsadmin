from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ...._endpoint_base import EndpointBase
from ...._utils import send_session_request
from .UserContent import UserContent

class Users(EndpointBase):

    def __init__(self, requests_session, url_base):
        super().__init__(requests_session, url_base)

    @property
    def _url_full(self):
        return "{0}/users".format(self._url_base)

    def get_user_content(self, username=None):
        if username == None:
            username = self._session.auth._username

        return UserContent(self._session, self._url_full, username)