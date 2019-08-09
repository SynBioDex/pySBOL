from toplevel import TopLevel
from constants import *
from rdflib import URIRef
from property import URIProperty, LiteralProperty


class Attachment(TopLevel):

    def __init__(self, type_uri=SBOL_ATTACHMENT, uri=URIRef("example"), version=VERSION_STRING, source=''):
        super().__init__(type_uri, uri, version)
        self.source = URIProperty(self, SBOL_SOURCE, '1', '1', [], source)
        self.format = LiteralProperty(self, SBOL_URI, '#format', '0', '1', [])
        self.size = LiteralProperty(self, SBOL_URI, '#size', '0', '1', [])
        self.hash = LiteralProperty(self, SBOL_URI, '#hash', '0', '1', [])
