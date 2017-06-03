# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property, PropertyDefinition, BaseType, dateTimeBase

__all__ = ['xhtml', ]

class xhtml(BaseType):
    """Autogenerated xhtml type."""
    
    value = Property(PropertyDefinition('value', str, '1', '1', 'xmlAttr'))
    
    def __init__(self, value=None):
        """Initialize a new xhtml instance."""
        if value is not None:
            value = str(value)

        super(xhtml, self).__init__(value)
    
    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if self.value is None or other is None:
            return self.value is None and other is None
        if isinstance(other, xhtml):
            return self.value.__eq__(other.value)
        elif isinstance(other, str):
            return self.value.__eq__(other)
        
        return self.value.__eq__(other)
        
    def __ne__(self, other):
        if self.value is None or other is None:
            return not (self.value is None and other is None)
        if isinstance(other, xhtml):
            return self.value.__ne__(other.value)
        elif isinstance(other, str):
            return self.value.__ne__(other)
        
        return self.value.__ne__(other)
        
    def __lt__(self, other):
        if isinstance(other, xhtml):
            return self.value.__lt__(other.value)
        elif isinstance(other, str):
            return self.value.__lt__(other)
        
        return self.value.__lt__(other)
        
    def __le__(self, other):
        if isinstance(other, xhtml):
            return self.value.__le__(other.value)
        elif isinstance(other, str):
            return self.value.__le__(other)
        
        return self.value.__le__(other)
        
    def __gt__(self, other):
        if isinstance(other, xhtml):
            return self.value.__gt__(other.value)
        elif isinstance(other, str):
            return self.value.__gt__(other)
        
        return self.value.__gt__(other)
        
    def __ge__(self, other):
        if isinstance(other, xhtml):
            return self.value.__ge__(other.value)
        elif isinstance(other, str):
            return self.value.__ge__(other)
        
        return self.value.__ge__(other)
        
    def __add__(self, other):
        if isinstance(other, xhtml):
            return xhtml(self.value.__add__(other.value))
        elif isinstance(other, str):
            return self.value.__add__(other)
        
        return self.value.__add__(other)
        
    __radd__ = __add__
    
    
    def __mul__(self, other):
        """x * y <==> x.__mul__(y)"""
        return xhtml(str(self).__mul__(other))

    def __rmul__(self, other):
        """y * x <==> x.__rmul__(y)"""
        return xhtml(str(self).__mul__(other))



