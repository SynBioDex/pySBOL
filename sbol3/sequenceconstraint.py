from .constants import *
from .identified import Identified
from rdflib import URIRef
from .property import Property, URIProperty, ReferencedObject

class SequenceConstraint(Identified):

    def __init__(self, type_uri=SBOL_SEQUENCE_CONSTRAINT, uri=URIRef('example'), subject='', object='', restriction=SBOL_RESTRICTION_PRECEDES, version=VERSION_STRING):
        super().__init__(type_uri, uri, version)
        self.subject = ReferencedObject(self, SBOL_SUBJECT, SBOL_COMPONENT, '1', '1', [], subject)
        self.object = ReferencedObject(self, SBOL_OBJECT, SBOL_COMPONENT, '1', '1', [], object)
        self.restriction = URIProperty(self, SBOL_RESTRICTION, '1', '1', [], restriction)
