# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property, PropertyDefinition
from . import FHIRBase, Element, Extension


from ._instant import instant
from ._uri import uri
from ._id import id

from .coding import Coding

__author__ = "Melle Sieswerda"
__copyright__  = "Copyright 2017, Melle Sieswerda"
__license__ = "GPL"
__version__ = "0.8"

__all__ = ['Meta']


# ------------------------------------------------------------------------------
# Meta
# ------------------------------------------------------------------------------
class Meta(Element):
    """
    The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content may not
    always be associated with version changes to the resource.
    
    Autogenerated class.
    """
    _url = 'http://hl7.org/fhir/StructureDefinition/Meta'
    
    versionId = Property(PropertyDefinition('versionId', id, '0', '1'))
    lastUpdated = Property(PropertyDefinition('lastUpdated', instant, '0', '1'))
    profile = Property(PropertyDefinition('profile', uri, '0', '*'))
    security = Property(PropertyDefinition('security', Coding, '0', '*'))
    tag = Property(PropertyDefinition('tag', Coding, '0', '*'))
    