from sbol3.identified import Identified
from sbol3.constants import *
from sbol3.property import LiteralProperty, URIProperty
from rdflib import URIRef


class Measurement(Identified):
    """The purpose of the Measure class is to link a numerical value to a unit of measure."""

    def __init__(self, uri=URIRef('example'), value=0.0, unit='', version=VERSION_STRING):
        super().__init__(SBOL_MEASURE, uri, version)
        self._value = LiteralProperty(self, SBOL_VALUE, '1', '1', [], value)
        self._unit = URIProperty(self, SBOL_UNIT, '1', '1', [], unit)
        self._types = URIProperty(self, SBOL_TYPES, '0', '*', [])

    @property
    def value(self):
        return self._value.value

    @value.setter
    def value(self, new_value):
        self._value.set(new_value)

    @property
    def unit(self):
        return self._unit.value

    @unit.setter
    def unit(self, new_unit):
        self._unit.set(new_unit)

    @property
    def types(self):
        return self._types.value

    @types.setter
    def types(self, new_types):
        self._types.set(new_types)

    def addType(self, new_type):
        self._types.add(new_type)

    def removeType(self, index=0):
        self._types.remove(index)
