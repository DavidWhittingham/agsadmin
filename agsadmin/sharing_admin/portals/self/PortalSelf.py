from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ...._utils import send_session_request
from ..._PortalEndpointBase import PortalEndpointBase
from ..Role import Role
from ..RolesResponse import RolesResponse


class PortalSelf(PortalEndpointBase):

    _roles = None

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
    
    def create_role(self, name, description):
        r = self._create_operation_request(self, "createRole", method="POST", data={
            "name": name,
            "description": description
        })
        response_json = send_session_request(self._session, r).json()

        # get new role properties
        r = self._create_operation_request(self, "roles/{}".format(response_json["id"]))
        role_json = send_session_request(self._session, r).json()

        # add a privileges key, which is missing
        role_json["privileges"] = []

        return Role(self._session, "{}/roles".format(self._url_full), role_json)

    def get_roles(self, start=1, num=10):
        r = self._create_operation_request(self, "roles", data={
            "start": start,
            "num": num,
            "returnPrivileges": True
        })
        roles_json = send_session_request(self._session, r).json()

        return RolesResponse(
            roles_json["start"],
            roles_json["num"],
            roles_json["total"],
            roles_json["nextStart"],
            [Role(self._session, "{}/roles".format(self._url_full), role_json) for role_json in roles_json["roles"]]
        )