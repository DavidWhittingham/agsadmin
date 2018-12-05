from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

import copy
import mimetypes
import os

from ...._endpoint_base import EndpointBase
from ...._utils import send_session_request
from .CreateUpdateGroupParams import CreateUpdateGroupParams
from .Group import Group


class Groups(EndpointBase):
    def __init__(self, requests_session, url_base):
        super().__init__(requests_session, url_base)

    @property
    def _url_full(self):
        return "{0}/groups".format(self._url_base)

    def get(self, id):
        return Group(self._session, self._url_full, id)

    def create(self, create_group_params):

        create_group_params = create_group_params._get_params() if isinstance(
            create_group_params, CreateUpdateGroupParams) else copy.deepcopy(create_group_params)

        if "thumbnail" in create_group_params:
            thumbnail_path = create_group_params["thumbnail"]
            del create_group_params["thumbnail"]
            r = self._create_operation_request(
                self._url_base,
                "createGroup",
                method="POST",
                data=create_group_params,
                files={
                    "thumbnail": (os.path.basename(thumbnail_path), open(thumbnail_path, "rb"),
                                  mimetypes.guess_type(thumbnail_path, False)[0])
                })
        else:
            r = self._create_operation_request(self._url_base, "createGroup", method="POST", data=create_group_params)

        return send_session_request(self._session, r).json()