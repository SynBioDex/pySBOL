from constants import *
from toplevel import *

class ComponentDefinition(TopLevel):
    """
    The ComponentDefinition class represents the structural entities of a biological design.

    The primary usage of this class is to represent structural entities with designed sequences, such as DNA, RNA,
    and proteins, but it can also be used to represent any other entity that is part of a design,
    such as small molecules, proteins, and complexes.
    """
    def __init__(self, uri="example", component_type=BIOPAX_DNA,
                            version=VERSION_STRING, rdf_type=SBOL_COMPONENT_DEFINITION):
        """Construct a ComponentDefinition.

        :param uri: A full URI including a scheme, namespace, and identifier.
        If SBOLCompliance configuration is enabled, then this argument is simply the displayId for
        the new object and a full URI will automatically be constructed.
        :param component_type: A BioPAX ontology term that indicates whether the ComponentDefinition
        is DNA, RNA, protein, or some other molecule type.
        :param version: An arbitrary version string. If SBOLCompliance is enabled, this should be
        a Maven version string of the form "major.minor.patch".
        :param rdf_type: The RDF type for an extension class derived from this one
        """
        super().__init__(rdf_type, uri, version)

    def assemble(self, components, assembly_standard="", doc=None):
        """Assembles ComponentDefinitions into an abstraction hierarchy.

        The resulting data structure is a partial design, still lacking a primary structure or explicit sequence.
        To form a primary structure out of the ComponentDefinitions, call linearize after calling assemble.
        To fully realize the target sequence, use Sequence::assemble().
        :param components: Either a list of URIs for the constituent ComponentDefinitions or
        a list of subcomponents. A list of displayIds is also acceptable if using SBOL-compliant URIs.
        :param assembly_standard: An optional argument such as IGEM_STANDARD_ASSEMBLY that affects
        how components are composed and the final target sequence.
        :param doc: The Document to which the assembled ComponentDefinitions will be added. If not set, then
        you must add this ComponentDefinition to a Document before calling this method.
        :return: None
        """
        raise NotImplementedError("Not yet implemented")

    def assemblePrimaryStructure(self, primary_structure, assembly_standard="", doc=None):
        """Assembles ComponentDefinition into a linear primary structure.

        The resulting data structure is a partial design, still lacking an explicit sequence.
        To fully realize the target sequence, use Sequence::assemble().
        :param primary_structure: Either a list of URIs for the constituent ComponentDefinitions or
        a list of subcomponents. A list of displayIds is also acceptable if using SBOL-compliant URIs.
        :param assembly_standard: An optional argument such as IGEM_STANDARD_ASSEMBLY that affects how
        components are composed and the final target sequence.
        :param doc: The Document to which the assembled ComponentDefinitions will be added. If not set, then
        you must add this ComponentDefinition to a Document before calling this method.
        :return: None
        """
        raise NotImplementedError("Not yet implemented")

    def compile(self):
        """Compiles an abstraction hierarchy of ComponentDefinitions into a nucleotide sequence.

        If no Sequence object is associated with this ComponentDefinition, one will be automatically instantiated
        :return: A string representing the nucleotide sequence for this ComponentDefinition.
        """
        raise NotImplementedError("Not yet implemented")

    def updateSequence(self, composite_sequence=""):
        """Assemble a parent ComponentDefinition's Sequence from its subcomponent Sequences.

        :param composite_sequence: A recursive parameter, use default value.
        :return: The assembled parent sequence.
        """
        raise NotImplementedError("Not yet implemented")

    def getInSequentialOrder(self):
        """Orders this ComponentDefinition's member Components into a linear arrangement based on Sequence Constraints.

        :return: Primary sequence structure.
        """
        raise NotImplementedError("Not yet implemented")

    def hasUpstreamComponent(self, current_component):
        """Checks if the specified Component has a Component upstream in linear arrangement on the DNA strand.

        Checks that the appropriate SequenceConstraint exists.
        :param current_component: A Component in this ComponentDefinition.
        :return: True if found, False if not
        """
        raise NotImplementedError("Not yet implemented")

    def getUpstreamComponent(self, current_component):
        """Get the upstream component.

        :param current_component: A Component in this ComponentDefinition.
        :return: The upstream component.
        """
        raise NotImplementedError("Not yet implemented")

    def hasDownstreamComponent(self, current_component):
        """Checks if the specified Component has a Component downstream in linear arrangement on the DNA strand.

        Checks that the appropriate SequenceConstraint exists.
        :param current_component: A Component in this ComponentDefinition.
        :return: True if found, False if not.
        """
        raise NotImplementedError("Not yet implemented")

    def getDownstreamComponent(self, current_component):
        """Get the downstream component.

        :param current_component: A Component in this ComponentDefinition.
        :return: The downstream component.
        """
        raise NotImplementedError("Not yet implemented")

    def getFirstComponent(self):
        """Gets the first Component in a linear sequence.

        :return: The first component in sequential order.
        """
        raise NotImplementedError("Not yet implemented")

    def getLastComponent(self):
        """Gets the last Component in a linear sequence.

        :return: The last component in sequential order.
        """
        raise NotImplementedError("Not yet implemented")

    def applyToComponentHierarchy(self, callback=None, user_data=None):
        """Perform an operation on every Component in a structurally-linked hierarchy of Components
        by applying a callback function.If no callback is specified, the default behavior is to return a list of
        each Component in the hierarchy.

        :param callback: The callback function to apply.
        :param user_data: Arbitrary user data which can be passed in and out of the callback as an argument.
        :return: A list of all Components in the hierarchy.
        """
        raise NotImplementedError("Not yet implemented")

    def getPrimaryStructure(self):
        """Get the primary sequence of a design in terms of its sequentially ordered Components.

        :return: Primary structure.
        """
        raise NotImplementedError("Not yet implemented")

    def insertDownstream(self, target, component_to_insert):
        """Insert a Component downstream of another in a primary sequence, shifting any
        adjacent Components downstream as well.

        :param target: The target Component will be upstream of the insert Component after this operation.
        :param component_to_insert: The insert Component is inserted downstream of the target Component.
        :return: None
        """
        raise NotImplementedError("Not yet implemented")

    def insertUpstream(self, target, component_to_insert):
        """Insert a Component upstream of another in a primary sequence, shifting any
        adjacent Components upstream as well.


        :param target: The target Component will be downstream of the insert Component after this operation.
        :param component_to_insert: The insert Component is inserted upstream of the target Component.
        :return:
        """
        raise NotImplementedError("Not yet implemented")

    def addUpstreamFlank(self, target, elements):
        """A useful method when building up SBOL representations of natural DNA sequences.

        For example, it is often necessary to specify components that are assumed to have no meaningful role
        in the design, but are nevertheless important to fill in regions of sequence. This method autoconstructs
        a ComponentDefinition and Sequence object to create an arbitrary flanking sequence around design Components.
        The new ComponentDefinition will have Sequence Ontology type of flanking_region or SO:0000239.
        :param target: The new flanking sequence will be placed upstream of the target.
        :param elements: The primary sequence elements will be assigned to the autoconstructed Sequence object.
        The encoding is inferred.
        :return: None
        """
        raise NotImplementedError("Not yet implemented")

    def addDownstreamFlank(self, target, elements):
        """A useful method when building up SBOL representations of natural DNA sequences.

        For example, it is often necessary to specify components that are assumed to have no meaningful role
        in the design, but are nevertheless important to fill in regions of sequence. This method autoconstructs
        a ComponentDefinition and Sequence object to create an arbitrary flanking sequence around design Components.
        The new ComponentDefinition will have Sequence Ontology type of flanking_sequence.
        :param target: The new flanking sequence will be placed downstream of the target.
        :param elements: The primary sequence elements will be assigned to the autoconstructed Sequence object.
        The encoding is inferred.
        :return: None
        """
        raise NotImplementedError("Not yet implemented")

    def isRegular(self, msg=None):
        """Use this diagnose an irregular design.

        Recursively checks if this ComponentDefinition defines a SequenceAnnotation and Range for every Sequence.
        Regularity is more stringent than completeness. A design must be complete to be regular.
        :param msg: An optional message for diagnosing the irregularity, if any is found.
        :return: True if the abstraction hierarchy is regular, False otherwise.
        """
        raise NotImplementedError("Not yet implemented")

    def isComplete(self, msg=None):
        """Use this diagnose an incomplete design.

        Recursively checks if this ComponentDefinition defines a SequenceAnnotation and Range for every Sequence.
        Completeness does not guarantee regularity.
        :param msg: An optional message for diagnosing the irregularity, if any is found.
        :return: True if the abstraction hierarchy is complete, False otherwise.
        """
        raise NotImplementedError("Not yet implemented")

    def disassemble(self, range_start=1):
        """Instantiates a Component for every SequenceAnnotation

         When converting from a flat GenBank file to a flat SBOL file, the result is a
         ComponentDefinition with SequenceAnnotations. This method will convert the flat SBOL file
         into hierarchical SBOL.

        :param range_start:
        :return: None
        """
        raise NotImplementedError("Not yet implemented")

    def linearize(self, components=None):
        """
        TODO document

        :param components: An optional list of component definitions or URIs. If None, an empty list of
        ComponentDefinitions is assumed.
        :return: None
        """
        raise NotImplementedError("Not yet implemented")

    def build(self):
        """
        TODO document

        :return: A ComponentDefinition.
        """

    def participate(self, species):
        """A convenience method that assigns a component to participate in a biochemical reaction.

        Behind the scenes, it auto-constructs a FunctionalComponent for this ComponentDefinition
        and assigns it to a Participation.

        :param species: A Participation object (ie, participant species in a biochemical Interaction).
        :return: None
        """
        raise NotImplementedError("Not yet implemented")

    def getTypeURI(self):
        return SBOL_COMPONENT_DEFINITION
