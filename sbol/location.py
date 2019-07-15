from identified import Identified
from constants import *
from property import Property
from rdflib import URIRef

class Location(Identified):

    def __init__(self, type_uri=SBOL_LOCATION, uri=URIRef('example'), orientation=SBOL_ORIENTATION_INLINE):
        super().__init__(type_uri, uri)
        self.orientation = Property(self, SBOL_ORIENTATION, '1', '1', [], orientation)
        self.sequence = Property(self, SBOL_SEQUENCE_PROPERTY, SBOL_SEQUENCE, '0', '1', [])


class Range(Location):
    pass


class Cut(Location):
    pass


class GenericLocation(Location):
    pass
