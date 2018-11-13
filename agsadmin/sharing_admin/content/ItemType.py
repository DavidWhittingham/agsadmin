from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from enum import Enum

class ItemType(Enum):

    ###############
    # Web Content #
    ###############

    # Maps
    WEB_MAP = "Web Map"
    CITYENGINE_WEB_SCENE = "CityEngine Web Scene"
    WEB_SCENE = "Web Scene"
    SPHERICAL_VR_EXPERIENCE = "360 VR Experience"
    PRO_MAP = "Pro Map"

    # Layers
    FEATURE_SERVICE = "Feature Service"
    MAP_SERVICE = "Map Service"
    IMAGE_SERVICE = "Image Service"
    KML = "KML"
    KML_COLLECTION = "KML Collection"
    WMS = "WMS"
    WFS = "WFS"
    WMTS = "WMTS"
    FEATURE_COLLECTION = "Feature Collection"
    FEATURE_COLLECTION_TEMPLATE = "Feature Collection Template"
    GEODATA_SERVICE = "Geodata Service"
    GLOBE_SERVICE = "Globe Service"
    VECTOR_TILE_SERVICE = "Vector Tile Service"
    SCENE_SERVICE = "Scene Service"
    RELATIONAL_DATABASE_CONNECTION = "Relational Database Connection"
    GEOMETRY_SERVICE = "Geometry Service"
    GEOCODING_SERVICE = "Geocoding Service"
    NETWORK_ANALYSIS_SERVICE = "Network Analysis Service"
    GEOPROCESSING_SERVICE = "Geoprocessing Service"
    WORKFLOW_MANAGER_SERVICE = "Workflow Manager Service"

    # Applications
    WEB_MAPPING_APPLICATION = "Web Mapping Application"
    MOBILE_APPLICATION = "Mobile Application"
    CODE_ATTACHMENT = "Code Attachment"
    OPERATIONS_DASHBOARD_ADD_IN = "Operations Dashboard Add In"
    OPERATION_VIEW = "Operation View"
    OPERATIONS_DASHBOARD_EXTENSION = "Operations Dashboard Extension"
    NATIVE_APPLICATION = "Native Application"
    NATIVE_APPLICATION_TEMPLATE = "Native Application Template"
    NATIVE_APPLICATION_INSTALLER = "Native Application Installer"
    WORKFORCE_PROJECT = "Workforce Project"
    FORM = "Form"
    INSIGHTS_WORKBOOK = "Insights Workbook"
    INSIGHTS_MODEL = "Insights Model"
    INSIGHTS_PAGE = "Insights Page"
    DASHBOARD = "Dashboard"
    HUB_INITIATIVE = "Hub Initiative"
    HUB_SITE_APPLICATION = "Hub Site Application"
    HUB_PAGE = "Hub Page"
    APP_BUILDER_EXTENSION = "App Builder Extension"

    # Data Files
    SYMBOL_SET = "Symbol Set"
    COLOR_SET = "Color Set"
    SHAPEFILE = "Shapefile"
    FILE_GEODATABASE = "File Geodatabase"
    CSV = "CSV"
    CAD_DRAWING = "CAD Drawing"
    SERVICE_DEFINITION = "Service Definition"
    DOCUMENT_LINK = "Document Link"
    MICROSOFT_WORD = "Microsoft Word"
    MICROSOFT_POWERPOINT = "Microsoft Powerpoint"
    MICROSOFT_EXCEL = "Microsoft Excel"
    PDF = "PDF"
    IMAGE = "Image"
    VISIO_DOCUMENT = "Visio Document"
    IWORK_KEYNOTE = "iWork Keynote"
    IWORK_PAGES = "iWork Pages"
    IWORK_NUMBERS = "iWork Numbers"
    REPORT_TEMPLATE = "Report Template"
    STATISTICAL_DATA_COLLECTION = "Statistical Data Collection"