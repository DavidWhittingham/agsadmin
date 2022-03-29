from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

# standard lib imports
from enum import Enum

class ItemRelationshipType(Enum):
    MAP2SERVICE = "Map2Service"
    WMA2CODE = "WMA2Code"
    MAP2FEATURECOLLE = "Map2FeatureCollection"
    MOBILEAPP2CODE = "MobileApp2Code"
    SERVICE2DATA = "Service2Data"
    SERVICE2SERVICE = "Service2Service"
    MAP2APPCONFIG = "Map2AppConfig"
    ITEM2ATTACHMENT = "Item2Attachment"
    ITEM2REPORT = "Item2Report"
    LISTED2PROVISION = "Listed2Provisioned"
    STYLE2STYLE = "Style2Style"
    SERVICE2STYLE = "Service2Style"
    SURVEY2SERVICE = "Survey2Service"
    SURVEY2DATA = "Survey2Data"
    SERVICE2ROUTE = "Service2Route"
    AREA2PACKAGE = "Area2Package"
    MAP2AREA = "Map2Area"
    SERVICE2LAYER = "Service2Layer"
    AREA2CUSTOMPACKA = "Area2CustomPackage"
    TRACKVIEW2MAP = "TrackView2Map"
    SURVEYADDIN2DATA = "SurveyAddIn2Data"