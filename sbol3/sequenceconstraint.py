from .constants import *
from .identified import Identified
from rdflib import URIRef
from .property import Property

class SequenceConstraint(Identified):

    def __init__(self, type_uri=SBOL_SEQUENCE_CONSTRAINT, uri=URIRef('example'), subject='', object='', restriction=SBOL_RESTRICTION_PRECEDES, version=VERSION_STRING):
        super().__init__(type_uri, uri, version)
        # TODO uses ReferencedObject