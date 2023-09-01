from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ....._endpoint_base import EndpointBase
from ....._utils import send_session_request


class Cache(EndpointBase):

    def __init__(self, requests_session, server_url):
        super().__init__(requests_session, server_url)

    def clear(self, folder_name=None, service_name=None, service_type=None):
        return send_session_request(
            self._session,
            self._create_operation_request(self,
                                           "clear",
                                           data={
                                               "folderName": folder_name,
                                               "serviceName": service_name,
                                               "type": service_type
                                           })).json()

    @property
    def _url_full(self):
        return "{0}/system/handlers/rest/cache".format(self._url_base)