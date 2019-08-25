from .identified import Identified
from .property import URIProperty, OwnedObject, ReferencedObject
from .constants import *


class ComponentInstance(Identified):
    def __init__(self, rdf_type, uri, definition, access, version):
        super().__init__(rdf_type, uri, version)
        self.definition = ReferencedObject(self, SBOL_DEFINITION, SBOL_COMPONENT_DEFINITION, '1', '1', [], definition)
        self._access = URIProperty(self, SBOL_ACCESS, '0', '1', [], access)
        self.mapsTos = OwnedObject(self, SBOL_MAPS_TOS, '0', '*', [])
        self.measurements = OwnedObject(self, SBOL_MEASUREMENTS, '0', '*', [])

    @property
    def access(self):
        return self._access.value

    @access.setter
    def access(self, new_access):
        self._access.set(new_access)


class Component(ComponentInstance):
    def __init__(self, uri=URIRef('example'), definition='', access=SBOL_ACCESS_PUBLIC, version=VERSION_STRING):
        super().__init__(SBOL_COMPONENT, uri, definition, access, version)
        self._roles = URIProperty(self, SBOL_ROLES, '0', '*', [])
        self._roleIntegration = URIProperty(self, SBOL_ROLE_INTEGRATION, '0', '1', [], SBOL_ROLE_INTEGRATION_MERGE)
        self.sourceLocations = OwnedObject(self, SBOL_LOCATIONS, '0', '*', [])

    @property
    def roles(self):
        return self._roles.value

    @roles.setter
    def roles(self, new_roles):
        self._roles.set(new_roles)

    def addRole(self, new_role):
        self._roles.add(new_role)

    def removeRole(self, index=0):
        self._roles.remove(index)

    @property
    def roleIntegration(self):
        return self._roleIntegration.value

    @roleIntegration.setter
    def roleIntegration(self, new_roleIntegration):
        self._roleIntegration.set(new_roleIntegration)


class FunctionalComponent(ComponentInstance):
    def __init__(self, uri=URIRef('example'), definition='', access=SBOL_ACCESS_PUBLIC, direction=SBOL_DIRECTION_NONE, version=VERSION_STRING):
        super().__init__(SBOL_FUNCTIONAL_COMPONENT, uri, definition, access, version)
        self._direction = URIProperty(self, SBOL_DIRECTION, '1', '1', [], direction)

    @property
    def direction(self):
        return self._direction.value

    @direction.setter
    def direction(self, new_direction):
        self._direction.set(new_direction)

    def connect(self, interface_component):
        raise NotImplementedError("Not yet implemented")

    def mask(self, masked_component):
        raise NotImplementedError("Not yet implemented")

    def override(selfself, masked_component):
        raise NotImplementedError("Not yet implemented")

    def isMasked(self):
        raise NotImplementedError("Not yet implemented")
