from ._mapserver import _MapServer
from ._gpserver import _GpServer
from ._imageserver import _ImageServer
from ._geocodeserver import _GeocodeServer

_type_map = {
    "mapserver": _MapServer,
    "gpserver": _GpServer,
    "imageserver": _ImageServer,
    "geocodeserver": _GeocodeServer
}

def _get_service_class(type):
    type = type.lower()
    if type.lower() in _type_map:
        return _type_map[type]
    return None