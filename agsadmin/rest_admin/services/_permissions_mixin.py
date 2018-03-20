from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ..._endpoint_base import EndpointBase
from ..._utils import send_session_request

class _PermissionsMixin(EndpointBase):

    ####################
    ## PUBLIC METHODS ##
    ####################
    def add_permission(self, principal):
        """
        Adds a user/role to the allowed principals list for an endpoint.
        """
        r = self._create_operation_request(self._url_full, "permissions/add")
        r.data = {"principal": principal, "isAllowed": True}
        send_session_request(self._session, r).json()

    def get_allowed_principals(self):
        """
        Gets a list of the allowed principals on the endpoint.
        """
        r = self._create_operation_request(self._url_full, "permissions")
        response = send_session_request(self._session, r).json()
        return [p["principal"] for p in response["permissions"]]

    def remove_permission(self, principal):
        """
        Removes a user/role from the allowed principals list for an endpoint.
        """
        r = self._create_operation_request(self._url_full, "permissions/add")
        r.data = {"principal": principal, "isAllowed": False}
        send_session_request(self._session, r).json()