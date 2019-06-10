from identified import Identified
from property import OwnedObject, Property
from validation import *
from constants import *


class Interaction(Identified):
    def __init__(self, rdf_type=SBOL_INTERACTION, uri='example', interaction_type=SBO_INTERACTION):
        super().__init__(rdf_type, uri)
        self.functionalComponents = OwnedObject(self, SBOL_FUNCTIONAL_COMPONENTS, '0', '*', [libsbol_rule_18])
        self.types = Property(self, SBOL_TYPES, '1', '*', [], interaction_type)
        self.participations = OwnedObject(self, SBOL_PARTICIPATIONS, '0', '*', [])
        # TODO hidden properties
