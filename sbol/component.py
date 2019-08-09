from identified import Identified
from property import URIProperty, OwnedObject, ReferencedObject
from constants import *


class ComponentInstance(Identified):
    def __init__(self, rdf_type, uri, definition, access, version):
        super().__init__(rdf_type, uri, version)
        self.definition = ReferencedObject(self, SBOL_DEFINITION, SBOL_COMPONENT_DEFINITION, '1', '1', [], definition)
        self.access = URIProperty(self, SBOL_ACCESS, '0', '1', [], access)
        self.mapsTos = OwnedObject(self, SBOL_MAPS_TOS, '0', '*', [])
        self.measurements = OwnedObject(self, SBOL_MEASUREMENTS, '0', '*', [])


class Component(ComponentInstance):
    def __init__(self, uri=URIRef('example'), definition='', access=SBOL_ACCESS_PUBLIC, version=VERSION_STRING):
        super().__init__(SBOL_COMPONENT, uri, definition, access, version)
        self.roles = URIProperty(self, SBOL_ROLES, '0', '*', [])
        self.roleIntegration = URIProperty(self, SBOL_ROLE_INTEGRATION, '0', '1', [], SBOL_ROLE_INTEGRATION_MERGE)
        self.sourceLoactions = OwnedObject(self, SBOL_LOCATIONS, '0', '*', [])


class FunctionalComponent(ComponentInstance):
    def __init__(self, uri=URIRef('example'), definition='', access=SBOL_ACCESS_PUBLIC, direction=SBOL_DIRECTION_NONE, version=VERSION_STRING):
        super().__init__(SBOL_FUNCTIONAL_COMPONENT, uri, definition, access, version)
        self.direction = URIProperty(self, SBOL_DIRECTION, '1', '1', [], direction)

    def connect(self, interface_component):
        raise NotImplementedError("Not yet implemented")

    def mask(self, masked_component):
        raise NotImplementedError("Not yet implemented")

    def override(selfself, masked_component):
        raise NotImplementedError("Not yet implemented")

    def isMasked(self):
        raise NotImplementedError("Not yet implemented")
