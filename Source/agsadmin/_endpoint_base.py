import abc

class _EndpointBase(object):
    """
    Base class for all ArcGIS Server interactive endpoints.  Contains abstract items for dealing with service 
    communication.
    """
    
    __metaclass__ = abc.ABCMeta
    
    _endpoint_base_data = {}
    
    def __init__(self, session, url_base):
        self._endpoint_base_data["_session"] = session
        self._endpoint_base_data["_url_base"] = url_base
    
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