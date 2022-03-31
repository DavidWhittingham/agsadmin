from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

# standard lib imports
from enum import Enum


class PublishFileType(Enum):
    CSV = "csv"
    EXCEL = "excel"
    FEATURE_COLLECTION = "featureCollection"
    FEATURE_SERVICE = "featureService"
    FILE_GEODATABASE = "fileGeodatabase"
    GEOJSON = "geojson"
    IMAGE_COLLECTION = "imageCollection"
    MAP_SERVICE = "mapService"
    SCENE_PACKAGE = "scenepackage"
    SERVICE_DEFINITION = "serviceDefinition"
    SHAPEFILE = "shapefile"
    SQLITE_GEODATABASE = "sqliteGeodatabase"
    TILE_PACKAGE = "tilePackage"
    VECTOR_TILE_PACKAGE = "vectortilepackage"
