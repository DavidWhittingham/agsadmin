from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.standard_library import install_aliases
install_aliases()
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

import requests
from datetime import datetime, timedelta
from future.moves.urllib.parse import urlparse, urlencode, urlunparse, parse_qs
from ._utils import get_public_key, encrypt_request_data
from .exceptions import AuthenticationError


class _RestAdminAuth(requests.auth.AuthBase):
    """Attaches ArcGIS REST Admin API Token to the given Request object."""

    _get_public_key_url = None
    _get_token_url = None
    _username = None
    _password = None
    _token = None
    _utc_delta = None
    _expiration = None
    _client = None
    _referer = None
    _ip = None

    def __init__(self,
                 username,
                 password,
                 get_token_url,
                 utc_delta=timedelta(),
                 expiration_minutes=15,
                 get_public_key_url=None,
                 proxies=None,
                 client=None,
                 referer=None,
                 ip=None,
                 verify=True):
        """Authorization agent for attching the ArcGIS Server REST Admin API Token to each request sent to an ArcGIS
        Server instance.

        :param utc_delta: Describes the time differential from UTC (plus/minus) the ArcGIS Server is.
            This is used to calculate when the server token has expired, as ArcGIS Server returns the timeout number
            in local server time, not UTC.
        :type utc_delta: str

        :param get_public_key_url: The URL to the public key service page (usually http://servername:port/instance_name/admin/publicKey)
        :type get_public_key_url: str

        :param proxies: A python dictionary of protocols (i.e. HTTP/HTTPS) as keys and proxy server addresses as values.
        :type proxies: Dict
        """

        # setup any auth-related data here
        self._get_public_key_url = get_public_key_url
        self._username = username
        self._password = password
        self._utc_delta = utc_delta
        self._get_token_url = get_token_url
        self._expiration = expiration_minutes
        self._proxies = proxies
        self._client = client
        self._referer = referer
        self._ip = ip
        self._verify = verify

    def __call__(self, r):
        # modify and return the request
        url_parts = urlparse(r.url)
        qs_args = parse_qs(url_parts[4])
        qs_args.update({"token": self._get_token()})
        new_qs = urlencode(qs_args, True)

        r.url = urlunparse(list(url_parts[0:4]) + [new_qs] + list(url_parts[5:]))
        return r

    def _get_token(self):
        if (self._token == None) or ((self._token["expires"] - timedelta(seconds=30)) <=
                                     (datetime.utcnow() + self._utc_delta)):
            req_data = {
                "username": self._username,
                "password": self._password,
                "expiration": str(self._expiration),
                "client": self._client
            }

            if (self._client == "ip"):
                req_data.update({"ip": self._ip})

            if (self._client == "referer"):
                req_data.update({"referer": self._referer})

            if not self._get_public_key_url == None:
                pk = get_public_key(self._get_public_key_url)
                req_data = encrypt_request_data(req_data, pk["publicKey"], pk["modulus"])
                req_data.update({"encrypted": "true"})

            req_data.update({"f": "json"})

            # print(req_data)

            r = requests.request("POST", self._get_token_url, data=req_data, proxies=self._proxies, verify=self._verify)

            if (not r.status_code == 200):
                raise Exception("Error getting token")

            tk = r.json()

            if ("error" in tk):
                if ("details" in tk["error"] and not tk["error"]["details"] == None and len(tk["error"]["details"]) > 0
                        and tk["error"]["details"][0] == "Invalid username or password."):
                    raise AuthenticationError("Could not authenticate with the ArcGIS server: Invalid username or password")
                else:
                    raise Exception(tk["error"])

            tk["expires"] = datetime.fromtimestamp(int(tk["expires"]) / 1000)

            self._token = tk

        return self._token["token"]
