from enum import Enum
from .sbolerror import *
import os
import random

class FileFormats(Enum):
    JSON = 'json'
    NTRIPLES = 'ntriples'
    RDFXML = 'rdfxml'


class ConfigOptions(Enum):
    HOMESPACE = 'homespace'
    SBOL_COMPLIANT_URIS = 'sbol_compliant_uris'
    SBOL_TYPED_URIS = 'sbol_typed_uris'
    SERIALIZATION_FORMAT = 'serialization_format'
    VALIDATE = 'validate'
    VALIDATOR_URL = 'validator_url'
    LANGUAGE = 'language'
    TEST_EQUALITY = 'test_equality'
    CHECK_URI_COMPLIANCE = 'check_uri_compliance'
    CHECK_COMPLETENESS = 'check_completeness'
    CHECK_BEST_PRACTICES = 'check_best_practices'
    FAIL_ON_FIRST_ERROR = 'fail_on_first_error'
    PROVIDE_DETAILED_STACK_TRACE = 'provide_detailed_stack_trace'
    URI_PREFIX = 'uri_prefix'
    SUBSET_URI = 'subset_uri'
    VERSION = 'version'
    INSERT_TYPE = 'insert_type'
    MAIN_FILE_NAME = 'main_file_name'
    DIFF_FILE_NAME = 'diff_file_name'
    RETURN_FILE = 'return_file'
    VERBOSE = 'verbose'


options = {
    ConfigOptions.HOMESPACE.value: 'http://examples.org',
    ConfigOptions.SBOL_COMPLIANT_URIS.value: True,
    ConfigOptions.SBOL_TYPED_URIS.value: True,
    ConfigOptions.SERIALIZATION_FORMAT.value: 'sbol',
    ConfigOptions.VALIDATE.value: True,
    ConfigOptions.VALIDATOR_URL.value: 'http://www.async.ece.utah.edu/validate/',
    ConfigOptions.LANGUAGE.value: 'SBOL2',
    ConfigOptions.TEST_EQUALITY.value: False,
    ConfigOptions.CHECK_URI_COMPLIANCE.value: False,
    ConfigOptions.CHECK_COMPLETENESS.value: False,
    ConfigOptions.CHECK_BEST_PRACTICES.value: False,
    ConfigOptions.FAIL_ON_FIRST_ERROR.value: False,
    ConfigOptions.PROVIDE_DETAILED_STACK_TRACE.value: False,
    ConfigOptions.URI_PREFIX.value: '',
    ConfigOptions.SUBSET_URI.value: '',
    ConfigOptions.VERSION.value: '',
    ConfigOptions.INSERT_TYPE.value: False,
    ConfigOptions.MAIN_FILE_NAME.value: 'main file',
    ConfigOptions.DIFF_FILE_NAME.value: 'comparison file',
    ConfigOptions.RETURN_FILE.value: False,
    ConfigOptions.VERBOSE.value: False
}


valid_options = {
    ConfigOptions.SBOL_COMPLIANT_URIS.value: {True, False},
    ConfigOptions.SBOL_TYPED_URIS.value: {True, False},
    ConfigOptions.SERIALIZATION_FORMAT.value: {'sbol', 'rdfxml', 'json', 'ntriples'},
    ConfigOptions.VALIDATE.value: {True, False},
    ConfigOptions.LANGUAGE.value: {'SBOL2', 'FASTA', 'GenBank'},
    ConfigOptions.TEST_EQUALITY.value: {True, False},
    ConfigOptions.CHECK_URI_COMPLIANCE.value: {True, False},
    ConfigOptions.CHECK_COMPLETENESS.value: {True, False},
    ConfigOptions.CHECK_BEST_PRACTICES.value: {True, False},
    ConfigOptions.FAIL_ON_FIRST_ERROR.value: {True, False},
    ConfigOptions.PROVIDE_DETAILED_STACK_TRACE.value: {True, False},
    ConfigOptions.INSERT_TYPE.value: {True, False},
    ConfigOptions.RETURN_FILE.value: {True, False},
    ConfigOptions.VERBOSE.value: {True, False}
}


extension_namespaces = {}
# The authoritative namespace for the Document. Setting the home namespace is like signing a piece of paper.
home = None
# Flag indicating whether an object's type is included in SBOL-compliant URIs.
SBOLCompliantTypes = 1
catch_exceptions = 0
file_format = 'rdfxml'


class Config:
    """A class which contains global configuration variables for the libSBOL environment.

    Configuration variables are accessed through the setOptions and getOptions methods.
    """

    @staticmethod
    def setHomespace(ns):
        """Setting the Homespace has several advantages. It simplifies object creation and retrieval from Documents.
        In addition, it serves as a way for a user to claim ownership of new objects. Generally users will want to
        specify a Homespace that corresponds to their organization's web domain.
        :param ns: The namespace to use as the Homespace
        :return: None
        """
        options[ConfigOptions.HOMESPACE.value] = ns

    @staticmethod
    def getHomespace():
        """

        :return: The Homespace (a string representing the default namespace).
        """
        return options[ConfigOptions.HOMESPACE.value]

    @staticmethod
    def hasHomespace():
        """

        :return: True if Homespace is set, False otherwise.
        """
        homespace = ConfigOptions.HOMESPACE.value
        return homespace in options and options[homespace] is not None and options[homespace] != ""

    @staticmethod
    def setFileFormat(_file_format):
        """

        :param file_format: The file format to use.
        :return: None
        """
        global file_format  # must declare that we're assigning to a global variable
        if _file_format == FileFormats.JSON.value:
            file_format = FileFormats.JSON.value
        elif _file_format == FileFormats.NTRIPLES.value:
            file_format = FileFormats.NTRIPLES.value
        else:
            file_format = FileFormats.RDFXML.value

    @staticmethod
    def getFileFormat():
        """

        :return: The file format.
        """
        return file_format

    @staticmethod
    def setOption(option, val):
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
        if option in options:
            if option in valid_options:
                if val in valid_options[option]:
                    options[option] = val
                else:
                    raise SBOLError(SBOLErrorCode.SBOL_ERROR_INVALID_ARGUMENT,
                                    val + ' is not a valid value for this option. Valid options are ' +
                                    str(valid_options[option]))
            else:
                # Any argument is valid, eg. uriPrefix
                options[option] = val
        else:
            raise SBOLError(SBOLErrorCode.SBOL_ERROR_INVALID_ARGUMENT,
                            option + ' is not a valid configuration option for libSBOL')

    @staticmethod
    def getOption(option):
        """Get current option value for online validation and conversion

        :param option: The option key
        :return: The option value
        """
        if option in options:
            return options[option]
        else:
            raise SBOLError(SBOLErrorCode.SBOL_ERROR_INVALID_ARGUMENT,
                            str(option) + ' not a valid configuration option for libSBOL')


# Global methods
def setHomespace(ns):
    Config.setHomespace(ns)


def getHomespace():
    return Config.getHomespace()


def hasHomespace():
    return Config.hasHomespace()


def setFileFormat(file_format):
    Config.setFileFormat(file_format)


def getFileFormat():
    return Config.getFileFormat()


def constructCompliantURI(sbol_type, display_id, version):
    if Config.getOption(ConfigOptions.SBOL_COMPLIANT_URIS.value) is True:
        return getHomespace() + os.sep + parseClassName(sbol_type) + os.sep + display_id + os.sep + version
    else:
        return ''


def constructCompliantURI_parentChild(parent_type, child_type, display_id, version):
    if Config.getOption(ConfigOptions.SBOL_COMPLIANT_URIS.value) is True:
        return getHomespace() + os.sep + parseClassName(parent_type) + os.sep + parseClassName(child_type) + \
            os.sep + display_id + os.sep + version
    else:
        return ''


def randomIdentifier():
    # TODO test
    id = ''
    for i in range(1, 11):
        r = random.randint(0, 9)
        id += str(r)
        if r % 4 == 0 and r != 16:
            id += '-'
    return id


def autoconstructURI():
    if Config.getOption(ConfigOptions.SBOL_COMPLIANT_URIS) is False and hasHomespace():
        return getHomespace() + os.sep + randomIdentifier()
    elif Config.getOption(ConfigOptions.SBOL_COMPLIANT_URIS) is False and not hasHomespace():
        raise SBOLError('The autoconstructURI method requires a valid namespace authority. Use setHomespace().',
                        SBOLErrorCode.SBOL_ERROR_COMPLIANCE)
    else:
        raise SBOLError('The autoconstructURI method only works when SBOLCompliance flag is false. '
                        'Use setOption to disable SBOL-compliant URIs.', SBOLErrorCode.SBOL_ERROR_COMPLIANCE)


def getCompliantURI(uri_prefix, sbol_class_name, display_id, version):
    return uri_prefix + os.sep + sbol_class_name + os.sep + display_id + os.sep + version


def parseClassName(uri):
    if '#' in uri:
        return uri[uri.rindex('#')+1:]
    elif '/' in uri:
        return uri[uri.rindex('/')+1:]
    else:
        return ''


def parseNamespace(uri):
    if '#' in uri:
        return uri[:uri.rindex('#')]
    elif '/' in uri:
        return uri[:uri.rindex('/')]
    else:
        return ''


def parseURLDomain(url):
    return url.split('://')[1].split('/')[0]


def parsePropertyName(uri):
    return parseClassName(uri)
