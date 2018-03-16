from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from .Service import Service

_SERVICE_TYPE = "SearchServer"

class SearchServer(Service):
    """
    A class representing ArcGIS Server Search services.
    
    Allows you to perfrom typical administrative functions on the service.
    """

    def __init__(self, requests_session, server_url, service_name, folder_name = None):
        super().__init__(requests_session, server_url, service_name, folder_name, _SERVICE_TYPE)