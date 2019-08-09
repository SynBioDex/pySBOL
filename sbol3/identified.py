from .object import *
from .constants import *
from . import validation


class Identified(SBOLObject):
    # The persistentIdentity property is OPTIONAL and has a data type of URI. This URI serves to uniquely refer to
    # a set of SBOL objects that are different versions of each other. An Identified object MUST be referred to
    # using either its identity URI or its persistentIdentity URI.
    _persistentIdentity = None

    # The displayId property is an OPTIONAL identifier with a data type of String. This property is intended to be an
    # intermediate between name and identity that is machine-readable, but more human-readable than the full URI
    # of an identity. If the displayId property is used, then its String value SHOULD be locally unique
    # (global uniqueness is not necessary) and MUST be composed of only alphanumeric or underscore characters
    # and MUST NOT begin with a digit.
    _displayId = None

    # If the version property is used, then it is RECOMMENDED that version numbering follow the conventions
    # of [semantic versioning](http://semver.org/), particularly as implemented by [Maven](http://maven.apache.org/).
    # This convention represents versions as sequences of numbers and qualifiers that are separated
    # by the characters '.' and '-' and are compared in lexicographical order (for example, 1 < 1.3.1 < 2.0-beta).
    # For a full explanation, see the linked resources.
    _version = None

    # The wasDerivedFrom property is OPTIONAL and has a data type of URI. An SBOL object with this property
    # refers to another SBOL object or non-SBOL resource from which this object was derived. If the wasDerivedFrom
    # property of an SBOL object A that refers to an SBOL object B has an identical persistentIdentity, and both
    # A and B have a version, then the version of B MUST precede that of A. In addition, an SBOL object MUST NOT
    # refer to itself via its own wasDerivedFrom property or form a cyclical chain of references via
    # its wasDerivedFrom property and those of other SBOL objects. For example, the reference chain
    # "A was derived from B and B was derived from A" is cyclical.
    _wasDerivedFrom = None

    # An Activity which generated this ComponentDefinition, eg., a design process like
    # codon-optimization or a construction process like Gibson Assembly
    _wasGeneratedBy = None

    # The name property is OPTIONAL and has a data type of String. This property is intended to be displayed to a human
    #  when visualizing an Identified object. If an Identified object lacks a name, then software tools SHOULD
    # instead display the object's displayId or identity. It is RECOMMENDED that software tools give users
    # the ability to switch perspectives between name properties that are human-readable and displayId properties
    # that are less human-readable, but are more likely to be unique.
    _name = None

    # The description property is OPTIONAL and has a data type of String.
    # This property is intended to contain a more thorough text description of an Identified object.
    _description = None

    def __init__(self, type_uri=SBOL_IDENTIFIED, uri=URIRef('example'), version=VERSION_STRING):
        super().__init__(type_uri, uri)
        self._persistentIdentity = URIProperty(self, SBOL_PERSISTENT_IDENTITY, '0', '1', None, URIRef(uri))
        self._displayId = LiteralProperty(self, SBOL_DISPLAY_ID, '0', '1', [validation.sbol_rule_10204])
        self._version = LiteralProperty(self, SBOL_VERSION, '0', '1', None, version)
        self._name = LiteralProperty(self, SBOL_NAME, '0', '1', None)
        self._description = LiteralProperty(self, SBOL_DESCRIPTION, '0', '1', None)
        if Config.getOption(ConfigOptions.SBOL_COMPLIANT_URIS.value) is True:
            self._displayId.set(uri)
            self._persistentIdentity.set(URIRef(os.path.join(getHomespace(), uri)))
            if Config.getOption(ConfigOptions.SBOL_TYPED_URIS.value) is True:
                if version != '':
                    self._identity.set(URIRef(os.path.join(getHomespace(), self.getClassName(type_uri), uri, version)))
                else:
                    self._identity.set(URIRef(os.path.join(getHomespace(), self.getClassName(type_uri), uri)))
            else:
                if version != '':
                    self._identity.set(URIRef(os.path.join(getHomespace(), uri, version)))
                else:
                    self._identity.set(URIRef(os.path.join(getHomespace(), uri)))
        elif hasHomespace():
            self._identity.set(URIRef(os.path.join(getHomespace(), uri)))
            self._persistentIdentity.set(URIRef(os.path.join(getHomespace(), uri)))
        # self._identity.validate() # TODO

    @property
    def persistentIdentity(self):
        return self._persistentIdentity.value

    @persistentIdentity.setter
    def persistentIdentity(self, new_persistentIdentity):
        self._persistentIdentity.set(new_persistentIdentity)

    @property
    def displayId(self):
        return self._displayId.value

    @displayId.setter
    def displayId(self, new_displayId):
        self._displayId.set(new_displayId)

    @property
    def version(self):
        return self._version.value

    @version.setter
    def version(self, new_version):
        self._version.set(new_version)

    @property
    def description(self):
        return self._description.value

    @description.setter
    def description(self, new_description):
        self._description.set(new_description)

    def generate(self):
        raise NotImplementedError("Not yet implemented")

    def update_uri(self):
        """
        Recursively generates SBOL compliant ids for an object and all
        its owned objects, then checks to make sure that these ids are unique.
        :return: None
        """
        if self.parent is None:
            raise Exception('update_uri: Parent cannot be None')
        parent = self.parent
        if Config.getOption(ConfigOptions.SBOL_COMPLIANT_URIS) is True:
            # Form compliant URI for child object
            persistent_id = parent.properties[SBOL_PERSISTENT_IDENTITY][0]
            persistent_id = os.path.join(persistent_id, self.displayId)
            if len(parent.properties[SBOL_VERSION]) > 0:
                version = parent.properties[SBOL_VERSION][0]
            else:
                version = VERSION_STRING
            obj_id = os.path.join(persistent_id, version)
            # Reset SBOLCompliant properties
            self._identity.set(obj_id)
            self._persistentIdentity.set(persistent_id)
            # Check for uniqueness of URI in local object properties
            matches = parent.find_property_value(SBOL_IDENTIFIED, obj_id)
            if len(matches) > 0:
                raise SBOLError("Cannot update SBOL-compliant URI. The URI " + self.identity + " is not unique",
                                SBOLErrorCode.SBOL_ERROR_URI_NOT_UNIQUE)
            for rdf_type, store in self.owned_objects:
                if rdf_type not in self._hidden_properties:
                    for nested_obj in store:
                        nested_obj.update_uri()
        # Check for uniqueness of URI in Document
        if parent.doc:
            matches = parent.doc.find_property_value(SBOL_IDENTITY, self.identity)
            if len(matches) > 0:
                raise SBOLError("Cannot update SBOL-compliant URI. "
                                "An object with URI " + self.identity + " is already in the Document",
                                SBOLErrorCode.SBOL_ERROR_URI_NOT_UNIQUE)
