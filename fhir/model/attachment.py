# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property, PropertyDefinition
from . import FHIRBase, Element, Extension


from ._base64binary import base64Binary
from ._string import string
from ._code import code
from ._uri import uri
from ._datetime import dateTime
from ._unsignedint import unsignedInt


__author__ = "Melle Sieswerda"
__copyright__  = "Copyright 2017, Melle Sieswerda"
__license__ = "GPL"
__version__ = "0.8"

__all__ = ['Attachment']


# ------------------------------------------------------------------------------
# Attachment
# ------------------------------------------------------------------------------
class Attachment(Element):
    """
    For referring to data content defined in other formats.
    
    Autogenerated class.
    """
    _url = 'http://hl7.org/fhir/StructureDefinition/Attachment'
    
    contentType = Property(PropertyDefinition('contentType', code, '0', '1'))
    language = Property(PropertyDefinition('language', code, '0', '1'))
    data = Property(PropertyDefinition('data', base64Binary, '0', '1'))
    url = Property(PropertyDefinition('url', uri, '0', '1'))
    size = Property(PropertyDefinition('size', unsignedInt, '0', '1'))
    hash = Property(PropertyDefinition('hash', base64Binary, '0', '1'))
    title = Property(PropertyDefinition('title', string, '0', '1'))
    creation = Property(PropertyDefinition('creation', dateTime, '0', '1'))
    