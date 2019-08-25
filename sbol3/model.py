from .toplevel import TopLevel
from .property import Property, URIProperty
from .constants import *


class Model(TopLevel):
    def __init__(self, rdf_type=SBOL_MODEL, uri=URIRef('example'), source='', language=EDAM_SBML, framework=SBO_CONTINUOUS, version=VERSION_STRING):
        super().__init__(rdf_type, uri, version)
        self._source = URIProperty(self, SBOL_SOURCE, '0', '1', [], source)
        self._language = URIProperty(self, SBOL_LANGUAGE, '0', '1', [], language)
        self._framework = URIProperty(self, SBOL_FRAMEWORK, '0', '1', [], framework)

    @property
    def source(self):
        return self._source.value

    @source.setter
    def source(self, new_source):
        self._source.set(new_source)

    @property
    def language(self):
        return self._language.value

    @language.setter
    def language(self, new_language):
        self._language.set(new_language)

    @property
    def framework(self):
        return self._framework.value

    @framework.setter
    def framework(self, new_framework):
        self._framework.set(new_framework)
