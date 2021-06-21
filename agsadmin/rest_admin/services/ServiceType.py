from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from enum import Enum


class ServiceType(Enum):
    FEATURE_SERVER = "FeatureServer"
    MAP_SERVER = "MapServer"
    GP_SERVER = "GPServer"
    IMAGE_SERVER = "ImageServer"
    GEOCODE_SERVER = "GeocodeServer"
    GEO_DATA_SERVER = "GeoDataServer"
    GEOMETRY_SERVER = "GeometryServer"
    GLOBE_SERVER = "GlobeServer"
    SEARCH_SERVER = "SearchServer"
    VECTOR_TILE_SERVER = "VectorTileServer"

    @staticmethod
    def _get_proxy(service_type):
        from .FeatureServer import FeatureServer
        from .MapServer import MapServer
        from .GpServer import GpServer
        from .ImageServer import ImageServer
        from .GeocodeServer import GeocodeServer
        from .GeoDataServer import GeoDataServer
        from .GeometryServer import GeometryServer
        from .GlobeServer import GlobeServer
        from .SearchServer import SearchServer
        from .VectorTileServer import VectorTileServer

        _type_map = {
            ServiceType.FEATURE_SERVER: FeatureServer,
            ServiceType.MAP_SERVER: MapServer,
            ServiceType.GP_SERVER: GpServer,
            ServiceType.IMAGE_SERVER: ImageServer,
            ServiceType.GEOCODE_SERVER: GeocodeServer,
            ServiceType.GEO_DATA_SERVER: GeoDataServer,
            ServiceType.GEOMETRY_SERVER: GeometryServer,
            ServiceType.GLOBE_SERVER: GlobeServer,
            ServiceType.SEARCH_SERVER: SearchServer,
            ServiceType.VECTOR_TILE_SERVER: VectorTileServer
        }

        service_type = ServiceType(service_type)

        return _type_map[service_type]