from identified import Identified
from constants import *
from rdflib import URIRef


class MapsTo(Identified):

    def __init__(self, type_uri=SBOL_MAPS_TO, uri=URIRef('example'), local='', remote='', refinedment=SBOL_REFINEMENT_VERIFY_IDENTICAL, version=VERSION_STRING):
        super().__init__(type_uri, uri, version)
        # TODO uses ReferencedObject
