from _service import _Service

_SERVICE_TYPE = "GeocodeServer"

class _GeocodeServer(_Service):
    """
    A class representing ArcGIS Server Geocode services.
    
    Allows you to perfrom typical administrative functions on the service.
    """

    def __init__(self, requests_session, server_url, service_name, folder_name = None):
        super(_GeocodeServer, self).__init__(requests_session, server_url, service_name, folder_name, _SERVICE_TYPE)