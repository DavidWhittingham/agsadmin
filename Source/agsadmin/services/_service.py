import abc
from copy import deepcopy
from json import dumps

from agsadmin.exceptions import UnknownServiceError, CommunicationError
from agsadmin._utils import send_session_request
from agsadmin._endpoint_base import _EndpointBase
from ._permissions_mixin import _PermissionsMixin


class _Service(_PermissionsMixin, _EndpointBase):
    """
    Base class for all types of ArcGIS Server services. Implements the core operations supported by all services,
    and decribes abstract properties that need to be supported by all implementors.
    """

    __metaclass__ = abc.ABCMeta
    
    def __init__(self, session, url_base):
        super(_Service, self).__init__(session, url_base)

    def __str__(self):
        return self.name

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
    def get_iteminfo(self):
        """
        Gets the item info (description, summary, tags, etc.) of the service.
        """
        return send_session_request(self._session, self._create_operation_request(self._url_full, "iteminfo")).json()

    def get_properties(self):
        """
        Gets the properties of the service.
        """
        return send_session_request(
            self._requests_session,
            service_class._create_operation_request(self._url_full, method = "GET")).json()

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
        return send_session_request(self._session, r).json()

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