from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

import abc
from json import dumps

from .._utils import send_session_request
from .._endpoint_base import _EndpointBase
from ._permissions_mixin import _PermissionsMixin
from .ServiceType import ServiceType
from .Folder import Folder

class Service(_PermissionsMixin, _EndpointBase):
    """
    Base class for all types of ArcGIS Server services. Implements the core operations supported by all services,
    and decribes abstract properties that need to be supported by all implementors.
    """

    __metaclass__ = abc.ABCMeta

    _name = None
    _folder = None
    _type_str = None

    def __init__(self, session, url_base, name, folder_name, type_str):
        super().__init__(session, url_base)
        self._name = name
        self._folder = Folder(session, url_base, folder_name) if folder_name != None else None
        self._type_str = type_str

    def __str__(self):
        return self.name

    ################
    ## PROPERTIES ##
    ################
    @property
    def name(self):
        """
        Gets the name of the service.
        """
        return self._name

    @property
    def folder(self):
        """
        Gets the folder the service is in ('None' if service is in the root folder).
        """
        return self._folder

    @property
    def _type(self):
        """
        Gets the type of this service
        """
        return self._type_str

    @property
    def _url_full(self):
        # Use _Service rather than self because method is possibly overridden
        return _Service._get_service_url(self._url_base, self.name, self._type, self.folder)

    ####################
    ## PUBLIC METHODS ##
    ####################
    def delete(self):
        return send_session_request(self._session, self._create_operation_request(self, "delete")).json()

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
            self._session,
            self._create_operation_request(self._url_full, method = "GET")).json()

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

    @staticmethod
    def _create_from_json(service_json, session, url_base, folder_name):
        service_enum = ServiceType(service_json["type"])
        service_name = service_json["serviceName"]

        return ServiceType._get_proxy(service_enum)(
                        session,
                        url_base,
                        service_name,
                        folder_name)