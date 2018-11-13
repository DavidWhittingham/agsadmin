from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from .UserContentBase import UserContentBase

class UserFolderContent(UserContentBase):

    def __init__(self, requests_session, url_base, username, folder_id):
        super().__init__(requests_session, url_base, username)

        self._pdata["folderId"] = folder_id

    @property
    def _url_full(self):
        return "{0}/{1}".format(self._url_base, self.folder_id)

    @property
    def folder_id(self):
        return self._pdata["folderId"]