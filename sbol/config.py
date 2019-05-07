class Config:
    """A class which contains global configuration variables for the libSBOL environment.

    Configuration variables are accessed through the setOptions and getOptions methods.
    """
    __options = {}
    __valid_options = {}
    __extension_namespaces = {}
    # The authoritative namespace for the Document. Setting the home namespace is like signing a piece of paper.
    __home = None
    # Flag indicating whether an object's type is included in SBOL-compliant URIs.
    __SBOLCompliantTypes = 1
    __catch_exceptions = 0
    __format = 'rdfxml'

    def setHomespace(self, ns):
        """Setting the Homespace has several advantages. It simplifies object creation and retrieval from Documents.
        In addition, it serves as a way for a user to claim ownership of new objects. Generally users will want to
        specify a Homespace that corresponds to their organization's web domain.
        :param ns: The namespace to use as the Homespace
        :return: None
        """
        raise NotImplementedError("Not yet implemented")

    def getHomespace(self):
        """

        :return: The Homespace (a string representing the default namespace).
        """
        raise NotImplementedError("Not yet implemented")

    def hasHomespace(self):
        """

        :return: True if Homespace is set, False otherwise.
        """
        raise NotImplementedError("Not yet implemented")

    def setFileFormat(self, file_format):
        """

        :param file_format: The file format to use.
        :return: None
        """
        raise NotImplementedError("Not yet implemented")

    def getFileFormat(self):
        """

        :return: The file format.
        """

    def setOption(self, option, val):
        """
        Configure options for libSBOL. Access online validation and conversion.

        | Option                       | Description                                                              | Values          |
        | :--------------------------- | :----------------------------------------------------------------------- | :-------------- |
        | homespace                    | Enable validation and conversion requests through the online validator   | http://examples.org |
        | sbol_compliant_uris          | Enables autoconstruction of SBOL-compliant URIs from displayIds          | True or False   |
        | sbol_typed_uris              | Include the SBOL type in SBOL-compliant URIs                             | True or False   |
        | output_format                | File format for serialization                                            | True or False   |
        | validate                     | Enable validation and conversion requests through the online validator   | True or False   |
        | validator_url                | The http request endpoint for validation                                 | A valid URL, set to<br>http://www.async.ece.utah.edu/sbol-validator/endpoint.php by default |
        | language                     | File format for conversion                                               | SBOL2, SBOL1, FASTA, GenBank |
        | test_equality                | Report differences between two files                                     | True or False |
        | check_uri_compliance         | If set to false, URIs in the file will not be checked for compliance<br>with the SBOL specification | True or False |
        | check_completeness           | If set to false, not all referenced objects must be described within<br>the given main_file | True or False |
        | check_best_practices         | If set to true, the file is checked for the best practice rules set<br>in the SBOL specification | True or False |
        | fail_on_first_error          | If set to true, the validator will fail at the first error               | True or False |
        | provide_detailed_stack_trace | If set to true (and failOnFirstError is true) the validator will<br>provide a stack trace for the first validation error | True or False |
        | uri_prefix                   | Required for conversion from FASTA and GenBank to SBOL1 or SBOL2,<br>used to generate URIs  | True or False |
        | version                      | Adds the version to all URIs and to the document                         | A valid Maven version string |
        | return_file                  | Whether or not to return the file contents as a string                   | True or False |
        :param option: The option key
        :param val: The option value (str or bool expected)
        :return: None
        """
        raise NotImplementedError("Not yet implemented")

    def getOption(self, option):
        """Get current option value for online validation and conversion

        :param option: The option key
        :return: The option value
        """
        raise NotImplementedError("Not yet implemented")


# Global methods
def setHomespace(ns):
    raise NotImplementedError("Not yet implemented")


def getHomespace(ns):
    raise NotImplementedError("Not yet implemented")


def hasHomespace():
    raise NotImplementedError("Not yet implemented")


def setFileFormat(file_format):
    raise NotImplementedError("Not yet implemented")


def getFileFormat():
    raise NotImplementedError("Not yet implemented")
