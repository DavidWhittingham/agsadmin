from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from .ags_admin_error import AgsAdminError

class AuthenticationError(AgsAdminError):
    """Error for representing authentication faults with ArcGIS servers."""

    DEFAULT_ERROR_MESSAGE = "Could not authenticate with the ArcGIS server."

    def __init__(self, *args):
        if len(args) == 0:
            super().__init__(self.DEFAULT_ERROR_MESSAGE)
        else:
            super().__init__(*args)