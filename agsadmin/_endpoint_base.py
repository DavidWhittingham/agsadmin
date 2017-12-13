import abc

from requests import Request

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

    @staticmethod
    def _create_operation_request(endpoint, operation = None, method = "POST"):
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

        return Request(method, "{endpoint}/{operation}".format(
            endpoint = endpoint._url_full if isinstance(endpoint, _EndpointBase) else endpoint,
            operation = operation if operation else ""))