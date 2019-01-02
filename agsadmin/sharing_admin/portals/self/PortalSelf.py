from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ...._utils import send_session_request
from ..._PortalEndpointBase import PortalEndpointBase


class PortalSelf(PortalEndpointBase):
    @property
    def _url_full(self):
        return "{0}/self".format(self._url_base)

    def __init__(self, requests_session, url_base):
        super().__init__(requests_session, url_base)

    def get_properties(self):
        """
        Gets the properties of the item.
        """
        return self._get()

    def update(self, updated_portal_info):
        r = self._create_operation_request(self, "update", method="POST", data=updated_portal_info)
        return send_session_request(self._session, r).json()