from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ...._endpoint_base import EndpointBase
from ...._utils import send_session_request
from .Group import Group

class Groups(EndpointBase):

    def __init__(self, requests_session, url_base):
        super().__init__(requests_session, url_base)

    @property
    def _url_full(self):
        return "{0}/groups".format(self._url_base)

    def get(self, id):
        return Group(self._session, self._url_full, id)