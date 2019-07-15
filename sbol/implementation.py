from toplevel import TopLevel
from rdflib import URIRef
from constants import *
from property import Property


class Implementation(TopLevel):

    def __init__(self, type_uri=SBOL_IMPLEMENTATION, uri=URIRef("example"), version=VERSION_STRING):
        super().__init__(type_uri, uri, version)
        self.built = Property(self, SBOL_URI+'#built', '0', '1', [])
