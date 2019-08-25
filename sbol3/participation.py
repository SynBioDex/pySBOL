from .identified import Identified
from .constants import *
from rdflib import URIRef
from .property import URIProperty, ReferencedObject, OwnedObject


class Participation(Identified):

    def __init__(self, type_uri=SBOL_PARTICIPATION, uri=URIRef('example'), participant='', version=VERSION_STRING):
        super().__init__(type_uri, uri, version)
        self._roles = URIProperty(self, SBOL_ROLES, '0', '*', [])
        self.participant = ReferencedObject(self, SBOL_PARTICIPANT, SBOL_FUNCTIONAL_COMPONENT, '1', '1', [], participant)
        self.measurements = OwnedObject(self, SBOL_MEASUREMENTS, '0', '*', [])

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

    def define(self, species, role=""):
        raise NotImplementedError('Not yet implemented')
