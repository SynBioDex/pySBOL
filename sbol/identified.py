from object import *
import validation


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

    def __init__(self, type_uri=SBOL_IDENTIFIED, uri='example', version=VERSION_STRING):
        super().__init__(type_uri, uri)
        self._persistentIdentity = Property(self, SBOL_PERSISTENT_IDENTITY, '0', '1', None, uri)
        self._displayId = Property(self, SBOL_DISPLAY_ID, '0', '1', validation.sbol_rule_10204)
        self._version = Property(self, SBOL_VERSION, '0', '1', None, version)
        self._name = Property(self, SBOL_NAME, '0', '1', None)
        self._description = Property(self, SBOL_DESCRIPTION, '0', '1', None)
        if Config.getOption(ConfigOptions.SBOL_COMPLIANT_URIS.value) is True:
            self._displayId.set(uri)
            self._identity.set(os.path.join(getHomespace(), uri, version))
            self._persistentIdentity.set(os.path.join(getHomespace(), uri))
        elif hasHomespace():
            self._identity.set(os.path.join(getHomespace(), uri))
            self._persistentIdentity.set(os.path.join(getHomespace(), uri))
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
        return self._name.value

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
