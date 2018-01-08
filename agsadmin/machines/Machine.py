from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from .._endpoint_base import _EndpointBase
from .._utils import send_session_request

class Machine(_EndpointBase):

    def __init__(self, requests_session, server_url):
        super().__init__(requests_session, server_url)
        self._pdata = {}

    ################
    ## PROPERTIES ##
    ################
    @property
    def name(self):
        return self._pdata["name"]

    @property
    def _url_full(self):
        return "{0}/machines/{1}".format(self._url_base, self.name)

    ####################
    ## PUBLIC METHODS ##
    ####################
    def start(self):
        """
        Starts the ArcGIS Service.
        """

        send_session_request(self._session, self._create_operation_request(self, "start", "POST"))

    def stop(self):
        """
        Stops the ArcGIS Service.
        """

        send_session_request(self._session, self._create_operation_request(self, "stop", "POST"))

    @staticmethod
    def _create_from_json(machine_json, session, url_base):
        new_machine = Machine(session, url_base)

        new_machine._pdata["name"] = machine_json["machineName"]
        new_machine._pdata["admin_url"] = machine_json["adminURL"]
        new_machine._pdata["synchronize"] = machine_json["synchronize"]

        return new_machine