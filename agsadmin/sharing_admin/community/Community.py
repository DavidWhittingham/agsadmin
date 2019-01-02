from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ..._utils import send_session_request
from .._PortalEndpointBase import PortalEndpointBase
from .users import Users
from .groups import Groups


class Community(PortalEndpointBase):
    def __init__(self, requests_session, url_base):
        super().__init__(requests_session, url_base)
        self._users = Users(self._session, self._url_full)
        self._groups = Groups(self._session, self._url_full)

    @property
    def _url_full(self):
        return "{0}/community".format(self._url_base)

    @property
    def groups(self):
        return self._groups

    @property
    def users(self):
        return self._users