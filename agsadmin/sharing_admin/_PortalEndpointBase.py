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

from .._endpoint_base import EndpointBase


class PortalEndpointBase(EndpointBase):
    """
    Base class for all ArcGIS Portal interactive endpoints.  Contains abstract items for dealing with service
    communication.
    """

    __metaclass__ = abc.ABCMeta

    @staticmethod
    def _create_operation_request(endpoint, operation=None, method="POST", data=None, files={}):
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

            # determine if we need to take any data paramaters and send them as files
            if "thumbnail" in data:
                thumbnail_path = data["thumbnail"]
                files["thumbnail"] = (os.path.basename(thumbnail_path), open(thumbnail_path, "rb"),
                                            mimetypes.guess_type(thumbnail_path, False)[0])
                del data["thumbnail"]    

        return Request(
            method,
            "{endpoint}/{operation}".format(
                endpoint=endpoint._url_full if isinstance(endpoint, EndpointBase) else endpoint,
                operation=operation if operation else ""),
            data=data,
            files=files if len(files) > 0 else None)
