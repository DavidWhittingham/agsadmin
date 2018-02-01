from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from .ags_admin_error import AgsAdminError

class UnknownServiceError(AgsAdminError):
    """description of class"""

    DEFAULT_ERROR_MESSAGE = "The service specified does not exist."

    def __init__(self, *args):
        if len(args) == 0:
            return super(AgsAdminError, self).__init__(self.DEFAULT_ERROR_MESSAGE)

        return super(AgsAdminError, self).__init__(*args)
