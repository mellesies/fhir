# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property, PropertyDefinition
from . import FHIRBase, Element, Extension

from .backboneelement import BackboneElement
from .domainresource import DomainResource

from ._code import code
from ._string import string
from ._datetime import dateTime

from .period import Period
from .codeableconcept import CodeableConcept
from .reference import Reference
from .backboneelement import BackboneElement
from .narrative import Narrative
from .identifier import Identifier

__author__ = "Melle Sieswerda"
__copyright__  = "Copyright 2017, Melle Sieswerda"
__license__ = "GPL"
__version__ = "0.8"

__all__ = ['Composition']


class Attester(BackboneElement):
    """Autogenerated class for implicit type."""
    mode = Property(PropertyDefinition('mode', 'code', '1', '*'))    
    time = Property(PropertyDefinition('time', 'dateTime', '0', '1'))    
    party = Property(PropertyDefinition('party', ['Reference(reference="http://hl7.org/fhir/StructureDefinition/Patient")', 'Reference(reference="http://hl7.org/fhir/StructureDefinition/Practitioner")', 'Reference(reference="http://hl7.org/fhir/StructureDefinition/Organization")'], '0', '1'))    

class Event(BackboneElement):
    """Autogenerated class for implicit type."""
    code = Property(PropertyDefinition('code', 'CodeableConcept', '0', '*'))    
    period = Property(PropertyDefinition('period', 'Period', '0', '1'))    
    detail = Property(PropertyDefinition('detail', 'Reference(reference="http://hl7.org/fhir/StructureDefinition/Resource")', '0', '*'))    

class Section(BackboneElement):
    """Autogenerated class for implicit type."""
    title = Property(PropertyDefinition('title', 'string', '0', '1'))    
    code = Property(PropertyDefinition('code', 'CodeableConcept', '0', '1'))    
    text = Property(PropertyDefinition('text', 'Narrative', '0', '1'))    
    mode = Property(PropertyDefinition('mode', 'code', '0', '1'))    
    orderedBy = Property(PropertyDefinition('orderedBy', 'CodeableConcept', '0', '1'))    
    entry = Property(PropertyDefinition('entry', 'Reference(reference="http://hl7.org/fhir/StructureDefinition/Resource")', '0', '*'))    
    emptyReason = Property(PropertyDefinition('emptyReason', 'CodeableConcept', '0', '1'))    
    section = Property(PropertyDefinition('section', 'Section', '0', '*'))    

# ------------------------------------------------------------------------------
# Composition
# ------------------------------------------------------------------------------
class Composition(DomainResource):
    """
    A set of healthcare-related information that is assembled together
    into a single logical document that provides a single coherent
    statement of meaning, establishes its own context and that has
    clinical attestation with regard to who is making the statement. While
    a Composition defines the structure, it does not actually contain the
    content: rather the full content of a document is contained in a
    Bundle, of which the Composition is the first resource contained.
    
    Autogenerated class.
    """
    _url = 'http://hl7.org/fhir/StructureDefinition/Composition'
    
    identifier = Property(PropertyDefinition('identifier', Identifier, '0', '1'))
    date = Property(PropertyDefinition('date', dateTime, '1', '1'))
    type = Property(PropertyDefinition('type', CodeableConcept, '1', '1'))
    class_ = Property(PropertyDefinition('class_', CodeableConcept, '0', '1'))
    title = Property(PropertyDefinition('title', string, '1', '1'))
    status = Property(PropertyDefinition('status', code, '1', '1'))
    confidentiality = Property(PropertyDefinition('confidentiality', code, '0', '1'))
    subject = Property(PropertyDefinition('subject', Reference(reference="http://hl7.org/fhir/StructureDefinition/Resource"), '1', '1'))
    author = Property(PropertyDefinition('author', ['Reference(reference="http://hl7.org/fhir/StructureDefinition/Practitioner")', 'Reference(reference="http://hl7.org/fhir/StructureDefinition/Device")', 'Reference(reference="http://hl7.org/fhir/StructureDefinition/Patient")', 'Reference(reference="http://hl7.org/fhir/StructureDefinition/RelatedPerson")'], '1', '*'))
    attester = Property(PropertyDefinition('attester', Attester, '0', '*'))
    custodian = Property(PropertyDefinition('custodian', Reference(reference="http://hl7.org/fhir/StructureDefinition/Organization"), '0', '1'))
    event = Property(PropertyDefinition('event', Event, '0', '*'))
    encounter = Property(PropertyDefinition('encounter', Reference(reference="http://hl7.org/fhir/StructureDefinition/Encounter"), '0', '1'))
    section = Property(PropertyDefinition('section', Section, '0', '*'))
    