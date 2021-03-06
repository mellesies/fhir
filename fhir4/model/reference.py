# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property
from . import FHIRBase, Element, Extension, Reference


from ._string import string
from ._uri import uri

from .identifier import Identifier

__author__ = "Melle Sieswerda"
__copyright__  = "Copyright 2017, Melle Sieswerda"
__license__ = "GPL"
__version__ = "0.8"

__all__ = ['Reference']


# ------------------------------------------------------------------------------
# Reference
# ------------------------------------------------------------------------------
class Reference(Element):
    """
    A reference from one resource to another.
    
    Autogenerated class.
    """
    _url = 'http://hl7.org/fhir/StructureDefinition/Reference'
    
    reference = Property('reference', string, '0', '1')
    type = Property('type', uri, '0', '1')
    identifier = Property('identifier', Identifier, '0', '1')
    display = Property('display', string, '0', '1')
