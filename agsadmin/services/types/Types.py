from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ..._endpoint_base import EndpointBase
from ..._utils import send_session_request
from .extensions import Extensions

class Types(EndpointBase):

    def __init__(self, requests_session, server_url):
        super().__init__(requests_session, server_url)

        self._extensions = Extensions(requests_session, server_url)

    @property
    def extensions(self):
        return self._extensions

    @property
    def _url_full(self):
        return "{0}/services/types".format(self._url_base)