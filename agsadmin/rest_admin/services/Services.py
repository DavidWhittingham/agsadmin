from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ..._endpoint_base import EndpointBase
from ..._utils import send_session_request
from ._folder_mixin import _FolderMixin
from .Folder import Folder
from .Service import Service
from .ServiceType import ServiceType
from .types import Types

class Services(_FolderMixin, EndpointBase):

    def __init__(self, requests_session, server_url):
        super().__init__(requests_session, server_url)

        self._types = Types(requests_session, server_url)

    @property
    def types(self):
        return self._types

    @property
    def _url_full(self):
        return "{0}/services".format(self._url_base)

    def list_folders(self):
        """
        Gets a list of machine proxy objects for machines registered on the server.
        """
        response = self._get()

        folders = []
        for f in response["foldersDetail"]:
            folders.append(Folder._create_from_json(f, self._session, self._url_base))

        return folders

    def list_services(self):
        """
        Gets a list of machine proxy objects for machines registered on the server.
        """
        response = self._get()

        services = []
        for s in response["services"]:
            services.append(Service._create_from_json(s, self._session, self._url_base, s["folderName"]))

        return services

    def get_folder(self, name):
        response = self._get()

        for f in response["foldersDetail"]:
            if f["folderName"].lower() == name.lower():
                return Folder._create_from_json(f, self._session, self._url_base)

        raise Exception("Folder with the name '{0}' could not be found.".format(name))

    def get_service(self, service_name, service_type, folder_name = None):
        """Gets a service proxy object by name, type and folder (optional).
        Currently allowed service types are: MapServer, GpServer"""

        # make sure service type is from the enum
        service_type = ServiceType(service_type)

        if folder_name == None:
            url = "{0}/{1}.{2}".format(self._url_full, service_name, service_type.value)
        else:
            url = "{0}/{1}/{2}.{3}".format(self._url_full, folder_name, service_name, service_type.value)

        service_response = send_session_request(
            self._session,
            self._create_operation_request(url, method = "GET")).json()

        return Service._create_from_json(service_response, self._session, self._url_base, folder_name)