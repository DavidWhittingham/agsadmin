from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

import abc
import collections
import json
import mimetypes
import os

from future.utils import iteritems
from requests import Request
from requests.utils import to_key_val_list
from requests_toolbelt import MultipartEncoder

from .._endpoint_base import EndpointBase


class PortalEndpointBase(EndpointBase):
    """
    Base class for all ArcGIS Portal interactive endpoints.  Contains abstract items for dealing with service
    communication.
    """

    __metaclass__ = abc.ABCMeta

    @classmethod
    def _create_operation_request(cls, endpoint, operation=None, method="POST", data=None, files=None):
        """
        Creates an operation request against a given ArcGIS Server endpoint.

        :param endpoint: The endpoint on which to perform the operation.
        :type base_url: str or object implementing agsadmin._endpoint_base

        :param operation: The operation to perform. If None, the endpoint metadata is returned.
        :type operation: str

        :param method: Overrides the HTTP verb to use on the request, default is POST but some operations
                       accept/require GET
        :type method: str
        """

        files = to_key_val_list(files or {})

        # data may come in as an object containing other complex objects types (e.g. strings, lists), these should be
        # encoded to JSON strings
        if not data == None:
            encoded_data = {}
            for key, value in iteritems(data):
                if isinstance(value, collections.Mapping):
                    encoded_data[key] = json.dumps(value)
                elif isinstance(value, list):
                    encoded_data[key] = json.dumps(value)
                else:
                    encoded_data[key] = value
            data = encoded_data

        if files:
            # determine if we need to take any data paramaters and send them as files
            cls._move_data_to_files(data, files, "file", "thumbnail")

            data_to_send = {}
            if data:
                data_to_send.update(data)
            data_to_send.update(files)
            m = MultipartEncoder(fields=data_to_send)

            return Request(method,
                           "{endpoint}/{operation}".format(
                               endpoint=endpoint._url_full if isinstance(endpoint, EndpointBase) else endpoint,
                               operation=operation if operation else ""),
                           data=m,
                           headers={"Content-Type": m.content_type})

        return Request(method,
                       "{endpoint}/{operation}".format(
                           endpoint=endpoint._url_full if isinstance(endpoint, EndpointBase) else endpoint,
                           operation=operation if operation else ""),
                       data=data)

    @staticmethod
    def _move_data_to_files(data, files, *args):
        for key in args:
            if key in data and not data[key] is None:
                p = data[key]
                files.append((key, (os.path.basename(p), open(p, "rb"), mimetypes.guess_type(p, False)[0])))
                del data[key]
