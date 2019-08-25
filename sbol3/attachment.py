from .toplevel import TopLevel
from .constants import *
from rdflib import URIRef
from .property import URIProperty, LiteralProperty


class Attachment(TopLevel):

    def __init__(self, type_uri=SBOL_ATTACHMENT, uri=URIRef("example"), version=VERSION_STRING, source=''):
        super().__init__(type_uri, uri, version)
        self._source = URIProperty(self, SBOL_SOURCE, '1', '1', [], source)
        self._format = LiteralProperty(self, SBOL_URI, '#format', '0', '1', [])
        self._size = LiteralProperty(self, SBOL_URI, '#size', '0', '1', [])
        self._hash = LiteralProperty(self, SBOL_URI, '#hash', '0', '1', [])

    @property
    def source(self):
        return self._source.value

    @source.setter
    def source(self, new_source):
        self._source.set(new_source)

    @property
    def format(self):
        return self._format.value

    @format.setter
    def format(self, new_format):
        self._format.set(new_format)

    @property
    def size(self):
        return self._size.value

    @size.setter
    def size(self, new_size):
        self._size.set(new_size)

    @property
    def hash(self):
        return self._hash.value

    @hash.setter
    def hash(self, new_hash):
        self._hash.set(new_hash)
