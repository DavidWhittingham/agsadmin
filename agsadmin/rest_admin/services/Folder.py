from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ..._endpoint_base import EndpointBase
from ..._utils import send_session_request
from ._folder_mixin import _FolderMixin
from ._permissions_mixin import _PermissionsMixin
from .ServiceType import ServiceType

class Folder(_FolderMixin, _PermissionsMixin, EndpointBase):

    def __init__(self, requests_session, server_url, name):
        super().__init__(requests_session, server_url)
        self._name = name

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self._name

    @property
    def _url_full(self):
        return "{0}/services/{1}".format(self._url_base, self.name)

    @staticmethod
    def _create_from_json(folder_json, session, url_base):
        return Folder(session, url_base, folder_json["folderName"])