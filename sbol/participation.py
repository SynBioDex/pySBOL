from identified import Identified
from constants import *
from rdflib import URIRef


class Participation(Identified):

    def __init__(self, type_uri=SBOL_PARTICIPATION, uri=URIRef('example'), participant='', version=VERSION_STRING):
        super().__init__(type_uri, uri, version)
        # TODO ReferencedObject