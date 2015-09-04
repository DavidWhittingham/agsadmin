import abc

class _EndpointBase(object):
    """
    Base class for all ArcGIS Server interactive endpoints.  Contains abstract items for dealing with service 
    communication.
    """
    
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractproperty
    def _session(self):
        """
        Gets the Requests session for interacting with this endpoint.
        """
        return

    @abc.abstractproperty
    def _url_base(self):
        """
        Returns the base URL for this instance of ArcGIS Server.
        """
        return