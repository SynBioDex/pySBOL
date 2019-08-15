from sbol3.identified import Identified
from sbol3.constants import *
from sbol3.property import LiteralProperty, URIProperty
from rdflib import URIRef


class Measurement(Identified):
    """The purpose of the Measure class is to link a numerical value to a unit of measure."""

    def __init__(self, uri=URIRef('example'), value=0.0, unit='', version=VERSION_STRING):
        super().__init__(SBOL_MEASURE, uri, version)
        self.value = LiteralProperty(self, SBOL_VALUE, '1', '1', [], value)
        self.unit = URIProperty(self, SBOL_UNIT, '1', '1', [], unit)
        self.types = URIProperty(self, SBOL_TYPES, '0', '*', [])
