from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

import abc

from os import environ

from requests import Request, Session

from ._auth import _RestAdminAuth
from ._endpoint_base import EndpointBase
from ._utils import get_instance_url_base, send_session_request

class AdminBase(EndpointBase):
    """
    Base class for all ArcGIS Server interactive endpoints.  Contains abstract items for dealing with service
    communication.
    """

    __metaclass__ = abc.ABCMeta

    @property
    def url(self):
        return self._url_full

    @property
    def instance_url(self):
        return self._url_base

    @property
    def username(self):
        return self._pdata["username"]

    def __init__(self,
                 hostname,
                 username,
                 password,
                 instance_name,
                 port,
                 use_ssl,
                 utc_delta,
                 proxy,
                 encrypt,
                 verify=True):
        """
        :param hostname: The hostname (or fully qualified domain name) of the ArcGIS Server.
        :type hostname: str

        :param username: The username used to log on as an administrative user to the ArcGIS Server.
        :type username: str

        :param password: The password for the administrative account used to login to the ArcGIS Server.
        :type password: str

        :param instance_name: The name of the ArcGIS Server instance.
        :type instance_name: str

        :param port: The port that the ArcGIS Server is operating on. If communication directly with an ArcGIS Server
        instance, you can ignore this setting and use the default.  If accesssing the ArcGIS Server REST Admin API
        through the ArcGIS Web Adaptor, enter the port the service is running on here.

        :param use_ssl: If True, instructs the REST Admin proxy to communicate with the ArcGIS Server REST Admin API
        via SSL/TLS.
        :type use_ssl: bool

        :param utc_delta: The time difference between UTC and the ArcGIS Server instance.  This is used to calculate
        when the admin token has expired, as Esri foolishly return this value as local server time, making calculation
        of its expiry impossible unless you know what time zone the server is also in.
        :type utc_delta: datetime.timedelta

        :param proxy: An addess of a proxy server to use for interacting with ArcGIS Server, if required.
        :type proxy: str

        :param encrypt: If set to True, uses public key crypto to encrypt communication with the ArcGIS
        Server instance.  Setting this to False disables public key crypto.  When communicating over SSL, this
        parameter is ignored, as SSL will already encrypt the traffic.
        :type encrypt: bool

        :param verify: Is set to True (default), which causes SSL certificates to be verified.  Can be set to false
        to disable verification, or set to the path of a CA_BUNDLE file, or to a directory with certifcates of a
        trusted certificate authority, to use for validating certificates.
        :type encrypt: bool or str
        """

        self._pdata = {
            "username": username
        }

        protocol = "https" if use_ssl else "http"

        # setup the requests session
        proxies = { protocol: proxy } if proxy else {}
        s = Session()
        s.verify = verify
        s.params = { "f": "json" }
        s.proxies = proxies

        # call super constructor with session and instance URL
        super().__init__(s, get_instance_url_base(protocol, hostname, port, instance_name))

        # Resolve the generate token endpoint from /arcgis/rest/info
        generate_token_url = None
        ags_info = self.get_server_info()

        if "authInfo" in ags_info and "isTokenBasedSecurity" in ags_info["authInfo"]:
            # token auth in use, setup auto-auth on requests on the session
            generate_token_url = ags_info["authInfo"]["tokenServicesUrl"]

            self._session.auth = _RestAdminAuth(
                username,
                password,
                generate_token_url,
                utc_delta=utc_delta,
                get_public_key_url=None if encrypt == False or use_ssl == True else self._url_full + "/publicKey",
                proxies=proxies,
                client="referer" if "/sharing" in generate_token_url else "requestip",
                referer=self._url_full if "/sharing" in generate_token_url else None,
                verify=verify
            )

    def get_server_info(self):
        return send_session_request(
            self._session,
            Request(
                "GET",
                "{0}/rest/info".format(self._url_base)
            ),
            True
        ).json()