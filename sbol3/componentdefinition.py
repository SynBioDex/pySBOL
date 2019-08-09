from .constants import *
from .toplevel import *
from . import validation
from .property import URIProperty

class ComponentDefinition(TopLevel):
    """
    The ComponentDefinition class represents the structural entities of a biological design.

    The primary usage of this class is to represent structural entities with designed sequences, such as DNA, RNA,
    and proteins, but it can also be used to represent any other entity that is part of a design,
    such as small molecules, proteins, and complexes.
    """

    # The types property is a REQUIRED set of URIs that specifies the category of biochemical or physical entity
    # (for example DNA, protein, or small molecule) that a ComponentDefinition object abstracts for the purpose of
    # engineering design.  The types property of every ComponentDefinition MUST contain one or more URIs that MUST
    # identify terms from appropriate ontologies, such as the BioPAX ontology or the ontology of Chemical Entities
    # of Biological Interest. See the table below for examples.
    # | Type              | URI for BioPAX Term                                           | LibSBOL symbol        |
    # | :---------------- | :------------------------------------------------------------ | :-------------------- |
    # | DNA               | http://www.biopax.org/release/biopax-level3.owl#DnaRegion     | BIOPAX_DNA            |
    # | RNA               | http://www.biopax.org/release/biopax-level3.owl#RnaRegion     | BIOPAX_RNA            |
    # | Protein           | http://www.biopax.org/release/biopax-level3.owl#Protein       | BIOPAX_PROTEIN        |
    # | Small Molecule    | http://www.biopax.org/release/biopax-level3.owl#SmallMolecule | BIOPAX_SMALL_MOLECULE |
    # | Complex           | http://www.biopax.org/release/biopax-level3.owl#Complex       | BIOPAX_COMPLEX        |
    _types = None # URIProperty

    # The roles property is an OPTIONAL set of URIs that clarifies the potential function of the entity represented
    # by a ComponentDefinition in a biochemical or physical context. The roles property of a ComponentDefinition MAY
    # contain one or more URIs that MUST identify terms from ontologies that are consistent with the types property
    # of the ComponentDefinition. For example, the roles property of a DNA or RNA ComponentDefinition could contain
    # URIs identifying terms from the Sequence Ontology (SO).  See the table below for common examples
    # | Role              | URI for Sequence Ontology Term            | LibSBOL symbol    |
    # | :---------------- | :---------------------------------------- | :---------------- |
    # | Miscellaneous     | http://identifiers.org/so/SO:0000001      | SO_MISC           |
    # | Promoter          | http://identifiers.org/so/SO:0000167      | SO_PROMOTER       |
    # | RBS               | http://identifiers.org/so/SO:0000139      | SO_RBS            |
    # | CDS               | http://identifiers.org/so/SO:0000316      | SO_CDS            |
    # | Terminator        | http://identifiers.org/so/SO:0000141      | SO_TERMINATOR     |
    # | Gene              | http://identifiers.org/so/SO:0000704      |                   |
    # | Operator          | http://identifiers.org/so/SO:0000057      |                   |
    # | Engineered Gene   | http://identifiers.org/so/SO:0000280      |                   |
    # | mRNA              | http://identifiers.org/so/SO:0000234      |                   |
    # | Effector          | http://identifiers.org/chebi/CHEBI:35224  |                   |
    _roles = None # URIProperty

    # The components property is OPTIONAL and MAY specify a set of Component objects that are contained by the
    # ComponentDefinition. The components properties of ComponentDefinition objects can be used to construct a
    # hierarchy of Component and ComponentDefinition objects. If a ComponentDefinition in such a hierarchy refers to
    # one or more Sequence objects, and there exist ComponentDefinition objects lower in the hierarchy that refer to
    # Sequence objects with the same encoding, then the elements properties of these Sequence objects SHOULD be
    # consistent with each other, such that well-defined mappings exist from the "lower level" elements to the
    # "higher level" elements. This mapping is also subject to any restrictions on the positions of the Component
    # objects in the hierarchy that are imposed by the SequenceAnnotation or SequenceConstraint objects contained
    # by the ComponentDefinition objects in the hierarchy.  The set of relations between Component and
    # ComponentDefinition objects is strictly acyclic.
    components = None  # OwnedObject<Component>

    sequences = None  # ReferencedObject

    sequence = None  # OwnedObject<Sequence>

    sequenceAnnotations = None  # OwnedObject<SequenceAnnotation>

    sequenceConstraints = None  # OwnedObject<SequenceConstraint>

    def __init__(self, uri=URIRef("example"), component_type=BIOPAX_DNA,
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
        self._types = URIProperty(self, SBOL_TYPES, '1', '*', None, component_type)
        self._roles = URIProperty(self, SBOL_ROLES, '0', '*', None)
        self.sequence = OwnedObject(self, SBOL_SEQUENCE, '0', '1', [validation.libsbol_rule_20])
        self.sequences = ReferencedObject(self, SBOL_SEQUENCE_PROPERTY, SBOL_SEQUENCE, '0', '*', [validation.libsbol_rule_21])
        self.sequenceAnnotations = OwnedObject(self, SBOL_SEQUENCE_ANNOTATIONS, '0', '*', None)
        self.components = OwnedObject(self, SBOL_COMPONENTS, '0', '*', None)
        self.sequenceConstraints = OwnedObject(self, SBOL_SEQUENCE_CONSTRAINTS, '0', '*', None)

    @property
    def types(self):
        return self._types.value

    @types.setter
    def types(self, new_types):
        self._types.set(new_types) # perform validation prior to setting the value of the types property

    @property
    def roles(self):
        return self._roles.value

    @roles.setter
    def roles(self, new_roles):
        self._roles.set(new_roles)

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
        raise NotImplementedError("Not yet implemented")

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
