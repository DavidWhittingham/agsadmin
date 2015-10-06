import abc
from copy import deepcopy
from json import dumps

from requests import Request

from agsadmin._utils import send_session_request
from agsadmin._endpoint_base import _EndpointBase


class _Service(_EndpointBase):
    """
    Base class for all types of ArcGIS Server services. Implements the core operations supported by all services,
    and decribes abstract properties that need to be supported by all implementors.
    """

    __metaclass__ = abc.ABCMeta

    _properties = None
    
    def __init__(self, session, url_base):
        super(_Service, self).__init__(session, url_base)
        

    ################
    ## PROPERTIES ##
    ################
    @abc.abstractproperty
    def name(self):
        """
        Gets the name of the service.
        """
        return

    @abc.abstractproperty
    def folder(self):
        """
        Gets the folder the service is in ('None' for root folder).
        """
        return

    @abc.abstractproperty
    def properties(self):
        """
        Gets the properties (metadata) of the service.
        """
        return
    
    @abc.abstractproperty
    def _type(self):
        """
        Gets the type of this service
        """
        return
    
    @property
    def _url_full(self):
        # Use _Service rather than self because method is possibly overridden
        return _Service._get_service_url(self._url_base, self.name, self._type, self.folder)

    ####################
    ## PUBLIC METHODS ##
    ####################
    def stop_service(self):
        """
        Stops the ArcGIS Service.
        """
        return send_session_request(self._session, self._create_operation_request(self._url_full, "stop")).json()

    def start_service(self):
        """
        Starts the ArcGIS Service.
        """
        return send_session_request(self._session, self._create_operation_request(self._url_full, "start")).json()

    def get_statistics(self):
        """
        Gets statistics for the ArcGIS Service.
        """
        return send_session_request(self._session, self._create_operation_request(self._url_full, "statistics")).json()

    def get_status(self):
        """
        Gets the current status of the ArcGIS Service.
        """
        return send_session_request(self._session, self._create_operation_request(self._url_full, "status")).json()

    def get_iteminfo(self):
        """
        Gets the item info (description, summary, tags, etc.) of the service.
        """
        return send_session_request(self._session, self._create_operation_request(self._url_full, "iteminfo")).json()

    def set_iteminfo(self, new_info):
        """
        Sets the item info (description, summary, tags, etc.) for the service.  Note that this will completely 
        overwrite the existing item info, so make sure all attributes are included.
        """
        r = self._create_operation_request(self._url_full,  "iteminfo/edit")
        r.data = {"serviceItemInfo": dumps(new_info)}
        return send_session_request(self._session, r).json()

    def set_properties(self, new_properties):
        """
        Sets the properties of the service. Note that this will completely overwrite the existing service properties,
        so make sure all attributes are included.
        """
        r = self._create_operation_request(self._url_full, "edit")
        r.data = {"service": dumps(new_properties)}
        response = send_session_request(self._session, r).json()

        #self._properties set after HTTP request incase exception is thrown
        self._properties = deepcopy(new_properties)
        return response
    
    @staticmethod
    def _create_operation_request(url, operation = None, method = "POST"):
        """
        Creates an operation request against a given ArcGIS Server Service.

        :param url: The full URL of the service endpoint.
        :type base_url: str

        :param operation: The operation to perform.  If None, no operation is sent and the basic service metadata is
            returned.
        :type operation: str

        :param method: Overrides the HTTP verb to use on the request, default is POST but some operations accept/require GET
        :type method: str
        """

        return Request(method, "{endpoint}/{operation}".format(endpoint = url, operation = operation if operation else ""))

    @staticmethod
    def _get_service_url(base_url, service_name, service_type, folder = None):
        """
        Constructs the full URL for a service endpoint.
        
        :param base_url: The base URL of the ArcGIS Server Admin API (usually 'http://serverName:port/instance_name/admin')
        :type base_url: str
        
        :param service_name: The name of the service to perform an operation on.
        :type service_name: str

        :param service_type: The type of the service named in the "service_name" property.
        :type service_type: str
        
        :param folder_name: If the service is not at the root level, specify the folder it resides in.
        :type folder_name: str
        """
        return ("{base}/services/{folder}/{name}.{type}" if folder else "{base}/services/{name}.{type}").format(
                base = base_url,
                folder = folder,
                name = service_name,
                type = service_type
            )