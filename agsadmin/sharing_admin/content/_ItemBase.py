from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ..._utils import send_session_request
from .._PortalEndpointBase import PortalEndpointBase
from .SetContentStatusParams import SetContentStatusParams


class ItemBase(PortalEndpointBase):
    @property
    def id(self):
        return self._pdata["id"]

    @property
    def _url_full(self):
        return "{0}/items/{1}".format(self._url_base, self.id)

    def __init__(self, requests_session, url_base, item_id):
        super().__init__(requests_session, url_base)

        self._pdata = {"id": item_id}

    def get_properties(self):
        """
        Gets the properties of the item.
        """
        return self._get()

    def get_thumbnail(self):
        props = self.get_properties()
        if not props["thumbnail"]:
            return None

        r = self._create_operation_request(self, "info/{}".format(props["thumbnail"]), method="GET")

        return send_session_request(self._session, r, ags_operation=False).content
    
    def set_content_status(self, set_content_status_params):
        set_content_status_params = set_content_status_params._get_params() if isinstance(
            set_content_status_params, SetContentStatusParams) else set_content_status_params

        r = self._create_operation_request(self, "setContentStatus", method="POST", data=set_content_status_params)

        return send_session_request(self._session, r).json()

    def share(self, everyone, org, groups, confirm_item_control):
        r = self._create_operation_request(self, "share", method="POST")

        r.data = {"everyone": everyone == True or False, "org": org == True or False}

        if groups != None:
            r.data["groups"] = ",".join(groups)

        if confirm_item_control != None:
            r.data["confirmItemControl"] = confirm_item_control == True or False

        return send_session_request(self._session, r).json()

    def unshare(self, groups):
        r = self._create_operation_request(self, "unshare", method="POST", data={"groups": ",".join(groups)})

        return send_session_request(self._session, r).json()