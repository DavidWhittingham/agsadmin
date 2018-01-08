import requests

from agsadmin._endpoint_base import _EndpointBase
from agsadmin._utils import send_session_request

class Machine(_EndpointBase):

    _pdata = {}

    def __init__(self, requests_session, server_url, machine_name):
        super(Machine, self).__init__(requests_session, server_url)
        self._pdata["name"] = machine_name

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

        send_session_request(self._session, requests.Request("POST", "{0}/start".format(self._url_full)))

    def stop(self):
        """
        Stops the ArcGIS Service.
        """

        send_session_request(self._session, requests.Request("POST", "{0}/stop".format(self._url_full)))