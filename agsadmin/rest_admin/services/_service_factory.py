from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from .ServiceType import ServiceType

def _create_service_from_json(service_json, session, url_base, folder_name):
        service_enum = ServiceType(service_json["type"])
        service_name = service_json["serviceName"]

        return ServiceType._get_proxy(service_enum)(
                        session,
                        url_base,
                        service_name,
                        folder_name)