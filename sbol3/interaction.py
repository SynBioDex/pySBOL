from .identified import Identified
from .property import OwnedObject, URIProperty
from .validation import *
from .constants import *


class Interaction(Identified):
    def __init__(self, rdf_type=SBOL_INTERACTION, uri='example', interaction_type=SBO_INTERACTION):
        super().__init__(rdf_type, uri)
        self.functionalComponents = OwnedObject(self, SBOL_FUNCTIONAL_COMPONENTS, '0', '*', [libsbol_rule_18])
        self._types = URIProperty(self, SBOL_TYPES, '1', '*', [], interaction_type)
        self.participations = OwnedObject(self, SBOL_PARTICIPATIONS, '0', '*', [])
        self.measurements = OwnedObject(self, SBOL_MEASUREMENTS, '0', '*', [])
        # TODO hidden properties

    @property
    def types(self):
        return self._types.value

    @types.setter
    def types(self, new_types):
        self._types.set(new_types)
