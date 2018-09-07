from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ..._endpoint_base import EndpointBase
from ..._utils import send_session_request
from .ServiceType import ServiceType
from ._service_factory import _create_service_from_json

class _FolderMixin(EndpointBase):

    ####################
    ## PUBLIC METHODS ##
    ####################

    def list_services(self):
        """
        Gets a list of machine proxy objects for machines registered on the server.
        """
        response = self._get()

        services = []
        for s in response["services"]:
            services.append(_create_service_from_json(s, self._session, self._url_base, s["folderName"]))

        return services