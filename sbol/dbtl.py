from toplevel import *
from constants import *


class Design(TopLevel):
    """This class represents a biological Design. A Design is a conceptual representation of a biological system
    that a synthetic biologist intends to build. A Design is the first object created in libSBOL's formalized
    Design-Build-Test-Analysis workflow."""

    structure = None
    function = None
    characterization = None

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

    def generateDesign(self, uri, agent=None, plan=None, usages=None):
        raise NotImplementedError("Not yet implemented")


class Build:
    # TODO
    pass


class Test:
    # TODO
    pass


class Analysis:
    # TODO
    pass


class SampleRoster:
    # TODO
    pass


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
