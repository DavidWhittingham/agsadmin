import requests

from agsadmin._endpoint_base import _EndpointBase
from agsadmin._utils import send_session_request

class Machine(_EndpointBase):

    _pdata = {}

    def __init__(self, requests_session, server_url, machine_name):
        self._pdata["_session"] = requests_session
        self._pdata["name"] = machine_name
        self._pdata["_url_base"] = server_url
        self._start_url = "{0}/machines/{1}/start".format(server_url, machine_name)
        self._stop_url = "{0}/machines/{1}/stop".format(server_url, machine_name)

    ################
    ## PROPERTIES ##
    ################
    @property
    def name(self):
        return self._pdata["name"]

    @property
    def _session(self):
        return self._pdata["_session"]

    @property
    def _url_base(self):
        return self._pdata["_url_base"]

    ####################
    ## PUBLIC METHODS ##
    ####################
    def start(self):
        """
        Starts the ArcGIS Service.
        """

        send_session_request(self._session, requests.Request("POST", self._start_url))

    def stop(self):
        """
        Stops the ArcGIS Service.
        """

        send_session_request(self._session, requests.Request("POST", self._stop_url))