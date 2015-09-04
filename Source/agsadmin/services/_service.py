import abc
from copy import deepcopy
from json import dumps

from requests import Request

from agsadmin._utils import send_session_request, create_operation_request
from agsadmin._endpoint_base import _EndpointBase


class _Service(_EndpointBase):
    """
    Base class for all types of ArcGIS Server services. Implements the core operations supported by all services,
    and decribes abstract properties that need to be supported by all implementors.
    """

    __metaclass__ = abc.ABCMeta

    _properties = None

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

    ####################
    ## PUBLIC METHODS ##
    ####################
    def stop_service(self):
        """
        Stops the ArcGIS Service.
        """
        return send_session_request(self._session, create_operation_request(
                    self._url_base, self.name, self._type, "stop", self.folder)).json()

    def start_service(self):
        """
        Starts the ArcGIS Service.
        """
        return send_session_request(self._session, create_operation_request(
                    self._url_base, self.name, self._type, "start", self.folder)).json()

    def get_statistics(self):
        """
        Gets statistics for the ArcGIS Service.
        """
        return send_session_request(self._session, create_operation_request(
                    self._url_base, self.name, self._type, "statistics", self.folder)).json()

    def get_status(self):
        """
        Gets the current status of the ArcGIS Service.
        """
        return send_session_request(self._session, create_operation_request(
                    self._url_base, self.name, self._type, "status", self.folder)).json()

    def get_iteminfo(self):
        """
        Gets the item info (description, summary, tags, etc.) of the service.
        """
        return send_session_request(self._session, create_operation_request(
                    self._url_base, self.name, self._type, "iteminfo", self.folder)).json()

    def set_iteminfo(self, new_info):
        """
        Sets the item info (description, summary, tags, etc.) for the service.  Note that this will completely 
        overwrite the existing item info, so make sure all attributes are included.
        """
        r = create_operation_request(
                    self._url_base, self.name, self._type, "iteminfo/edit", self.folder)
        r.data = {"serviceItemInfo": dumps(new_info)}
        return send_session_request(self._session, r).json()

    def set_properties(self, new_properties):
        """
        Sets the properties of the service. Note that this will completely overwrite the existing service properties,
        so make sure all attributes are included.
        """
        r = create_operation_request(
                    self._url_base, self.name, self._type, "edit", self.folder)
        r.data = {"service": dumps(new_properties)}
        response = send_session_request(self._session, r).json()

        #self._properties set after HTTP request incase exception is thrown
        self._properties = deepcopy(new_properties)
        return response