from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from datetime import (datetime, timedelta)
from dateutil import tz

from .._endpoint_base import _EndpointBase
from .._utils import send_session_request

class UploadedItem(_EndpointBase):

    # replaces tzinfo with UTC, as bizarely utcfromtimestamp comes with no timezone info (despit UTC being in the name)
    _epoch = datetime.utcfromtimestamp(0).replace(tzinfo=tz.tzutc())

    def __init__(self, requests_session, server_url):
        super().__init__(requests_session, server_url)

        self._pdata = {}

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
    def path_on_server(self):
        return self._pdata["path_on_server"]

    @property
    def date(self):
        return self._epoch + timedelta(milliseconds = self._pdata["date"])

    @property
    def committed(self):
        return self._pdata["committed"]

    @property
    def service_name(self):
        return self._pdata["service_name"]

    @property
    def content_type(self):
        return self._pdata["content_type"]

    @property
    def _url_full(self):
        return "{0}/uploads/{1}".format(self._url_base, self.id)

    def delete(self):
        """
        Deletes the uploaded item from the server.
        """
        return send_session_request(
            self._session,
            self._create_operation_request(
                self,
                operation = "delete",
                method = "POST"
            )
        ).json()

    @staticmethod
    def _create_from_json(item_json, session, url_base):
        new_item = UploadedItem(session, url_base)

        new_item._pdata["id"] = item_json["itemID"]
        new_item._pdata["name"] = item_json["itemName"]
        new_item._pdata["description"] = item_json["description"]
        new_item._pdata["path_on_server"] = item_json["pathOnServer"]
        new_item._pdata["date"] = item_json["date"]
        new_item._pdata["committed"] = item_json["committed"]
        new_item._pdata["service_name"] = item_json["serviceName"]
        new_item._pdata["content_type"] = item_json["contentType"]

        return new_item