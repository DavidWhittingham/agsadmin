from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from .._endpoint_base import _EndpointBase
from .._utils import send_session_request
from .Machine import Machine

class Machines(_EndpointBase):
    
    def __init__(self, requests_session, server_url):
        super().__init__(requests_session, server_url)

    @property
    def _url_full(self):
        return "{0}/machines".format(self._url_base)
    
    def get(self, name):
        """
        Gets a proxy object for a registered machine given it's name.
        """
        machine_json = send_session_request(
            self._session,
            self._create_operation_request("{0}/{1}".format(self._url_full, name), method = "GET")).json()

        return Machine._create_from_json(machine_json, self._session, self._url_base)

    def list(self):
        """
        Gets a list of machine proxy objects for machines registered on the server.
        """
        response = self._get()

        machines = []
        for m in response["machines"]:
            machines.append(Machine._create_from_json(m, self._session, self._url_base))

        return machines