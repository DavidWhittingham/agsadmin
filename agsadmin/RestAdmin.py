from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from datetime import datetime
from dateutil import tz

from .rest_admin.machines import Machines
from .rest_admin.system import System
from .rest_admin.services import Services
from .rest_admin.uploads import Uploads
from ._admin_base import AdminBase

class RestAdmin(AdminBase):
    """
    Provides a proxy object for an ArcGIS Server instance, communicating with the REST Admin API.
    """

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

    @property
    def _url_full(self):
        """
        Returns the full URL for this endpoint.
        """
        return self._url_base + "/admin"

    def __init__(self,
                 hostname,
                 username,
                 password,
                 instance_name="arcgis",
                 port=6080,
                 use_ssl=False,
                 utc_delta=tz.tzlocal().utcoffset(datetime.now()),
                 proxy=None,
                 encrypt=True,
                 verify=True):
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

        :param proxy: An addess of a proxy server to use for interacting with ArcGIS Server, if required.
        :type proxy: str

        :param encrypt: Is set to True (default), uses public key crypto to encrypt communication with the ArcGIS
        Server instance.  Setting this to False disables public key crypto.  When communicating over SSL, this
        parameter is ignored, as SSL will already encrypt the traffic.
        :type encrypt: bool

        :param verify: Is set to True (default), which causes SSL certificates to be verified.  Can be set to false
        to disable verification, or set to the path of a CA_BUNDLE file, or to a directory with certifcates of a
        trusted certificate authority, to use for validating certificates.
        :type encrypt: bool or str
        """

        super().__init__(hostname, username, password, instance_name, port, use_ssl, utc_delta, proxy, encrypt, verify)

        # setup sub-modules/classes
        self._system = System(self._session, self.url)
        self._machines = Machines(self._session, self.url)
        self._services = Services(self._session, self.url)
        self._uploads = Uploads(self._session, self.url)
