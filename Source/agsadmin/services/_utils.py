from ._mapserver import _MapServer
from ._gpserver import _GpServer

_type_map = {
    "mapserver": _MapServer,
    "gpserver": _GpServer
}

def _get_service_class(type):
    type = type.lower()
    if type.lower() in _type_map:
        return _type_map[type]
    return None