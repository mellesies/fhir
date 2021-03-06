# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property
from . import FHIRBase, Element, Extension, Reference

from .backboneelement import BackboneElement
from .domainresource import DomainResource

from ._code import code
from ._positiveint import positiveInt

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .identifier import Identifier
from .period import Period

__author__ = "Melle Sieswerda"
__copyright__  = "Copyright 2017, Melle Sieswerda"
__license__ = "GPL"
__version__ = "0.8"

__all__ = ['EpisodeOfCare']

class StatusHistory(BackboneElement):
    """Autogenerated class for implicit type."""
    status = Property('status', 'code', '1', '1')
    period = Property('period', 'Period', '1', '1')

class Diagnosis(BackboneElement):
    """Autogenerated class for implicit type."""
    condition = Property('condition', Reference("http://hl7.org/fhir/StructureDefinition/Condition"), '1', '1')        
    role = Property('role', 'CodeableConcept', '0', '1')
    rank = Property('rank', 'positiveInt', '0', '1')


# ------------------------------------------------------------------------------
# EpisodeOfCare
# ------------------------------------------------------------------------------
class EpisodeOfCare(DomainResource):
    """
    An association between a patient and an organization / healthcare
    provider(s) during which time encounters may occur. The managing
    organization assumes a level of responsibility for the patient during
    this time.
    
    Autogenerated class.
    """
    _url = 'http://hl7.org/fhir/StructureDefinition/EpisodeOfCare'
    
    identifier = Property('identifier', Identifier, '0', '*')
    status = Property('status', code, '1', '1')
    statusHistory = Property('statusHistory', StatusHistory, '0', '*')
    type = Property('type', CodeableConcept, '0', '*')
    diagnosis = Property('diagnosis', Diagnosis, '0', '*')
    patient = Property('patient', Reference("http://hl7.org/fhir/StructureDefinition/Patient"), '1', '1')
    managingOrganization = Property('managingOrganization', Reference("http://hl7.org/fhir/StructureDefinition/Organization"), '0', '1')
    period = Property('period', Period, '0', '1')
    referralRequest = Property('referralRequest', Reference("http://hl7.org/fhir/StructureDefinition/ServiceRequest"), '0', '*')
    careManager = Property('careManager', Reference("http://hl7.org/fhir/StructureDefinition/Practitioner", "http://hl7.org/fhir/StructureDefinition/PractitionerRole"), '0', '1')
    team = Property('team', Reference("http://hl7.org/fhir/StructureDefinition/CareTeam"), '0', '*')
    account = Property('account', Reference("http://hl7.org/fhir/StructureDefinition/Account"), '0', '*')
