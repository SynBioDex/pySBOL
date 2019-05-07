from object import *


class Identified(SBOLObject):
    def __init__(self, type_uri=SBOL_IDENTIFIED, uri="example", version=VERSION_STRING):
        super().__init__(type_uri, uri)

    # The persistentIdentity property is OPTIONAL and has a data type of URI. This URI serves to uniquely refer to
    # a set of SBOL objects that are different versions of each other. An Identified object MUST be referred to
    # using either its identity URI or its persistentIdentity URI.
    persistentIdentity = None

    # The displayId property is an OPTIONAL identifier with a data type of String. This property is intended to be an
    # intermediate between name and identity that is machine-readable, but more human-readable than the full URI
    # of an identity. If the displayId property is used, then its String value SHOULD be locally unique
    # (global uniqueness is not necessary) and MUST be composed of only alphanumeric or underscore characters
    # and MUST NOT begin with a digit.
    displayId = None

    # If the version property is used, then it is RECOMMENDED that version numbering follow the conventions
    # of [semantic versioning](http://semver.org/), particularly as implemented by [Maven](http://maven.apache.org/).
    # This convention represents versions as sequences of numbers and qualifiers that are separated
    # by the characters '.' and '-' and are compared in lexicographical order (for example, 1 < 1.3.1 < 2.0-beta).
    # For a full explanation, see the linked resources.
    version = None

    # The wasDerivedFrom property is OPTIONAL and has a data type of URI. An SBOL object with this property
    # refers to another SBOL object or non-SBOL resource from which this object was derived. If the wasDerivedFrom
    # property of an SBOL object A that refers to an SBOL object B has an identical persistentIdentity, and both
    # A and B have a version, then the version of B MUST precede that of A. In addition, an SBOL object MUST NOT
    # refer to itself via its own wasDerivedFrom property or form a cyclical chain of references via
    # its wasDerivedFrom property and those of other SBOL objects. For example, the reference chain
    # "A was derived from B and B was derived from A" is cyclical.
    wasDerivedFrom = None

    # An Activity which generated this ComponentDefinition, eg., a design process like
    # codon-optimization or a construction process like Gibson Assembly
    wasGeneratedBy = None

    # The name property is OPTIONAL and has a data type of String. This property is intended to be displayed to a human
    #  when visualizing an Identified object. If an Identified object lacks a name, then software tools SHOULD
    # instead display the object's displayId or identity. It is RECOMMENDED that software tools give users
    # the ability to switch perspectives between name properties that are human-readable and displayId properties
    # that are less human-readable, but are more likely to be unique.
    name = None

    # The description property is OPTIONAL and has a data type of String.
    # This property is intended to contain a more thorough text description of an Identified object.
    description = None

    def generate(self):
        raise NotImplementedError("Not yet implemented")
