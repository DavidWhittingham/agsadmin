from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

import copy
import mimetypes
import os

from ...._endpoint_base import EndpointBase
from ...._utils import send_session_request
from .CreateUpdateGroupParams import CreateUpdateGroupParams


class Group(EndpointBase):
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
            update_group_params, CreateUpdateGroupParams) else copy.deepcopy(update_group_params)
        if not "clearEmptyFields" in update_group_params:
            update_group_params["clearEmptyFields"] = clear_empty_fields

        if "thumbnail" in update_group_params:
            thumbnail_path = update_group_params["thumbnail"]
            del update_group_params["thumbnail"]
            r = self._create_operation_request(
                self,
                "updateGroup",
                method="POST",
                data=update_group_params,
                files={
                    "thumbnail": (os.path.basename(thumbnail_path), open(thumbnail_path, "rb"),
                                  mimetypes.guess_type(thumbnail_path, False)[0])
                })
        else:
            r = self._create_operation_request(self, "updateGroup", method="POST", data=update_group_params)

        return send_session_request(self._session, r).json()