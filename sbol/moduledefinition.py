from constants import *
from toplevel import *
from property import *


class ModuleDefinition(TopLevel):
    """ModuleDefinition is a principle top-level class for describing the function of a design."""

    # The roles property is an OPTIONAL set of URIs that clarifies the intended function of a ModuleDefinition.
    # These URIs might identify descriptive biological roles, such as "metabolic pathway" and "signaling cascade",
    # but they can also identify identify "logical" roles, such as "inverter" or "AND gate", or other abstract roles
    # for describing the function of design. Interpretation of the meaning of such roles currently depends
    # on the software tools that read and write them.
    roles = None

    # The modules property is OPTIONAL and MAY specify a set of Module objects contained by the ModuleDefinition.
    # While the ModuleDefinition class is analogous to a specification sheet for a system of interacting biological
    # elements, the Module class represents the occurrence of a particular subsystem within the system. Hence,
    # this class allows a system design to include multiple instances of a subsystem, all defined by reference
    # to the same ModuleDefinition. For example, consider the ModuleDefinition for a network of two-input
    # repressor devices in which the particular repressors have not been chosen yet. This ModuleDefinition
    # could contain multiple Module objects that refer to the same ModuleDefinition of an abstract two-input
    # repressor device. Note that the set of relations between Module and ModuleDefinition objects is strictly acyclic.
    modules = None

    # The interactions property is OPTIONAL and MAY specify a set of Interaction objects within the ModuleDefinition.
    # The Interaction class provides an abstract, machine-readable representation of entity behavior within a
    # ModuleDefinition. Each Interaction contains Participation objects that indicate the roles of the
    # FunctionalComponent objects involved in the Interaction.
    interactions = None

    # The functionalComponents property is OPTIONAL and MAY specify a set of FunctionalComponent objects contained by
    # the ModuleDefinition. Just as a Module represents an instance of a subsystem in the overall system represented by
    # a ModuleDefinition, a FunctionalComponent represents an instance of a structural entity (represented by a
    # ComponentDefinition) in the system. This concept allows a ModuleDefinition to assert different interactions
    # for separate copies of the same structural entity if needed. For example, a ModuleDefinition might contain
    # multiple FunctionalComponent objects that refer to the same promoter ComponentDefinition, but assert different
    # interactions for these promoter copies based on their separate positions in another ComponentDefinition that
    # represents the structure of the entire system.
    functionalComponents = None

    # The models property is OPTIONAL and MAY specify a set of URI references to Model objects.
    # Model objects are placeholders that link ModuleDefinition objects to computational models of any format.
    # A ModuleDefinition object can link to more than one Model since each might encode system behavior in
    # a different way or at a different level of detail.
    models = None

    def __init__(self, uri=URIRef("example"), version=VERSION_STRING, sbol_type_uri=SBOL_MODULE_DEFINITION):
        """Construct a ModuleDefinition

        :param uri: A full URI including a scheme, namespace, and identifier.
        If SBOLCompliance configuration is enabled, then this argument is simply the displayId
        for the new object and a full URI will automatically be constructed.
        :param version: An arbitrary version string. If SBOLCompliance is enabled,
        this should be a valid [Maven version string](http://maven.apache.org/).
        :param sbol_type_uri: The RDF type for an extension class derived from this one (optional)
        """
        super().__init__(sbol_type_uri, uri, version)
        roles = Property(self, SBOL_ROLES, '0', '*', None)

    def setOutput(self, output):
        """Defines an output for a sub-Module. Useful for top-down assembly of Modules and sub-Modules.

        If a FunctionalComponent with the given definition does not exist yet, one will be autoconstructed.
        Otherwise the FunctionalComponent with the given definition will be inferred. Be warned that this inference
        may fail if there is more than one FunctionalComponent with the same definition.

        :param output: A ComponentDefinition that defines the output
        :return: A FunctionalComponent that is derived from the argument ComponentDefinition and configured
        as this ModuleDefinition's output (it's direction property is set to SBOL_DIRECTION_OUT)
        """
        raise NotImplementedError("Not yet implemented")

    def setOutputFunctional(self, output):
        """Configures a FunctionalComponent as an output for a Module.

        Useful for bottom-up assembly of Modules and sub-Modules.

        :param output: The FunctionalComponent that will be configured
        :return: None
        """
        raise NotImplementedError("Not yet implemented")

    def setInput(self, input):
        """Defines an input for a sub-Module. Useful for top-down assembly of Modules and sub-Modules.

        If a FunctionalComponent with the given definition does not exist yet, one will be autoconstructed.
        Otherwise the FunctionalComponent with the given definition will be inferred. Be warned that this inference
        may fail if there is more than one FunctionalComponent with the same definition.

        :param input: A ComponentDefinition that defines the input.
        :return: A FunctionalComponent that is derived from the argument ComponentDefinition
        and configured as this ModuleDefinition's input (it's direction property is set to SBOL_DIRECTION_IN).
        """
        raise NotImplementedError("Not yet implemented")

    def setInputFunctional(self, input):
        """Configures a FunctionalComponent as an input for a Module.

        Useful for bottom-up assembly of Modules and sub-Modules.

        :param input: The FunctionalComponent that will be configured.
        :return: None
        """

    def connect(self, output, input):
        """Connects the output of a sub-Module with the input of another sub-Module. Auto-constructs MapsTo objects.

        :param output: A FunctionalComponent configured as a Module output (see setOutput).
        :param input: A FunctionalComponent configured as a Module input (see setInput).
        :return: None
        """
        raise NotImplementedError("Not yet implemented")

    def override(self, highlevel, lowlevel):
        """Overrides a low-level component in an abstract sub-Module with a high-level component
        in a parent ModuleDefinition, for example when overriding an abstract template Module with explicit components.

        :param highlevel: A high-level FunctionalComponent
        :param lowlevel: A low-level FunctionalComponent in a nested sub-Module
        :return: None
        """
        raise NotImplementedError("Not yet implemented")

    def applyToModuleHierarchy(self, callback=None, user_data=None):
        """Perform an operation on every ModuleDefinition in a structurally-linked hierarchy of ModuleDefinitions
        by applying a callback function. If no callback is specified, the default behavior is to return a
        list of each ModuleDefinition in the hierarchy.

        :param callback: A callback function
        :param user_data: Arbitrary user data which can be passed in and out of the callback as an argument.
        :return: A list of all ModuleDefinitions in the hierarchy.
        """
        raise NotImplementedError("Not yet implemented")

    def assemble(self, list_of_modules):
        """Assemble a high-level ModuleDefinition from lower-level submodules.

        Autoconstructs Module objects in the process.

        :param list_of_modules: A list of submodule ModuleDefinitions.
        :return: None
        """
        raise NotImplementedError("Not yet implemented")

    def getTypeURI(self):
        return SBOL_MODULE_DEFINITION

