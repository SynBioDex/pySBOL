from .toplevel import TopLevel
from .property import Property, URIProperty
from .constants import *


class Model(TopLevel):
    def __init__(self, rdf_type=SBOL_MODEL, uri=URIRef('example'), source='', language=EDAM_SBML, framework=SBO_CONTINUOUS, version=VERSION_STRING):
        super().__init__(rdf_type, uri, version)
        self.source = URIProperty(self, SBOL_SOURCE, '0', '1', [], source)
        self.language = URIProperty(self, SBOL_LANGUAGE, '0', '1', [], language)
        self.framework = URIProperty(self, SBOL_FRAMEWORK, '0', '1', [], framework)
