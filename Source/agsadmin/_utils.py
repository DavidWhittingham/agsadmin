import requests

JSON_DECODE_ERROR = "Unknown server response, error parsing server response as JSON."

def get_public_key(public_key_url):
    """
    Gets the ArcGIS Server REST Admin API public key, given the page address.

    :param public_key_url: The URL to the public key service page (usually http://servername:port/instance_name/admin/publicKey)
    :type public_key_url: str

    :returns: A dictionary with the public key (dictionary key "publicKey") and the modulus (dictionary key "modulus")
    :rtype: Dict
    """

    r = requests.get(public_key_url, params = {"f": "json"}).json()
    r["publicKey"] = long(r["publicKey"], 16)
    r["modulus"] = long(r["modulus"], 16)
    return r

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
    :type key: int

    :param modulus: The ArcGIS Server REST Admin API RSA modulus
    :type modulus: long

    :returns: A new copy of the dictionary with all values encrypted using the public key and the RSA PKCS v1.5
        algorithm.
    :rtype: Dict
    """

    # get crypto module, then encode
    try:
        from rsa import PublicKey, encrypt
        rpk = PublicKey(modulus, key)
        new_data = {key: encrypt(value, rpk).encode('hex') for key, value in data_dict.iteritems()}
    except ImportError:
        from Crypto.PublicKey import RSA
        from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5
        cipher = PKCS1_v1_5.new(RSA.construct((modulus, key)))
        new_data = {key: cipher.encrypt(value).encode('hex') for key, value in data_dict.iteritems()}

    return new_data

def create_operation_request(base_url, service_name, service_type, operation = None, folder_name = None,
                             method = "POST"):
    """
    Creates an operation request against a given ArcGIS Server Service.

    :param base_url: The base URL of the ArcGIS Server Admin API (usually 'http://serverName:port/instance_name/admin')
    :type base_url: str

    :param service_name: The name of the service to perform an operation on.
    :type service_name: str

    :param service_type: The type of the service named in the "service_name" property.
    :type service_type: str

    :param operation: The operation to perform.  If None, no operation is sent and the basic service metadata is
        returned.
    :type operation: str

    :param folder_name: If the service is not at the root level, specify the folder it resides in.
    :type folder_name: str

    :param method: Overrides the HTTP verb to use on the request, default is POST but some operations accept/require GET
    :type method: str
    """

    url = "{base}/services/{service}.{type}/{operation}" \
        if folder_name == None or len(folder_name.strip()) == 0 \
        else "{base}/services/{folder}/{service}.{type}/{operation}"
    url = url.format(
        base = base_url,
        service = service_name,
        type = service_type,
        operation = operation if not operation == None else "",
        folder = folder_name)
    return requests.Request(method, url)

def send_session_request(session, request, ags_operation = True):
    """
    For whatever reason, the requests library doesn't use pre-configured authentication or paramater information on a
    session object when you use session.send(), so this function takes a session and request object, and uses
    session.request() to perform the HTTP request, using the information in the request object.

    :param session: The pre-configured session object to use when making the request
    :type session: requests.session
    """

    hooks = {}

    if ags_operation:
        hooks["response"] = decode_ags_operation

    r = session.request(request.method, request.url, data = request.data, params = request.params, hooks = hooks)

    r.raise_for_status()
    return r

def decode_ags_operation(response, **kwargs):
    """
    Because Esri don't know how to write a REST service correctly (i.e. one that uses HTTP error codes in the response
    headers), we have to untangle responses to ensure the correct HTTP errors are raised.
    """

    try:
        j = response.json()

        if "code" in j:
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