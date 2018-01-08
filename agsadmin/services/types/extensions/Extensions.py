from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ...._endpoint_base import _EndpointBase
from ...._utils import send_session_request

class Extensions(_EndpointBase):

    def __init__(self, requests_session, server_url):
        super().__init__(requests_session, server_url)

    @property
    def _url_full(self):
        return "{0}/services/types/extensions".format(self._url_base)

    def register(self, item_id):
        """
        Registers the specified extension with ags
        """

        return send_session_request(
            self._session, 
            self._create_operation_request(
                self,
                operation = "register",
                method = "POST",
                data = { "id": item_id }
            )
        ).json()

    def unregister(self, extension_name):
        """
        Unregisters the specified extension from ags
        """

        return send_session_request(
            self._session, 
            self._create_operation_request(
                self,
                operation = "unregister",
                method = "POST",
                data = { "extensionFilename": extension_name }
            )
        ).json()
