from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from .._endpoint_base import _EndpointBase
from .._utils import send_session_request

from enum import Enum

class Directory(_EndpointBase):

    class DirectoryType(Enum):
        OUTPUT = "OUTPUT"
        CACHE = "CACHE"
        INDEX = "INDEX"
        INPUT = "INPUT"
        JOB_REGISTRY = "JOBREGISTRY"
        JOBS = "JOBS"
        UPLOADS = "UPLOADS"
        KML = "KML"
        SYSTEM = "SYSTEM"

    class CleanupMode(Enum):
        NONE = "NONE"
        TIME_ELAPSED_SINCE_LAST_MODIFIED = "TIME_ELAPSED_SINCE_LAST_MODIFIED"

    def __init__(self, requests_session, parent_url):
        super().__init__(requests_session, parent_url)
        self._pdata = {}

    @property
    def cleanup_mode(self):
        return self.CleanupMode(self._pdata["cleanup_mode"])

    @cleanup_mode.setter
    def cleanup_mode(self, value):
        self._pdata["cleanup_mode"] = CleanupMode(value).value

    @property
    def description(self):
        return self._pdata["description"]

    @description.setter
    def description(self, value):
        self._pdata["description"] = value

    @property
    def directory_type(self):
        return self.DirectoryType(self._pdata["directory_type"])

    @property
    def local_directory_path(self):
        return self._pdata["local_directory_path"]

    @local_directory_path.setter
    def local_directory_path(self, value):
        if self.use_local_directory == False:
            raise Exception("Cannot edit local directory path when 'use_local_directory' is false.")
        self._pdata["local_directory_path"] = value

    @property
    def max_file_age(self):
        return self._pdata["max_file_age"]

    @max_file_age.setter
    def max_file_age(self, value):
        self._pdata["max_file_age"] = value

    @property
    def name(self):
        return self._pdata["name"]

    @property
    def physical_path(self):
        return self._pdata["physical_path"]

    @physical_path.setter
    def physical_path(self, value):
        self._pdata["physical_path"] = value

    @property
    def use_local_directory(self):
        return self._pdata["use_local_directory"]

    @property
    def virtual_path(self):
        return self._pdata["virtual_path"]

    @property
    def _url_full(self):
        return "{0}/system/directories/{1}".format(self._url_base, self.name)

    def clean(self):
        send_session_request(
            self._session,
            self._create_operation_request(
                self,
                operation = "clean",
                method = "POST")
        )
    
    def unregister(self):
        send_session_request(
            self._session,
            self._create_operation_request(
                self,
                operation = "unregister",
                method = "POST")
        )

    def update(self):
        invalid_to_update = [
            self.DirectoryType.UPLOADS,
            self.DirectoryType.KML,
            self.DirectoryType.INDEX,
            self.DirectoryType.JOB_REGISTRY,
            self.DirectoryType.INPUT
        ]

        if self.directory_type in invalid_to_update:
            raise Exception("Directory type '{0}' cannot be edited/updated.".format(self.directory_type.value))

        send_session_request(
            self._session, 
            self._create_operation_request(
                self,
                operation = "edit",
                method = "POST",
                data = {
                    # name and directory type are required, even though name is in the URL and the documentation makes no
                    # mention of including either of them
                    "name": self.name,
                    "directoryType": self.directory_type.value,
                    "physicalPath": self.physical_path,
                    "cleanupMode": self.cleanup_mode.value,
                    "maxFileAge": self.max_file_age,
                    "description": self.description
                }
            )
        )
    
    @staticmethod
    def _create_from_json(dir_json, session, url_base):
        new_dir = Directory(session, url_base)

        new_dir._pdata["name"] = dir_json["name"]
        new_dir._pdata["physical_path"] = dir_json["physicalPath"]
        new_dir._pdata["directory_type"] = dir_json["directoryType"]
        new_dir._pdata["cleanup_mode"] = dir_json["cleanupMode"]
        new_dir._pdata["max_file_age"] = dir_json["maxFileAge"]
        new_dir._pdata["description"] = dir_json["description"]
        new_dir._pdata["use_local_directory"] = dir_json["useLocalDir"]
        new_dir._pdata["local_directory_path"] = dir_json["localDirectoryPath"]
        new_dir._pdata["virtual_path"] = dir_json["virtualPath"]

        return new_dir