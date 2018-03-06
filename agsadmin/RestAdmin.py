from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from requests.exceptions import ConnectionError, HTTPError

from . import services
from .machines import Machines
from ._auth import _RestAdminAuth
from .exceptions import InvalidServiceTypeError, UnknownServiceError, CommunicationError
from ._utils import get_server_url_base, send_session_request, get_server_info_url
from .system import System
from .services import Services
from .uploads import Uploads

import requests
import os

from datetime import datetime
from dateutil import tz

class RestAdmin(object):
    """
    Provides a proxy object for an ArcGIS Server instance, communicating with the REST Admin API.
    """

    _server_url_base = None
    _server_url_rest_base = None
    _requests_session = None
    _proxies = None

    @property
    def url(self):
        return self._server_url_base

    @property
    def rest_url(self):
        return self._server_url_rest_base

    @property
    def system(self):
        return self._system

    @property
    def machines(self):
        return self._machines

    @property
    def services(self):
        return self._services

    @property
    def uploads(self):
        return self._uploads

    def __init__(self,
                 hostname,
                 username,
                 password,
                 instance_name="arcgis",
                 port=6080,
                 use_ssl=False,
                 utc_delta=tz.tzlocal().utcoffset(datetime.now()),
                 proxies=None,
                 encrypt=True):
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

        protocol = "https" if use_ssl else "http"

        # Resolve proxy from env vars
        if proxies is None and ((os.environ.get('HTTP_PROXY') or os.environ.get('HTTPS_PROXY'))):
            self._proxies = {
                'http': os.environ.get('HTTP_PROXY'),
                'https': os.environ.get('HTTPS_PROXY'),
            }
            print("Proxy enabled:", self._proxies)

        # Resolve the generate token endpoint from /arcgis/rest/info
        use_token_auth = False
        generate_token_url = None
        ags_info = self._get_rest_info(protocol, hostname, port, instance_name)

        if "authInfo" in ags_info and "isTokenBasedSecurity" in ags_info["authInfo"]:
            generate_token_url = ags_info["authInfo"]["tokenServicesUrl"]
            use_token_auth = True

        # setup the requests session
        serverBaseUrl = get_server_url_base(protocol, hostname, port, instance_name)
        self._server_url_rest_base = serverBaseUrl + "/rest/services"
        self._server_url_base = serverBaseUrl + "/admin"
        self._requests_session = requests.Session()
        self._requests_session.proxies = self._proxies
        self._requests_session.params = {"f": "json"}

        # setup token auth (if required)
        if use_token_auth:
            self._requests_session.auth = _RestAdminAuth(
                username,
                password,
                generate_token_url,
                utc_delta=utc_delta,
                get_public_key_url=self._server_url_base +
                "/publicKey" if (use_ssl == False) or (use_ssl == False and encrypt == False) else None,
                proxies=proxies,
                client="referer" if "/sharing" in generate_token_url else "requestip",
                referer=self._server_url_base if "/sharing" in generate_token_url else None
            )

        # setup sub-modules/classes
        self._system = System(self._requests_session, self._server_url_base)
        self._machines = Machines(self._requests_session, self._server_url_base)
        self._services = Services(self._requests_session, self._server_url_base)
        self._uploads = Uploads(self._requests_session, self._server_url_base)

    # Fetch the AGS rest info
    def _get_rest_info(self, protocol, hostname, port, instance_name):
        url = get_server_info_url(protocol, hostname, port, instance_name)
        r = requests.request(
            "GET",
            url,
            params={"f": "json"},
            proxies=self._proxies)

        if (not r.status_code == 200):
            print(r)
            raise Exception("Failed to get %s" % url)

        return r.json()
