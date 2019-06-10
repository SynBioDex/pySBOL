from identified import Identified
from constants import *
from property import OwnedObject


class Module(Identified):
    def __init__(self, rdf_type=SBOL_MODULE, uri='example', definition='', version=VERSION_STRING):
        super().__init__(rdf_type, uri, version)
        self.definition = None  # TODO ReferencedObject
        self.mapsTos = OwnedObject(self, SBOL_MAPS_TOS, '0', '*', [])
