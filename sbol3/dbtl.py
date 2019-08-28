from .toplevel import *
from .constants import *
from .implementation import Implementation
from .experiment import ExperimentalData
from .collection import Collection


class Design(TopLevel):
    """This class represents a biological Design. A Design is a conceptual representation of a biological system
    that a synthetic biologist intends to build. A Design is the first object created in libSBOL's formalized
    Design-Build-Test-Analysis workflow."""

    def __init__(self, uri="example", version=VERSION_STRING, structure=None, function=None):
        """Constructs a new Design.

        :param uri: A full URI including a scheme, namespace, and identifier.
        If SBOLCompliance configuration is enabled, then this argument is simply the displayId
        for the new object and a full URI will automatically be constructed.
        :param version: An arbitrary version string. If SBOLCompliance is enabled, this should be
        a Maven version string of the form "major.minor.patch".
        :param structure: A ComponentDefinition representing the structural aspects of the Design.
        :param function: A ModuleDefiniition representing the functional aspects of the Design.
        """
        super().__init__(SYSBIO_DESIGN, uri, version)
        self.characterization = ReferencedObject(self, SYSBIO_URI + "#characterization", SYSBIO_ANALYSIS, '0', '*', [libsbol_rule_2])
        self.structure = OwnedObject(self, SBOL_COMPONENT_DEFINITION, '1', '1', [libsbol_rule_3], structure)
        self.function = OwnedObject(self, SBOL_MODULE_DEFINITION, '1', '1', [libsbol_rule_4], function)
        self._structure = ReferencedObject(self, SYSBIO_URI + "#_structure", SBOL_COMPONENT_DEFINITION, '1', '1', [], structure.identity)
        self._function = ReferencedObject(self, SYSBIO_URI + "#_function", SBOL_MODULE_DEFINITION, '1', '1', [], function.identity)


    def generateDesign(self, uri, agent=None, plan=None, usages=None):
        raise NotImplementedError("Not yet implemented")


class Build(Implementation):
    """A Build is a realization of a Design. For practical purposes, a Build can represent a biological clone,
    a plasmid, or other laboratory sample. For a given Design, there may be multiple Builds realized in the lab.
    A Build represents the second step in libSBOL's formalized Design-Build-Test-Analyze workflow."""

    def __init__(self, uri=URIRef('example'), version=VERSION_STRING, structure=None, behavior=None):
        super().__init__(uri, version)
        self.design = ReferencedObject(self, SYSBIO_URI + "#design", SYSBIO_DESIGN, '0', '1', [libsbol_rule_8])
        self.structure = OwnedObject(self, SBOL_COMPONENT_DEFINITION, '1', '1', [libsbol_rule_5], structure)
        self.behavior = OwnedObject(self, SBOL_MODULE_DEFINITION, '1', '1', [libsbol_rule_6], behavior)
        self._structure = ReferencedObject(self, SYSBIO_URI + "#_structure", SBOL_MODULE_DEFINITION, '1', '1', [], structure.identity)
        self._behavior = ReferencedObject(self, SBOL_URI + "#built", SBOL_MODULE_DEFINITION, '1', '1', [], behavior.identity)
        self._sysbio_type = URIProperty(self, SYSBIO_URI + "#type", '1', '1', [], SYSBIO_BUILD)

    @property
    def sysbio_type(self):
        return self._sysbio_type.value

    @sysbio_type.setter
    def sysbio_type(self, new_sysbio_type):
        self._sysbio_type.set(new_sysbio_type)


class Test(ExperimentalData):
    def __init__(self, uri=URIRef('example'), version=VERSION_STRING):
        super().__init__(uri, version)
        self.samples = ReferencedObject(self, SYSBIO_URI + "#samples", SBOL_IMPLEMENTATION, '0', '*', [libsbol_rule_9])
        self.dataFiles = ReferencedObject(self, SBOL_ATTACHMENTS, SBOL_ATTACHMENT, '0', '*', [])


class Analysis(TopLevel):
    def __init__(self, uri=URIRef('example'), version=VERSION_STRING):
        super().__init__(SYSBIO_ANALYSIS, uri, version)
        self.rawData = ReferencedObject(self, SYSBIO_URI + "#rawData", SBOL_EXPERIMENTAL_DATA, '0', '1', [libsbol_rule_10])
        self.dataFiles = ReferencedObject(self, SBOL_ATTACHMENTS, SBOL_ATTACHMENT, '0', '*', [])
        self.consensusSequence = OwnedObject(self, SYSBIO_URI + "#consensusSequence", '0', '1', [])
        self.fittedModel = OwnedObject(self, SYSBIO_URI + "#model", '0', '1', [])
        self.dataSheet = ReferencedObject(self, SYSBIO_URI + "#dataSheet", SBOL_ATTACHMENT, '0', '1', [])
        self._consensusSequence = OwnedObject(self, SYSBIO_URI + "#consensusSequence", SBOL_SEQUENCE, '0', '1', [])
        self._fittedModel = OwnedObject(self, SYSBIO_URI + "#model", SBOL_MODEL, '0', '1', [])

    def verifyTarget(self, consensus_sequence):
        raise NotImplementedError('Not yet implemented')

    def reportIdentity(self):
        raise NotImplementedError('Not yet implemented')

    def reportCoverage(self):
        raise NotImplementedError('Not yet implemented')

    def reportAmbiguity(self):
        raise NotImplementedError('Not yet implemented')

    def generate_analysis(self, uri, agent=None, plan=None, usages=None):
        raise NotImplementedError('Not yet implemented')


class SampleRoster(Collection):
    """A SampleRoster is a container used to group Builds that are included in an experiment together.

    A SampleRoster can be used to generate a Test in a Design-Build-Test-Learn workflow."""

    def __init__(self, uri=URIRef('example'), version=VERSION_STRING):
        super().__init__(uri, version)
        self.samples = ReferencedObject(self, SBOL_MEMBERS, SBOL_IMPLEMENTATION, '0', '*', [libsbol_rule_15])
        self._sysbio_type = URIProperty(self, SYSBIO_URI + "#type", '1', '1', [], SYSBIO_URI + "#SampleRoster")
        if Config.getOption(ConfigOptions.SBOL_COMPLIANT_URIS.value) is True:
            self.identity = URIRef(Config.getHomespace() + '/SampleRoster/' + self.displayId + '/' + version)
            self.persistentIdentity = URIRef(Config.getHomespace() + '/SampleRoster/' + self.displayId)

    @property
    def sysbio_type(self):
        return self._sysbio_type.value

    @sysbio_type.setter
    def sysbio_type(self, new_sysbio_type):
        self._sysbio_type.set(new_sysbio_type)


class AliasedProperty:
    # TODO
    pass


class TranscriptionRepressionInteraction:
    # TODO
    pass


class SmallMoleculeInhibitionInteraction:
    # TODO
    pass


class GeneProductionInteraction:
    # TODO
    pass


class TranscriptionalActivationInteraction:
    # TODO
    pass


class SmallMoleculeActivationInteraction:
    # TODO
    pass


class EnzymeCatalysisInteraction:
    # TODO
    pass
