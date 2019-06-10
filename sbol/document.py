from identified import *
from config import *
from componentdefinition import ComponentDefinition
from sequence import Sequence
from moduledefinition import ModuleDefinition
from object import SBOLObject
import rdflib
import os


class Document(Identified):
    """
    The Document is a container for all SBOL data objects.

    In a previous era, engineers might sit at a drafting board and draft a design by hand.
    The engineer's drafting sheet in LibSBOL is called a Document. The Document serves as a container,
    initially empty, for SBOL data objects. All file I/O operations are performed on the Document
    to populate it with SBOL objects representing design elements.
    """

    SBOL_DATA_MODEL_REGISTER = {
        UNDEFINED: SBOLObject,
        SBOL_IDENTIFIED: Identified,
        SBOL_COMPONENT_DEFINITION: ComponentDefinition,
        SBOL_SEQUENCE: Sequence,
        SBOL_MODULE_DEFINITION: ModuleDefinition
    }

    def __init__(self, filename=None):
        """
        Construct a document.

        :param filename: (optional) a file to initialize the Document.
        """
        super().__init__(SBOL_DOCUMENT, "", VERSION_STRING)
        # The Document's register of objects
        self.objectCache = {}  # Needed?
        self.SBOLObjects = {}  # Needed?
        self.resource_namespaces = None
        self.designs = OwnedObject(self, SYSBIO_DESIGN, '0', '*', [libsbol_rule_11])
        self.builds = OwnedObject(self, SYSBIO_BUILD, '0', '*', [libsbol_rule_12])
        self.tests = OwnedObject(self, SYSBIO_TEST, '0', '*', [libsbol_rule_13])
        self.analyses = OwnedObject(self, SYSBIO_ANALYSIS, '0', '*', [libsbol_rule_14])
        self.componentDefinitions = OwnedObject(self, SBOL_COMPONENT_DEFINITION, '0', '*', None)
        self.moduleDefinitions = OwnedObject(self, SBOL_MODULE_DEFINITION, '0', '*', None)
        self.models = OwnedObject(self, SBOL_MODEL, '0', '*', None)
        self.sequences = OwnedObject(self, SBOL_SEQUENCE, '0', '*', None)
        self.collections = OwnedObject(self, SBOL_COLLECTION, '0', '*', None)
        self.activities = OwnedObject(self, PROVO_ACTIVITY, '0', '*', None)
        self.plans = OwnedObject(self, PROVO_PLAN, '0', '*', None)
        self.agents = OwnedObject(self, PROVO_AGENT, '0', '*', None)
        self.attachments = OwnedObject(self, SBOL_ATTACHMENT, '0', '*', None)
        self.combinatorialderivations = OwnedObject(self, SBOL_COMBINATORIAL_DERIVATION, '0', '*', None)
        self.implementations = OwnedObject(self, SBOL_IMPLEMENTATION, '0', '*', None)
        self.sampleRosters = OwnedObject(self, SYSBIO_SAMPLE_ROSTER, '0', '*', [validation.libsbol_rule_16])
        self.experiments = OwnedObject(self, SBOL_EXPERIMENT, '0', '*', None)
        self.experimentalData = OwnedObject(self, SBOL_EXPERIMENTAL_DATA, '0', '*', None)

        self.citations = Property(self, PURL_URI + "bibliographicCitation", '0', '*', None)
        self.graph = None
        self.keywords = Property(self, PURL_URI + "elements/1.1/subject", '0', '*', None)

    def add(self, sbol_obj):
        """
        Register an object in the Document.

        :param sbol_obj: The SBOL object(s) you want to serialize. Either a single object or a list of objects.
        :return: None
        """
        # Check for uniqueness of URI
        if sbol_obj.identity in self.SBOLObjects:
            raise SBOLError('Cannot add ' + sbol_obj.identity + ' to Document. An object with this identity '
                            'is already contained in the Document', SBOLErrorCode.SBOL_ERROR_URI_NOT_UNIQUE)
        else:
            # If TopLevel add to Document.
            if sbol_obj.is_top_level():
                self.SBOLObjects[sbol_obj.identity] = sbol_obj
            if sbol_obj.getTypeURI() in self.owned_objects:
                sbol_obj.parent = self  # Set back-pointer to parent object
                # Add the object to the Document's property store, eg, componentDefinitions, moduleDefinitions, etc.
                self.owned_objects[sbol_obj.getTypeURI()].append(sbol_obj)
            sbol_obj.doc = self
            # Recurse into child objects and set their back-pointer to this Document
            for key, obj_store in self.owned_objects.items():
                for child_obj in obj_store:
                    if child_obj.doc != self:
                        self.add(child_obj)

    def add_list(self, sbol_objs):
        for obj in sbol_objs:
            self.add(obj)

    def addNamespace(self, ns, prefix):
        """Add a new namespace to the Document.

        :param ns: The namespace, eg. http://sbols.org/v2#
        :param prefix: The namespace prefix, eg. sbol
        :return:
        """
        raise NotImplementedError("Not yet implemented")

    def addComponentDefinition(self, sbol_obj):
        """
        Convenience method for adding a component definition.

        :param sbol_obj: component definition
        :return: None
        """
        if isinstance(sbol_obj, list):
            for obj in sbol_obj:
                self.add(obj)
        else:
            self.add(sbol_obj)

    def addModuleDefinition(self, sbol_obj):
        """
        Convenience method for adding a module definition.

        :param sbol_obj: module definition
        :return: None
        """
        self.add(sbol_obj)

    def addSequence(self, sbol_obj):
        """
        Convenience method for adding a sequence.

        :param sbol_obj: sequence
        :return: None
        """
        self.add(sbol_obj)

    def addModel(self, sbol_obj):
        """
        Convenience method for adding a model.

        :param sbol_obj: model
        :return: None
        """
        self.add(sbol_obj)

    def create(self, uri):
        """
        Creates another SBOL object derived from TopLevel and adds it to the Document.
        NOTE: originally from ReferencedObject
        :param uri: In "open world" mode, this is a full URI and the same as the returned URI.
        If the default namespace for libSBOL has been configured, then this argument should simply be a
        local identifier. If SBOL-compliance is enabled, this argument should be the intended
        displayId of the new object. A full URI is automatically generated and returned.
        :return: The full URI of the created object
        """
        if Config.getOption(ConfigOptions.SBOL_COMPLIANT_URIS.value) is True:
            obj = Identified()
            #obj.identity = os.path.join(getHomespace(), )
        raise NotImplementedError("Not yet implemented")

    def get(self, uri):
        """
        Retrieve an object from the Document.
cas9 = ComponentDefinition('Cas9', BIOPAX_PROTEIN)
        :param uri: The identity of the SBOL object you want to retrieve.
        :return: The SBOL object.
        """
        # TODO may want to move into SBOLObject or Property
        # First, search the object's property store for the uri
        if uri in self.objectCache:
            return self.objectCache[uri]
        if Config.getOption(ConfigOptions.SBOL_COMPLIANT_URIS.value) is True:
            return

    def getAll(self):
        """
        Retrieve a list of objects from the Document.

        :return: A list of objects from the Document.
        """
        raise NotImplementedError("Not yet implemented")

    def getComponentDefinition(self, uri):
        # NOTE: I couldn't find this in the original libSBOL source, but they are
        # heavily used in all the unit tests.
        return self.componentDefinitions.get(uri)

    def getModuleDefinition(self, uri):
        return self.moduleDefinitions.get(uri)

    def getSequence(self, uri):
        raise NotImplementedError("Not yet implemented")

    def getModel(self, uri):
        raise NotImplementedError("Not yet implemented")

    # File I/O #
    def write(self, filename):
        """
        Serialize all objects in this Document to an RDF/XML file.

        :param filename: The full name of the file you want to write (including file extension).
        :return: A string with the validation results, or empty string if validation is disabled.
        """
        self.doc_serialize_rdf2xml(filename, output_format=ConfigOptions.SERIALIZATION_FORMAT.value)

    def read(self, filename):
        """
        Read an RDF/XML file and attach the SBOL objects to this Document.

        Existing contents of the Document will be wiped.
        :param filename: The full name of the file you want to read (including file extension).
        :return: None
        """
        self.clear()
        self.append(filename)

    def readString(self, sbol_str):
        """
        Convert text in SBOL into data objects.

        :param sbol_str: A string formatted in SBOL.
        :return: None
        """
        raise NotImplementedError("Not yet implemented")

    def writeString(self):
        """
        Convert data objects in this Document into textual SBOL.

        :return: A string representation of the objects in this Document.
        """
        raise NotImplementedError("Not yet implemented")

    def append(self, filename):
        """
        Read an RDF/XML file and attach the SBOL objects to this Document.

        New objects will be added to the existing contents of the Document.
        :param filename: The full name of the file you want to read (including file extension).
        :return: None
        """
        with open(filename, 'r') as f:
            graph = rdflib.Graph()
            graph.parse(f, format="application/rdf+xml")
            # Parse namespaces
            for ns in graph.namespaces():
                self._namespaces[ns[0]] = str('<' + ns[1] + '>')
            # Find top-level objects
            top_level_query = "PREFIX : <http://example.org/ns#> " \
                "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> " \
                "PREFIX sbol: <http://sbols.org/v2#> " \
                "SELECT ?s ?o " \
                "{ ?s a ?o }"
            sparql_results = graph.query(top_level_query)
            for result in sparql_results:
                subject = str(result.s)
                obj = str(result.o)
                self.parse_objects_inner(subject, obj)
            # Find everything in the triple store
            all_query = "PREFIX : <http://example.org/ns#> " \
                "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> " \
                "PREFIX sbol: <http://sbols.org/v2#> " \
                "SELECT ?s ?p ?o " \
                "{ ?s ?p ?o }"
            all_results = graph.query(all_query)
            # Find the graph base uri.  This is the location of the sbol
            # file, and begins with the "file://" scheme.  Any URI in the
            # file without a scheme will appear relative to this URI, after
            # the file is parsed.  Therefore, if the any URI property value
            # begins with the graph base uri, the base part of the URI is removed.
            graphBaseURIStr = "file://" + os.getcwd() # Not sure if this is correct...
            # Remove the filename from the path
            pos = graphBaseURIStr.rfind('/')
            if pos != -1:
                pos += 1
            rdf_type = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
            for result in all_results:
                predicate = str(result.p)
                # Look for properties
                if predicate != rdf_type:
                    subject = str(result.s)
                    obj = result.o
                    lval = str(obj)
                    if isinstance(result.o, URIRef) and pos != -1:
                        if lval[:pos] == graphBaseURIStr:
                            # This was a URI without a scheme.  Remove URI base
                            lval = lval[pos:]
                    # If the literal value is a URI, wrap it in < and >, otherwise wrap it in quotes
                    if isinstance(result.o, URIRef):
                        padStart = '<'
                        padEnd = '>'
                    else:
                        padStart = '"'
                        padEnd = '"'
                    obj_str = padStart + lval + padEnd
                    self.parse_properties_inner(subject, predicate, obj_str)
            # TODO parse annotation objects
            # TODO dress document

    def parse_objects_inner(self, subject_str, obj_str):
        if subject_str not in self.SBOLObjects and obj_str in self.SBOL_DATA_MODEL_REGISTER:
            # Call constructor for the appropriate SBOLObject
            new_obj = self.SBOL_DATA_MODEL_REGISTER[obj_str]()
            # Wipe default property values passed from default
            # constructor. New property values will be added as properties
            # are parsed from the input file
            for prop_name, values in new_obj.properties.items():
                token = values[0]
                if token[0] == '<':
                    values.clear()
                    values.ppend('<>')
                elif token[0] == '"':
                    values.clear()
                    values.append('""')
            new_obj.identity.set(subject_str)
            # Update document
            self.SBOLObjects[new_obj.identity.get()] = new_obj
            new_obj.doc = self
            # For now, set the parent to the Document. This may get overwritten later for child objects.
            new_obj.parent = self
            # If the new object is TopLevel, add to the Document's property store
            if new_obj.is_top_level():
                self.owned_objects[new_obj.rdf_type].append(new_obj)
        elif subject_str not in self.SBOLObjects and obj_str not in self.SBOL_DATA_MODEL_REGISTER:
            # Generic TopLevels
            new_obj = SBOLObject()
            new_obj.identity.set(subject_str)
            new_obj.rdf_type = obj_str
            self.SBOLObjects[new_obj.identity.get()] = new_obj
            new_obj.doc = self

    def parse_properties_inner(self, subject, predicate, obj):
        id = subject
        property_uri = predicate
        property_value = self.convert_ntriples_encoding_to_ascii(obj)
        found = property_uri.rfind('#')
        if found == -1:
            found = property_uri.rfind('/')
        if found != -1:
            property_ns, property_name = property_uri.split[found]
            # Checks if the object to which this property belongs already exists
            if id in self.SBOLObjects:
                sbol_obj = self.SBOLObjects[id]
                # Decide if this triple corresponds to a simple property,
                # a list property, an owned property or a referenced property
                if property_uri in sbol_obj.properties:
                    # triple is a property
                    if sbol_obj.properties[property_uri] == '<>' or \
                            sbol_obj.properties[property_uri] == '""':
                        sbol_obj.properties[property_uri].clear()
                    sbol_obj.properties[property_uri].append(property_value)
                elif property_uri in sbol_obj.owned_objects:
                    # triple is an owned object
                    # Strip off the angle brackets from the URI value.
                    # Note that a Document's object_store and
                    # correspondingly, an SBOLObject's property_store
                    # uses stripped URIs as keys, while libSBOL uses as a
                    # convention angle brackets or quotes for Literal values
                    owned_obj_id = property_value[1:-1]
                    owned_obj_lookup = self.SBOLObjects[owned_obj_id]
                    if owned_obj_lookup is not None:
                        owned_obj = owned_obj_lookup
                        sbol_obj.owned_objects[property_uri].append(owned_obj)
                        owned_obj.parent = sbol_obj
                        del self.SBOLObjects[owned_obj_id]
                    pass
                else:
                    # Extension data
                    sbol_obj.properties[property_uri].append(property_value)

    def convert_ntriples_encoding_to_ascii(self, s):
        s.replace("\\\"", "\"")
        s.replace("\\\\", "\\")
        return s

    # Online validation #
    def request_validation(self, sbol_str):
        # TODO what is this method supposed to do?
        raise NotImplementedError("Not yet implemented")

    def request_comparison(self, diff_file):
        """
        Perform comparison on Documents using the online validation tool.

        This is for cross-validation of SBOL documents with libSBOLj. Document comparison can also be performed
        using the built-in compare method.
        :param diff_file:
        :return: The comparison results
        """
        raise NotImplementedError("Not yet implemented")

    def clear(self):
        """
        Delete all properties and objects in the Document.

        :return: None
        """
        self.SBOLObjects.clear()
        for name, vals in self.properties.items():
            if vals[0] == '<':
                reinitialized_property = '<>'
            else:
                reinitialized_property = '""'
            vals.clear()
            vals.append(reinitialized_property)
        for object_store in self.owned_objects.values():
            object_store.clear()
        self._namespaces.clear()
        self.graph = rdflib.Graph()  # create a new graph

    def query_repository(self, command):
        """

        :param command:
        :return: str
        """
        # TODO better docstring
        raise NotImplementedError("Not yet implemented")

    def search_metadata(self, role, type, name, collection):
        """

        :param role:
        :param type:
        :param name:
        :param collection:
        :return: str
        """
        # TODO better docstring
        raise NotImplementedError("Not yet implemented")

    # TODO The commented-out methods below are important, but they rely heavily on raptor
    # static std::string string_from_raptor_term(raptor_term *term, bool addWrapper=false);
    #
    # /// Generates rdf/xml
    # void generate(raptor_world** world, raptor_serializer** sbol_serializer, char** sbol_buffer, size_t* sbol_buffer_len, raptor_iostream** ios, raptor_uri** base_uri);

    def doc_serialize_rdf2xml(self, out, output_format=ConfigOptions.SERIALIZATION_FORMAT.value):
        """
        Serialize RDF XML.
        :param out: output stream
        :param output_format: output format
        :return: None
        """
        graph = rdflib.Graph()
        # TODO Add default namespace if there is one
        # Add namespaces
        for name, ns in self._namespaces:
            graph.bind(name, ns)
        # Add top-level objects
        for rdf_type, obj in self.SBOLObjects:
            graph.add((self.identity, rdf_type, obj.identity))
            obj.serialize_rdf2xml(graph)
        graph.serialize(out)

    def validate(self):
        """
        Run validation on this Document via the online validation tool.

        :return: A string containing a message with the validation results
        """
        raise NotImplementedError("Not yet implemented")

    def size(self):
        """
        Get the total number of objects in the Document, including SBOL core object and custom annotation objects.

        :return: The total number of objects in the Document.
        """
        return len(self.SBOLObjects)

    def __len__(self):
        """
        Get the total number of objects in the Document, including SBOL core object and custom annotation objects.

        (Returns the same thing as size())

        :return: The total number of objects in the Document.
        """
        return self.size()

    def __str__(self):
        """
        Produce a string representation of the Document.

        :return: A string representation of the Document.
        """
        return self.summary()

    def cacheObjectsDocument(self):
        # TODO docstring
        raise NotImplementedError("Not yet implemented")

    def referenceNamespace(self, uri):
        """Replaces the namespace with a reference and removes the default namespace, shortening the URI.
        :param uri:
        :return: str
        """
        if self._default_namespace is not None and len(self._default_namespace) > 0:
            if self._default_namespace in uri:
                uri.replace(self._default_namespace, '')
                return uri
        for abbrev, ns in self._namespaces.items():
            if ns in uri:
                # Assume only one namespace per URI
                uri.replace(ns, abbrev)
                return uri

    def summary(self):
        """
        Produce a string representation of the Document.

        :return: A string representation of the Document.
        """
        summary = ''
        col_size = 30
        total_core_objects = 0
        for rdf_type, obj_store in self.owned_objects.items():
            property_name = parsePropertyName(rdf_type)
            obj_count = len(obj_store)
            total_core_objects += obj_count
            summary += property_name
            summary += '.' * (col_size-len(property_name))
            summary += str(obj_count) + '\n'
        summary += 'Annotation Objects'
        summary += '.' * (col_size-18)
        summary += str(self.size() - total_core_objects) + '\n'
        summary += '---\n'
        summary += 'Total: '
        summary += '.' * (col_size-5)
        summary += str(self.size()) + '\n'
        return summary

    # TODO Port iterator, which loops over top-level items of Document

    def find(self, uri):
        """
        Search recursively for an SBOLObject in this Document that matches the uri.

        :param uri: The identity of the object to search for.
        :return: A pointer to the SBOLObject, or NULL if an object with this identity doesn't exist.
        """
        for obj in self.SBOLObjects:
            match = obj.find(uri)
            if match is not None:
                return match
        return None

    def getTypeURI(self):
        return SBOL_DOCUMENT
