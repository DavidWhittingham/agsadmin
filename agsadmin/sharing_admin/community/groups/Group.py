from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ...._utils import send_session_request
from ..._PortalEndpointBase import PortalEndpointBase
from .CreateUpdateGroupParams import CreateUpdateGroupParams


class Group(PortalEndpointBase):
    @property
    def id(self):
        return self._pdata["id"]

    @property
    def _url_full(self):
        return "{0}/{1}".format(self._url_base, self.id)

    def __init__(self, requests_session, url_base, id):
        super().__init__(requests_session, url_base)

        self._pdata = {"id": id}

    def get_properties(self):
        """
        Gets the properties of the item.
        """
        return self._get()

    def update(self, update_group_params, clear_empty_fields=False):
        """
        Updates the group properties.
        """

        update_group_params = update_group_params._get_params() if isinstance(
            update_group_params, CreateUpdateGroupParams) else update_group_params.copy()

        if not "clearEmptyFields" in update_group_params:
            update_group_params["clearEmptyFields"] = clear_empty_fields

        r = self._create_operation_request(self, "update", method="POST", data=update_group_params)

        return send_session_request(self._session, r).json()