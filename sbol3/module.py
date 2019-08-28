from .identified import Identified
from .constants import *
from .property import OwnedObject, ReferencedObject


class Module(Identified):
    def __init__(self, rdf_type=SBOL_MODULE, uri='example', definition='', version=VERSION_STRING):
        super().__init__(rdf_type, uri, version)
        self.definition = ReferencedObject(self, SBOL_DEFINITION, SBOL_MODULE_DEFINITION, '1', '1', [], definition)
        self.mapsTos = OwnedObject(self, SBOL_MAPS_TOS, '0', '*', [])
        self.measurements = OwnedObject(self, SBOL_MEASUREMENTS, '0', '*', [])
