from .identified import Identified
from .constants import *
from rdflib import URIRef
from .property import URIProperty, ReferencedObject


class MapsTo(Identified):

    def __init__(self, type_uri=SBOL_MAPS_TO, uri=URIRef('example'), local='', remote='', refinement=SBOL_REFINEMENT_VERIFY_IDENTICAL, version=VERSION_STRING):
        super().__init__(type_uri, uri, version)
        self.local = ReferencedObject(self, SBOL_LOCAL, SBOL_COMPONENT, '1', '1', [], local)
        self.remote = ReferencedObject(self, SBOL_REMOTE, SBOL_COMPONENT, '1', '1', [], remote)
        self.refinement = URIProperty(self, SBOL_REFINEMENT, '1', '1', [], refinement)
