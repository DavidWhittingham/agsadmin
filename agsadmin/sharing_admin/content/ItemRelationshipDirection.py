from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

# standard lib imports
from enum import Enum

class ItemRelationshipDirection(Enum):
    FORWARD = "forward"
    REVERSE = "reverse"