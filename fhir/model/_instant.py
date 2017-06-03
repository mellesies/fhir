# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property, PropertyDefinition, BaseType, dateTimeBase

__all__ = ['instant', ]

class instant(dateTimeBase):
    """Autogenerated instant type."""
    _regex = None    
    # value = Property(PropertyDefinition('value', dateTimeBase, '1', '1', 'xmlAttr'))
    value = Property(PropertyDefinition('value', str, '1', '1', 'xmlAttr'))


