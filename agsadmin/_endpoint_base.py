from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

import abc
import collections
import json

from future.utils import iteritems
from requests import Request

from ._utils import send_session_request


class EndpointBase(object):
    """
    Base class for all ArcGIS Server interactive endpoints.  Contains abstract items for dealing with service
    communication.
    """

    __metaclass__ = abc.ABCMeta

    def __init__(self, session, url_base):
        self._endpoint_base_data = {"_session": session, "_url_base": url_base}

    @property
    def _session(self):
        """
        Gets the Requests session for interacting with this endpoint.
        """
        return self._endpoint_base_data["_session"]

    @property
    def _url_base(self):
        """
        Returns the base URL for this instance of ArcGIS Server.
        """
        return self._endpoint_base_data["_url_base"]

    @abc.abstractproperty
    def _url_full(self):
        """
        Returns the full URL for this endpoint.
        """
        return

    def _get(self):
        return send_session_request(self._session, self._create_operation_request(self, method="GET")).json()

    @staticmethod
    def _create_operation_request(endpoint, operation=None, method="POST", data=None, files=None):
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

        return Request(
            method,
            "{endpoint}/{operation}".format(
                endpoint=endpoint._url_full if isinstance(endpoint, EndpointBase) else endpoint,
                operation=operation if operation else ""),
            data=data,
            files=files)
