from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

import requests
from datetime import datetime, timedelta
from urlparse import urlparse, urlunparse, parse_qs
from urllib import urlencode
from ._utils import get_public_key, encrypt_request_data


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

    def __init__(self,
                 username,
                 password,
                 get_token_url,
                 utc_delta=timedelta(),
                 expiration_minutes=15,
                 get_public_key_url=None,
                 proxies=None,
                 client=None,
                 referer=None):
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

    def __call__(self, r):
        # modify and return the request
        url_parts = urlparse(r.url)
        qs_args = parse_qs(url_parts[4])
        qs_args.update({"token": self._GetToken()})
        new_qs = urlencode(qs_args, True)

        r.url = urlunparse(
            list(url_parts[0:4]) + [new_qs] + list(url_parts[5:]))
        return r

    def _GetToken(self):
        if (self._token == None) or ((self._token["expires"] - timedelta(seconds=30)) <= (datetime.utcnow() + self._utc_delta)):
            req_data = {
                "username": self._username,
                "password": self._password,
                "expiration": str(self._expiration),
                "client":  self._client,
                "referer":  self._referer
            }

            if not self._get_public_key_url == None:
                pk = get_public_key(self._get_public_key_url)
                req_data = encrypt_request_data(
                    req_data, pk["publicKey"], pk["modulus"])
                req_data.update({
                    "encrypted": "true"
                })

            req_data.update({
                "f": "json"
            })

            tk = requests.request("POST", self._get_token_url, data=req_data, proxies=self._proxies, verify=False).json()
            tk["expires"] = datetime.fromtimestamp(int(tk["expires"]) / 1000)

            self._token = tk

        return self._token["token"]
