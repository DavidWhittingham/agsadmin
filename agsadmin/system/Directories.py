from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from .._endpoint_base import _EndpointBase
from .._utils import send_session_request
from .Directory import Directory

class Directories(_EndpointBase):

    def __init__(self, requests_session, server_url):
        super().__init__(requests_session, server_url)

    @property
    def _url_full(self):
        return "{0}/system/directories".format(self._url_base)

    def get(self, name):
        dir_json = send_session_request(
            self._session,
            self._create_operation_request("{0}/{1}".format(self._url_full, name), method = "GET")).json()

        return Directory._create_from_json(dir_json, self._session, self._url_base)

    def list(self):
        """
        Gets a list of directory proxy objects for directories registered on the server.
        """
        response = self._get()

        directories = []
        for d in response["directories"]:
            directories.append(Directory._create_from_json(dir_json, self._session, self._url_base))

        return directories

    def register(self, name, physical_path, directory_type, description = None, cleanup_mode = Directory.CleanupMode.NONE, max_file_age = None):
        new_dir_data = {
            "name": name,
            "physicalPath": physical_path,
            "directoryType": Directory.DirectoryType(directory_type).value,
            "cleanupMode": Directory.CleanupMode(cleanup_mode).value
        }

        if description != None:
            new_dir_data["description"] = description
        
        if max_file_age != None:
            new_dir_data["maxFileAge"] = max_file_age
        
        send_session_request(
            self._session,
            self._create_operation_request(
                self,
                operation = "register",
                method = "POST",
                data = new_dir_data
            )
        )