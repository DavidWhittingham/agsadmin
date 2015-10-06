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
        super(_GpServer, self).__init__(requests_session, server_url)
        self._pdata["name"] = service_name
        self._pdata["folder"] = folder_name
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
    def _type(self):
        return _SERVICE_TYPE

    #####################
    ## PRIVATE METHODS ##
    #####################
    @staticmethod
    def _get_service_url(base_url, service_name, folder = None):
        """
        Constructs the full URL for a service endpoint.
        
        :param base_url: The base URL of the ArcGIS Server Admin API (usually 'http://serverName:port/instance_name/admin')
        :type base_url: str
        
        :param service_name: The name of the service to perform an operation on.
        :type service_name: str
        
        :param folder_name: If the service is not at the root level, specify the folder it resides in.
        :type folder_name: str
        """
        return _Service._get_service_url(base_url, service_name, _SERVICE_TYPE, folder)