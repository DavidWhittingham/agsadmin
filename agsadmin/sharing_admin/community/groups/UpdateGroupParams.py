from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

# standard lib imports
from enum import Enum

# local imports
from ..._params_mixins.ClearEmptyFieldsMixin import ClearEmptyFieldsMixin
from .CreateGroupParams import CreateGroupParams


class UpdateGroupParams(ClearEmptyFieldsMixin, CreateGroupParams):
    """Holds parameter values for the "update" group function."""
    pass

   