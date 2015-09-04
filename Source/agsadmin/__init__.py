"""agsadmin

Python Library used to provide conveniant access to administrative functions of ArcGIS Server 10.1.
"""

from ._version import *
from ._restadmin import RestAdmin
import agsadmin.machines as machines
import agsadmin.services as services
import agsadmin.exceptions as exceptions
