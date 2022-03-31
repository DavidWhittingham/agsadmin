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

        data = data or {}
        files = to_key_val_list(files or {})

        # determine if we need to take any data paramaters and send them as files
        cls._move_data_to_files(data, files, "file", "thumbnail")

        return super()._create_operation_request(endpoint, operation, method, data, files)

    @staticmethod
    def _move_data_to_files(data, files, *args):
        for key in args:
            if key in data and not data[key] is None:
                p = data.pop(key)

                # test if p is already a tuple
                if type(p) is tuple:
                    # assume already in correct format, expand and open
                    (file_name, file_path, mime_type) = p
                    files.append((key, (file_name, open(file_path, "rb"), mime_type)))
                else:
                    # try to guess filename/mimetype and provide file handler
                    files.append((key, (os.path.basename(p), open(p, "rb"), mimetypes.guess_type(p, False)[0])))