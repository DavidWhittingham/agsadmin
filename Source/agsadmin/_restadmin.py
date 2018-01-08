from requests.exceptions import ConnectionError, HTTPError

from . import services
from .machines import Machine
from ._auth import _RestAdminAuth
from .exceptions import InvalidServiceTypeError, UnknownServiceError, CommunicationError
from ._utils import get_server_url_base, send_session_request

import requests
import os

from datetime import datetime
from dateutil import tz

class RestAdmin(object):
    """
    Provides a proxy object for an ArcGIS Server instance, communicating with the REST Admin API.
    """

    _server_url_base = None
    _requests_session = None

    @property
    def url(self):
        return self._server_url_base

    def __init__(self, hostname, username, password, instance_name = "arcgis", port = 6080, use_ssl = False,
                 utc_delta = tz.tzlocal().utcoffset(datetime.now()), proxies = None, encrypt = True):
        """
        :param hostname: The hostname (or fully qualified domain name) of the ArcGIS Server.
        :type hostname: str

        :param username: The username used to log on as an administrative user to the ArcGIS Server.
        :type username: str

        :param password: The password for the administrative account used to login to the ArcGIS Server.
        :type password: str

        :param instance_name: The name of the ArcGIS Server instance.  If communication directly with an ArcGIS Server
        instance, you can ignore this setting and use the default.  If accesssing the ArcGIS Server REST Admin API
        through the ArcGIS Web Adaptor and you have customised the instance name, it should be specified here.
        :type instance_name: str

        :param port: The port that the ArcGIS Server is operating on. If communication directly with an ArcGIS Server
        instance, you can ignore this setting and use the default.  If accesssing the ArcGIS Server REST Admin API
        through the ArcGIS Web Adaptor, enter the port the service is running on here.

        :param use_ssl: If True, instructs the REST Admin proxy to communicate with the ArcGIS Server REST Admin API
        via SSL/TLS.  Default is False.
        :type use_ssl: bool

        :param utc_delta: The time difference between UTC and the ArcGIS Server instance.  This is used to calculate
        when the admin token has expired, as Esri foolishly return this value as local server time, making calculation
        of its expiry impossible unless you know what time zone the server is also in.  Defaults to the UTC offset of
        your local machine.
        :type utc_delta: datetime.timedelta

        :param proxies: A dictionary of key/value pairs matching protocol to proxy address.  Required if a proxy is
        needed to access the ArcGIS Server instance.
        :type proxies: dict

        :param encrypt: Is set to True (default), uses public key crypto to encrypt communication with the ArcGIS
        Server instance.  Setting this to False disables public key crypto.  When communicating over SSL, this
        parameter is ignored, as SSL will already encrypt the traffic.
        :type encrypt: bool
        """

        self._server_url_base = get_server_url_base("https" if use_ssl else "http", hostname, port, instance_name)
        self._requests_session = requests.Session()
        self._requests_session.params = {"f": "json"}
        self._requests_session.auth = _RestAdminAuth(
            username,
            password,
            self._server_url_base + "/generateToken",
            utc_delta = utc_delta,
            get_public_key_url = self._server_url_base + "/publicKey" \
                if (use_ssl == False) or (use_ssl == False and encrypt == False) else None,
            proxies = proxies)

        if not proxies == None:
            self._requests_session.proxies = proxies

    def delete_service(self, service_name, service_type, service_folder = None):
        serv_type = service_type.lower()
        if (serv_type in services._type_map):
            url = services._type_map[serv_type]._get_service_url(self._server_url_base, service_name, service_type, service_folder)
            request = services._type_map[serv_type]._create_operation_request(url, operation = "delete", method = "POST")

            try:
                response = send_session_request(self._requests_session, request).json()
            except HTTPError as he:
                if he.response.status_code == 404:
                    raise UnknownServiceError()
                else:
                    raise CommunicationError()
            except ConnectionError:
                raise CommunicationError()
        else:
            raise InvalidServiceTypeError()

    def get_service(self, service_name, service_type, service_folder = None):
        """Gets a service proxy object by name, type and folder (optional).
        Currently allowed service types are: MapServer, GpServer"""

        service_folder = self.get_folder(service_folder)

        serv_type = service_type.lower()
        if (serv_type in services._type_map):
            return services._type_map[serv_type](
                        self._requests_session,
                        self._server_url_base,
                        service_name,
                        service_folder)
        else:
            raise InvalidServiceTypeError()

    def get_folder(self, service_folder):
        if service_folder != None and not isinstance(service_folder, services._Folder):
            service_folder = services._Folder(self._requests_session, self._server_url_base, service_folder)
        return service_folder

    def get_machine(self, name):
        """Gets a machine proxy object by name."""
        return Machine(self._requests_session, self._server_url_base, name)

    def upload_item(self, itemFile, description=""):
        """
        Uploads the specified file to ags
        """
        r = requests.Request("POST", "{0}/uploads/upload".format(self._server_url_base))
        r.data = {"description": description}
        r.files = {"itemFile": (os.path.basename(itemFile.name), itemFile)}
        return send_session_request(self._requests_session, r).json()

    def delete_uploaded_item(self, itemID):
        """
        Deletes an uploaded file from ags
        """
        r = requests.Request("POST", "{0}/uploads/{1}/delete".format(self._server_url_base, itemID))
        return send_session_request(self._requests_session, r).json()

    def unregister_extension(self, extension_name):
        """
        Unregisters the specified extension from ags
        """
        r = requests.Request("POST", "{0}/services/types/extensions/unregister".format(self._server_url_base))
        r.data = {"extensionFilename": extension_name}
        return send_session_request(self._requests_session, r).json()

    def register_extension(self, itemID):
        """
        Registers the specified extension with ags
        """
        r = requests.Request("POST", "{0}/services/types/extensions/register".format(self._server_url_base))
        r.data = {"id": itemID}
        return send_session_request(self._requests_session, r).json()