from toplevel import TopLevel
from rdflib import URIRef
from constants import *
from property import ReferencedObject

class ExperimentalData(TopLevel):
    def __init__(self, uri=URIRef('example'), version=VERSION_STRING):
        super().__init__(SBOL_EXPERIMENTAL_DATA, uri, version)


class Experiment(TopLevel):
    def __init__(self, uri=URIRef('example'), version=VERSION_STRING):
        super().__init__(SBOL_EXPERIMENT, uri, version)
        self.experimentalData = ReferencedObject(self, SBOL_URI + "#experimentalData", SBOL_EXPERIMENTAL_DATA, '0', '*', [])
