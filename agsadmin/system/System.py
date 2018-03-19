from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from .._endpoint_base import EndpointBase
from .Directories import Directories

class System(EndpointBase):
    
    def __init__(self, requests_session, server_url):
        super().__init__(requests_session, server_url)
        
        self._directories = Directories(requests_session, self._url_base)

    @property
    def directories(self):
        return self._directories
    
    @property
    def _url_full(self):
        return "{0}/system".format(self._url_base)