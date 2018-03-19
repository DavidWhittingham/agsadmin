from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from os import path

from .._endpoint_base import EndpointBase
from .._utils import send_session_request
from .UploadedItem import UploadedItem

class Uploads(EndpointBase):

    def __init__(self, requests_session, server_url):
        super().__init__(requests_session, server_url)

    def get(self, id):
        item_json = send_session_request(
            self._session,
            self._create_operation_request("{0}/{1}".format(self._url_full, id), method = "GET")).json()

        return UploadedItem._create_from_json(item_json, self._session, self._url_base)

    def list(self):
        response = self._get()

        items = []
        for item_json in response["items"]:
            items.append(UploadedItem._create_from_json(item_json, self._session, self._url_base))

        return items

    def upload(self, path_to_file, description = None):
        """
        Uploads the specified file to ArcGIS Server
        """

        return send_session_request(
            self._session,
            self._create_operation_request(
                self,
                operation = "upload",
                method = "POST",
                data = { "description": description } if description != None else None,
                files = { "itemFile": (path.basename(path_to_file), open(path_to_file, 'rb'), 'application/octet-stream', {'Expires': '0'}) }
            )
        ).json()

    @property
    def _url_full(self):
        return "{0}/uploads".format(self._url_base)