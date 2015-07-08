from copy import deepcopy

from _service import _Service

_SERVICE_TYPE = "GpServer"

class _GpServer(_Service):
    """
    A class representing ArcGIS Server Geoprocessing services.
    
    Allows you to perfrom typical administrative functions on the service.
    """

    _pdata = {}

    def __init__(self, requests_session, server_url, service_properties, service_name, folder_name = None):
        self._pdata["_session"] = requests_session
        self._pdata["name"] = service_name
        self._pdata["folder"] = folder_name
        self._pdata["_url_base"] = server_url
        self._properties = service_properties

    ################
    ## PROPERTIES ##
    ################
    @property
    def name(self):
        return self._pdata["name"]

    @property
    def folder(self):
        return self._pdata["folder"]

    @property
    def properties(self):
        return deepcopy(self._properties)

    @property
    def _session(self):
        return self._pdata["_session"]

    @property
    def _type(self):
        return _SERVICE_TYPE

    @property
    def _url_base(self):
        return self._pdata["_url_base"]
