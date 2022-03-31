from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

import requests
import unicodedata

from binascii import b2a_hex
from future.utils import iteritems
from past.builtins import basestring
from rsa import PublicKey, encrypt

JSON_DECODE_ERROR = "Unknown server response, error parsing server response as JSON."


def caseless_equal(left, right):
    return normalize_caseless(left) == normalize_caseless(right)


def decode_ags_operation(response, **kwargs):
    """
    Because Esri don't know how to write a REST service correctly (i.e. one that uses HTTP error codes in the response
    headers), we have to untangle responses to ensure the correct HTTP errors are raised.
    """

    try:
        j = response.json()

        # fuzzy check for Portal vs ArcGIS Server
        error_dict = j.get("error", {})
        if error_dict.get("code"):
            # probably from Portal
            error_code = error_dict["code"]
            if 400 <= error_code < 600:
                response.status_code = error_code
                response.reason = error_dict.get("message", "")
        elif "code" in j:
            # probably from ArcGIS Server
            if 400 <= j["code"] < 600:
                response.status_code = j["code"]
                response.reason = " | ".join(j["messages"])
    except ValueError:
        # we've seen instances where ArcGIS Server returns an XML response for errors.
        # we aren't going to parse these, we simply assume the server has lost its mind and return HTTP/500
        # if Esri fixed their JSON responses so they actually return the correct HTTP code, this wouldn't be an issue
        response.status_code = 500
        response.reason = JSON_DECODE_ERROR

    return response


def encrypt_request_data(data_dict, key, modulus):
    """
    Encrypts request data using the ArcGIS Server REST Admin API Public Key from an ArcGIS Server instance.
    According to Esri's documentation, the public key should be retrieved every time a request is sent, as it may
    change. This is also backed by Esri's own software, which follows this practice and doesn't cache the key.  As
    such, each request to this function should ensure it is providing an up-to-date key/modulus pair.

    :param data_dict: The data to be encrypted. The data will not be modified, instead a new dictionary with the
        encrypted data will be returned.
    :type data_dict: Dict

    :param key: The ArcGIS Server REST Admin API RSA public key
    :type key: Integer

    :param modulus: The ArcGIS Server REST Admin API RSA modulus
    :type modulus: Integer

    :returns: A new copy of the dictionary with all values encrypted using the public key and the RSA PKCS v1.5
        algorithm.
    :rtype: Dict
    """

    rpk = PublicKey(modulus, key)
    return {key: b2a_hex(encrypt(bytes(value, "utf-8"), rpk)) for key, value in iteritems(data_dict)}


def get_instance_url_base(protocol, hostname, port, instance):
    if instance:
        return "{0}://{1}{2}/{3}".format(protocol, hostname, "" if port in (80, 443) else ":%s" % port, instance)
    else:
        return "{0}://{1}{2}".format(protocol, hostname, "" if port in (80, 443) else ":%s" % port)


def get_public_key(public_key_url):
    """
    Gets the ArcGIS Server REST Admin API public key, given the page address.

    :param public_key_url: The URL to the public key service page (usually http://servername:port/instance_name/admin/publicKey)
    :type public_key_url: str

    :returns: A dictionary with the public key (dictionary key "publicKey") and the modulus (dictionary key "modulus")
    :rtype: Dict
    """

    r = requests.get(public_key_url, params={"f": "json"}).json()
    r["publicKey"] = int(r["publicKey"], 16)
    r["modulus"] = int(r["modulus"], 16)
    return r


def normalize_caseless(text):
    if hasattr(text, "casefold"):
        # use casefold on Py3 to normalize correctly
        return unicodedata.normalize("NFKD", text.casefold())

    # Python 2 or other weird non-casefoldable string, just use upper/lower as fallback
    return text.upper().lower()


def truthy(value, nullable=False):
    """Gets a boolean value based on truthiness, explictly evaluating string content.

    Args:
        value (any): The truthy value to evaluate
    """

    if nullable and value is None:
        return None

    if isinstance(value, basestring):
        if caseless_equal(value, "true"):
            return True
        elif nullable and value.strip() == "":
            return None
        else:
            return False

    return bool(value)


def send_session_request(session, request, ags_operation=True):
    """
    For whatever reason, the requests library doesn't use pre-configured authentication or paramater information on a
    session object when you use session.send(), so this function takes a session and request object, and uses
    session.request() to perform the HTTP request, using the information in the request object.

    :param session: The pre-configured session object to use when making the request
    :type session: requests.session
    """

    if ags_operation:
        if "response" in request.hooks:
            request.hooks["response"].append(decode_ags_operation)
        else:
            request.hooks["response"] = [decode_ags_operation]

    prepped = session.prepare_request(request)

    # merge in environment variables, to pick up proxies
    settings = session.merge_environment_settings(request.url, {}, None, None, None)

    r = session.send(prepped, **settings)

    r.raise_for_status()
    return r
