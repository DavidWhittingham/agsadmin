from agsadmin._endpoint_base import _EndpointBase
from agsadmin._utils import send_session_request

class _PermissionsMixin(_EndpointBase):

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