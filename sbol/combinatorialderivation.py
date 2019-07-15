from identified import Identified
from toplevel import TopLevel
from constants import *
from rdflib import URIRef
from property import Property


class VariableComponent(Identified):

    def __init__(self, type_uri=SBOL_IDENTIFIED, uri=URIRef('example'), repeat='http://sbols.org/v2#on', version=VERSION_STRING):
        super().__init__(type_uri, uri, version)
        self.variable = Property(self, SBOL_VARIABLE, SBOL_COMPONENT, '0', '1', [])
        self.repeat = Property(self, SBOL_OPERATOR, '1', '1', [], repeat)
        self.variants = Property(self, SBOL_VARIANTS, SBOL_COMPONENT_DEFINITION, '0', '*', [])
        self.variantCollections = Property(self, SBOL_VARIANT_COLLECTIONS, SBOL_COLLECTION, '0', '*', [])
        self.variantDerivations = Property(self, SBOL_VARIANT_DERIVATIONS, SBOL_COMBINATORIAL_DERIVATION, '0', '*', [])


class CombinatorialDerivation(TopLevel):

    def __init__(self, type_uri=SBOL_COMBINATORIAL_DERIVATION, uri=URIRef("example"), strategy='http://sbols.org/v2#enumerate', version=VERSION_STRING):
        super().__init__(type_uri, uri, version)
        self.strategy = Property(self, SBOL_STRATEGY, '1', '1', [])  # TODO in original source, it doesn't look like strategy is used
        self.masterTemplate = Property(self, SBOL_TEMPLATE, SBOL_COMBINATORIAL_DERIVATION, '0', '1', [])
        self.variableComponents = Property(self, SBOL_VARIABLE_COMPONENTS, '0', '*', [])
