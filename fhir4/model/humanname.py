# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property
from . import FHIRBase, Element, Extension, Reference


from ._code import code
from ._string import string

from .period import Period

__author__ = "Melle Sieswerda"
__copyright__  = "Copyright 2017, Melle Sieswerda"
__license__ = "GPL"
__version__ = "0.8"

__all__ = ['HumanName']


# ------------------------------------------------------------------------------
# HumanName
# ------------------------------------------------------------------------------
class HumanName(Element):
    """
    A human's name with the ability to identify parts and usage.
    
    Autogenerated class.
    """
    _url = 'http://hl7.org/fhir/StructureDefinition/HumanName'
    
    use = Property('use', code, '0', '1')
    text = Property('text', string, '0', '1')
    family = Property('family', string, '0', '1')
    given = Property('given', string, '0', '*')
    prefix = Property('prefix', string, '0', '*')
    suffix = Property('suffix', string, '0', '*')
    period = Property('period', Period, '0', '1')