from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ..._utils import send_session_request
from .._PortalEndpointBase import PortalEndpointBase


class Role(PortalEndpointBase):
    _pdata = None

    @property
    def id(self):
        return self._pdata["id"]

    @property
    def name(self):
        return self._pdata["name"]
    
    @property
    def description(self):
        return self._pdata["description"]

    @property
    def created(self):
        return self._pdata["created"]

    @property
    def modified(self):
        return self._pdata["modified"]

    @property
    def privileges(self):
        return self._pdata["privileges"]

    @property
    def _url_full(self):
        return "{}/{}".format(self._url_base, self.id)

    def __init__(self, requests_session, url_base, role_json):
        super().__init__(requests_session, url_base)

        self._pdata = role_json

    def update(self, name, description):
        """Update the name and description of the role."""

        r = self._create_operation_request(self, "update", data={
            "name": name,
            "description": description
        })
        response = send_session_request(self._session, r).json()

        # set the name/description locally
        self._pdata["name"] = name
        self._pdata["description"] = description

        return response
    
    def set_privileges(self, privileges):
        """Set the privileges for the role."""

        r = self._create_operation_request(self, "setPrivileges", data={
            "privileges": privileges
        })
        response = send_session_request(self._session, r).json()

        # set the name/description locally
        self._pdata["privileges"] = privileges

        return response