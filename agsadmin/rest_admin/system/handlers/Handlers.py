from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ...._endpoint_base import EndpointBase
from .rest import Rest


class Handlers(EndpointBase):

    def __init__(self, requests_session, server_url):
        super().__init__(requests_session, server_url)

        self._rest = Rest(requests_session, self._url_base)

    @property
    def rest(self):
        return self._rest

    @property
    def _url_full(self):
        return "{0}/system/handlers".format(self._url_base)