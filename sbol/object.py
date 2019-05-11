from abc import ABCMeta, abstractmethod  # Note: Python 3 defines a helper class ABC.
from constants import *
from property import *
from validation import *

class SBOLObject(metaclass=ABCMeta):
    """An SBOLObject converts a Python data structure into an RDF triple store
     and contains methods for serializing and parsing RDF triples.
    """
    # 'Protected' members
    _namespaces = {}
    _default_namespace = None
    _hidden_properties = []

    # def _init(self, rdf_type, uri):
    #     raise NotImplementedError("Not yet implemented")

    def _serialize(self):
        # Convert and SBOL object into RDF triples.
        raise NotImplementedError("Not yet implemented")

    def _nest(self):
        # Pretty-writer that converts flat RDF/XML into nested RDF/XML (ie. SBOL)
        raise NotImplementedError("Not yet implemented")

    def _makeQName(self, uri):
        raise NotImplementedError("Not yet implemented")

    def _register_extension_class(self, ns, ns_prefix, class_name):
        """Register an extension class and its namespace, so custom data can be embedded into and read from SBOL files.

        :param ns: The extension namespace, eg, http://myhome.org/my_extension#.
        It's important that the namespace ends in a forward-slash or hash.
        :param ns_prefix: A shorthand symbol for the full namespace as it will appear in the output file,
        eg. my_extension.
        :param class_name: The extension class name.
        :return: The new class.
        """
        raise NotImplementedError("Not yet implemented")

    # 'Public' members
    doc = None
    rdf_type = None
    parent = None
    properties = {}
    owned_objects = {}

    # TODO Docstrings on variables isn't a thing in Python. Consider using Epydoc.
    # The identity property is REQUIRED by all Identified objects and has a data type of URI.
    # A given Identified object's identity URI MUST be globally unique among all other identity URIs.
    # The identity of a compliant SBOL object MUST begin with a URI prefix that maps to a domain
    # over which the user has control. Namely, the user can guarantee uniqueness of identities within this domain.
    # For other best practices regarding URIs see Section 11.2 of the
    # [SBOL specification doucment](http://sbolstandard.org/wp-content/uploads/2015/08/SBOLv2.0.1.pdf).
    identity = None

    def __init__(self, _rdf_type=UNDEFINED, uri="example"):
        """Open-world constructor."""
        self.rdf_type = _rdf_type
        self.identity = Property(self, SBOL_IDENTITY, '0', '1', [sbol_rule_10202], uri)

    @abstractmethod
    def getTypeURI(self):
        """
        :return: The uniform resource identifier that describes the RDF-type of this SBOL Object.
        """
        raise NotImplementedError("Child classes must define getTypeURI")

    def getClassName(self, rdf_type):
        """Parses a local class name from the RDF-type of this SBOL Object."""
        raise NotImplementedError("Not yet implemented")

    def find(self, uri):
        """Search this object recursively to see if an object or any child object with URI already exists.

        :param uri: The URI to search for.
        :return: The SBOLObject associated with this URI if it exists, None otherwise.
        """
        raise NotImplementedError("Not yet implemented")

    def cacheObjects(self, objectCache):
        """TODO document

        :param objectCache: a dictionary mapping strings to SBOLObjects
        :return: None
        """
        raise NotImplementedError("Not yet implemented")

    def find_property(self, uri):
        """Search this object recursively to see if it contains a member property with the given RDF type.

        :param uri: The RDF type of the property to search for.
        :return: The SBOLObject that contains a member property with the specified RDF type, None otherwise
        """
        raise NotImplementedError("Not yet implemented")

    def find_property_value(self, uri, value, matches=None):
        """Search this object recursively to see if it contains a member property with the given RDF type
        and indicated property value.

        :param uri: The RDF type of the property to search for.
        :param value: The property value to match.
        :param matches:
        :return: A vector containing all objects found that contain a member property with the specified RDF type
        """
        raise NotImplementedError("Not yet implemented")

    def find_reference(self, uri):
        """Search this object recursively to see if it contains a member property with the given RDF type
        and indicated property value.

        :param uri: A URI, either an ontology term or an object reference, to search for.
        :return: A vector containing all objects found that contain the URI in a property value.
        """
        raise NotImplementedError("Not yet implemented")

    def compare(self, comparand):
        """Compare two SBOL objects or Documents. The behavior is currently undefined for objects
        with custom annotations or extension classes.

        :param comparand: The object being compared to this one.
        :return: True if the objects are identical, False if they are different.
        """
        return self == comparand

    def __eq__(self, other):
        """Compare two SBOL objects or Documents. The behavior is currently undefined for objects
        with custom annotations or extension classes.

        :param other: The object being compared to this one.
        :return: True if the objects are identical, False if they are different.
        """
        # if other is None or not isinstance(other, SBOLObject):
        #     return False
        # if self.rdf_type != other.rdf_type:
        #     print(self.identity.get() + ' does not match type of ' + other.type())
        raise NotImplementedError("Not yet implemented")

    def getPropertyValue(self, property_uri):
        """Get the value of a custom annotation property by its URI.

        :param property_uri: The URI for the property.
        :return: The value of the property or SBOL_ERROR_NOT_FOUND.
        """
        raise NotImplementedError("Not yet implemented")

    def getPropertyValues(self, property_uri):
        """Get all values of a custom annotation property by its URI.

        :param property_uri: The URI for the property.
        :return: A vector of property values or SBOL_ERROR_NOT_FOUND.
        """
        raise NotImplementedError("Not yet implemented")

    def getProperties(self):
        """Gets URIs for all properties contained by this object. This includes SBOL core properties as well as
        custom annotations. Use this to find custom extension data in an SBOL file.

        :return: A vector of URIs that identify the properties contained in this object.
        """
        raise NotImplementedError("Not yet implemented")

    def setPropertyValue(self, property_uri, val):
        """Set and overwrite the value for a user-defined annotation property.

        :param property_uri:
        :param val: Either a literal or URI value.
        :return: None
        """
        raise NotImplementedError("Not yet implemented")

    def addPropertyValue(self, property_uri, val):
        """Append a value to a user-defined annotation property.

        :param property_uri:
        :param val: Either a literal or URI value.
        :return: None
        """
        raise NotImplementedError("Not yet implemented")

    def setAnnotation(self, property_uri, val):
        """Set the value for a user-defined annotation property. Synonymous with setPropertyValue.

        :param property_uri:
        :param val: If the value is a URI, it should be surrounded by angle brackets,
        else it will be interpreted as a literal value.
        :return: None
        """
        raise NotImplementedError("Not yet implemented")

    def getAnnotation(self, property_uri):
        """Get the value of a custom annotation property by its URI. Synonymous with getPropertyValue.

        :param property_uri: The URI for the property.
        :return: The value of the property or SBOL_ERROR_NOT_FOUND.
        """
        raise NotImplementedError("Not yet implemented")

    def apply(self, callback, user_data):
        """
        TODO document
        :param callback:
        :param user_data:
        :return: None
        """
        raise NotImplementedError("Not yet implemented")

    def update_uri(self):
        """
        TODO document
        :return: None
        """
        raise NotImplementedError("Not yet implemented")

    def serialize_rdf2xml(self, os, indentLevel):
        """Serialize the SBOLObject.

        :param os: Output stream.
        :param indentLevel:
        :return: None
        """
        raise NotImplementedError("Not yet implemented")

    def __str__(self):
        return self.identity.get()
