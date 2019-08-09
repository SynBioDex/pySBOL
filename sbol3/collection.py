from .toplevel import TopLevel
from rdflib import URIRef
from .constants import *
from .property import URIProperty


class Collection(TopLevel):

    def __init__(self, type_uri=SBOL_COLLECTION, uri=URIRef("example"), version=VERSION_STRING):
        super().__init__(type_uri, uri, version)
        self.members = URIProperty(self, SBOL_MEMBERS, '0', '*', [])
