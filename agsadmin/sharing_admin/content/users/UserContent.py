from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ...._utils import send_session_request
from .UserContentBase import UserContentBase
from .UserFolderContent import UserFolderContent

class UserContent(UserContentBase):

    def __init__(self, requests_session, url_base, username):
        super().__init__(requests_session, url_base, username)

    def list_folders(self):
        """
        Gets a list of item details.
        """

        return self._get()["folders"]

    def create_folder(self, folder_name):
        r = self._create_operation_request(self, "createFolder", method = "POST", data = {"title": folder_name})

        return send_session_request(self._session, r).json()

    def get_folder(self, folder_id):
        return UserFolderContent(self._session, self._url_full, self.username, folder_id)