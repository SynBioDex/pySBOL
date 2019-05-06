class Document:
    """
    The Document is a container for all SBOL data objects.

    In a previous era, engineers might sit at a drafting board and draft a design by hand.
    The engineer's drafting sheet in LibSBOL is called a Document. The Document serves as a container,
    initially empty, for SBOL data objects. All file I/O operations are performed on the Document
    to populate it with SBOL objects representing design elements.
    """

    def __init__(self, filename=None):
        """
        Construct a document.

        :param filename: (optional) a file to initialize the Document.
        """
        pass

    def add(self, sbol_objs):
        """
        Register an object in the Document.

        :param sbol_objs: The SBOL object(s) you want to serialize. Either a single object or a list of objects.
        :return: None
        """
        pass

    def addComponentDefinition(self, sbol_obj):
        """
        Convenience method for adding a component definition.

        :param sbol_obj: component definition
        :return: None
        """
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

    def get(self, uri):
        """
        Retrieve an object from the Document.

        :param uri: The identity of the SBOL object you want to retrieve.
        :return: The SBOL object.
        """
        pass

    def getAll(self):
        """
        Retrieve a list of objects from the Document.

        :return: A list of objects from the Document.
        """
        pass

    # File I/O #
    def write(self, filename):
        """
        Serialize all objects in this Document to an RDF/XML file.

        :param filename: The full name of the file you want to write (including file extension).
        :return: A string with the validation results, or empty string if validation is disabled.
        """
        pass

    def read(self, filename):
        """
        Read an RDF/XML file and attach the SBOL objects to this Document.

        Existing contents of the Document will be wiped.
        :param filename: The full name of the file you want to read (including file extension).
        :return: None
        """
        pass

    def readString(self, sbol_str):
        """
        Convert text in SBOL into data objects.

        :param sbol_str: A string formatted in SBOL.
        :return: None
        """
        pass

    def writeString(self):
        """
        Convert data objects in this Document into textual SBOL.

        :return: A string representation of the objects in this Document.
        """
        pass

    def append(self, filename):
        """
        Read an RDF/XML file and attach the SBOL objects to this Document.

        New objects will be added to the existing contents of the Document.
        :param filename: The full name of the file you want to read (including file extension).
        :return: None
        """
        pass

    # Online validation #
    def request_validation(self, sbol_str):
        # TODO what is this method supposed to do?
        pass

    def request_comparison(self, diff_file):
        """
        Perform comparison on Documents using the online validation tool.

        This is for cross-validation of SBOL documents with libSBOLj. Document comparison can also be performed
        using the built-in compare method.
        :param diff_file:
        :return: The comparison results
        """
        pass

    def clear(self):
        """
        Delete all properties and objects in the Document.

        :return: None
        """
        pass

    def query_repository(self, command):
        """

        :param command:
        :return: str
        """
        # TODO better docstring
        pass

    def search_metadata(self, role, type, name, collection):
        """

        :param role:
        :param type:
        :param name:
        :param collection:
        :return: str
        """
        # TODO better docstring
        pass

    # TODO The commented-out methods below are important, but they rely heavily on raptor
    # static std::string string_from_raptor_term(raptor_term *term, bool addWrapper=false);
    #
    # /// Generates rdf/xml
    # void generate(raptor_world** world, raptor_serializer** sbol_serializer, char** sbol_buffer, size_t* sbol_buffer_len, raptor_iostream** ios, raptor_uri** base_uri);

    def serialize_rdfxml(self, out):
        """
        Serialize RDF XML.
        :param out: output stream
        :return: None
        """
        pass

    def validate(self):
        """
        Run validation on this Document via the online validation tool.

        :return: A string containing a message with the validation results
        """
        pass

    def size(self):
        """
        Get the total number of objects in the Document, including SBOL core object and custom annotation objects.

        :return: The total number of objects in the Document.
        """
        pass

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

    def cacheObjects(self):
        # TODO docstring
        pass

    def referenceNamespace(self, uri):
        """

        :param uri:
        :return: str
        """
        # TODO better docstring
        pass

    def summary(self):
        """
        Produce a string representation of the Document.

        :return: A string representation of the Document.
        """
        pass

    # TODO Port iterator, which loops over top-level items of Document

    def find(self, uri):
        """
        Search recursively for an SBOLObject in this Document that matches the uri.

        :param uri: The identity of the object to search for.
        :return: A pointer to the SBOLObject, or NULL if an object with this identity doesn't exist.
        """
        pass