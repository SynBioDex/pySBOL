from rdflib import URIRef

# All SBOL objects will be created in the default namespace, unless otherwise specified
DEFAULT_NS = URIRef("http://examples.org/")

# The URIs defined here determine the appearance of serialized RDF/XML nodes.
# Change these URIs to change the appearance of an SBOL class or property name
SBOL_URI = URIRef("http://sbols.org/v2")  #< Namespace for the SBOL standard.
RDF_URI = URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
PURL_URI = URIRef("http://purl.org/dc/terms/")
PROV_URI = URIRef("http://www.w3.org/ns/prov")
PROVO = URIRef("http://www.w3.org/ns/prov")
SYSBIO_URI = URIRef("http://sys-bio.org")
# PROVO = URIRef("https://www.w3.org/TR/prov-o/")

# rdf nodes used in SBOL
NODENAME_ABOUT = URIRef("rdf:about")
NODENAME_RESOURCE = URIRef("rdf:resource")

VERSION_STRING = "1"

# URIs for SBOL objects
SBOL_DOCUMENT = URIRef(SBOL_URI + "#Document")
SBOL_IDENTIFIED = URIRef(SBOL_URI + "#Identified")
SBOL_DOCUMENTED = URIRef(SBOL_URI + "#Documented")
SBOL_TOP_LEVEL = URIRef(SBOL_URI + "#TopLevel")
SBOL_GENERIC_TOP_LEVEL = URIRef(SBOL_URI + "#GenericTopLevel")
SBOL_SEQUENCE_ANNOTATION = URIRef(SBOL_URI + "#SequenceAnnotation")
SBOL_COMPONENT = URIRef(SBOL_URI + "#Component")
SBOL_FUNCTIONAL_COMPONENT = URIRef(SBOL_URI + "#FunctionalComponent")
SBOL_COMPONENT_DEFINITION = URIRef(SBOL_URI + "#ComponentDefinition")
SBOL_SEQUENCE = URIRef(SBOL_URI + "#Sequence")
SBOL_MODULE_DEFINITION = URIRef(SBOL_URI + "#ModuleDefinition")
SBOL_MODULE = URIRef(SBOL_URI + "#Module")
SBOL_MODEL = URIRef(SBOL_URI + "#Model")
SBOL_MAPS_TO = URIRef(SBOL_URI + "#MapsTo")
SBOL_INTERACTION = URIRef(SBOL_URI + "#Interaction")
SBOL_PARTICIPATION = URIRef(SBOL_URI + "#Participation")
SBOL_SEQUENCE_CONSTRAINT = URIRef(SBOL_URI + "#SequenceConstraint")
SBOL_LOCATION = URIRef(SBOL_URI + "#Location")
# SBOL_DOCUMENT = URIRef(SBOL_URI + "#Document")
SBOL_RANGE = URIRef(SBOL_URI + "#Range")
SBOL_CUT = URIRef(SBOL_URI + "#Cut")
SBOL_COLLECTION = URIRef(SBOL_URI + "#Collection")
SBOL_GENERIC_LOCATION = URIRef(SBOL_URI + "#GenericLocation")
SBOL_VARIABLE_COMPONENT = URIRef(SBOL_URI + "#VariableComponent")
SBOL_COMBINATORIAL_DERIVATION = URIRef(SBOL_URI + "#CombinatorialDerivation")
SBOL_ATTACHMENT = URIRef(SBOL_URI + "#Attachment")
SBOL_IMPLEMENTATION = URIRef(SBOL_URI + "#Implementation")
SBOL_EXPERIMENT = URIRef(SBOL_URI + "#Experiment")
SBOL_EXPERIMENTAL_DATA = URIRef(SBOL_URI + "#ExperimentalData")

UNDEFINED = URIRef(SBOL_URI + "#Undefined")

# URIs for SBOL Properties
SBOL_IDENTITY = URIRef(SBOL_URI + "#identity")
SBOL_PERSISTENT_IDENTITY = URIRef(SBOL_URI + "#persistentIdentity")
SBOL_VERSION = URIRef(SBOL_URI + "#version")
SBOL_DISPLAY_ID = URIRef(SBOL_URI + "#displayId")
SBOL_NAME = URIRef(PURL_URI + "title")
SBOL_DESCRIPTION = URIRef(PURL_URI + "description")
SBOL_TYPES = URIRef(SBOL_URI + "#type")
SBOL_START = URIRef(SBOL_URI + "#start")
SBOL_END = URIRef(SBOL_URI + "#end")
SBOL_SEQUENCE_ANNOTATIONS = URIRef(SBOL_URI + "#sequenceAnnotation")
SBOL_COMPONENTS = URIRef(SBOL_URI + "#component")
SBOL_COMPONENT_PROPERTY = URIRef(SBOL_URI + "#component")
SBOL_ROLES = URIRef(SBOL_URI + "#role")
SBOL_ELEMENTS = URIRef(SBOL_URI + "#elements")
SBOL_ENCODING = URIRef(SBOL_URI + "#encoding")
SBOL_SEQUENCE_PROPERTY = URIRef(SBOL_URI + "#sequence")
SBOL_WAS_DERIVED_FROM = URIRef(PROV_URI + "#wasDerivedFrom")
SBOL_DEFINITION = URIRef(SBOL_URI + "#definition")
SBOL_ACCESS = URIRef(SBOL_URI + "#access")
SBOL_DIRECTION = URIRef(SBOL_URI + "#direction")
SBOL_MODELS = URIRef(SBOL_URI + "#model")
SBOL_MODULES = URIRef(SBOL_URI + "#module")
SBOL_FUNCTIONAL_COMPONENTS = URIRef(SBOL_URI + "#functionalComponent")
SBOL_INTERACTIONS = URIRef(SBOL_URI + "#interaction")
SBOL_MAPS_TOS = URIRef(SBOL_URI + "#mapsTo")
SBOL_PARTICIPATIONS = URIRef(SBOL_URI + "#participation")
SBOL_PARTICIPANT = URIRef(SBOL_URI + "#participant")
SBOL_LOCAL = URIRef(SBOL_URI + "#local")
SBOL_REMOTE = URIRef(SBOL_URI + "#remote")
SBOL_REFINEMENT = URIRef(SBOL_URI + "#refinement")
SBOL_SOURCE = URIRef(SBOL_URI + "#source")
SBOL_LANGUAGE = URIRef(SBOL_URI + "#language")
SBOL_FRAMEWORK = URIRef(SBOL_URI + "#framework")
SBOL_SEQUENCE_CONSTRAINTS = URIRef(SBOL_URI + "#sequenceConstraint")
SBOL_SUBJECT = URIRef(SBOL_URI + "#subject")
SBOL_OBJECT = URIRef(SBOL_URI + "#object")
SBOL_RESTRICTION = URIRef(SBOL_URI + "#restriction")
SBOL_ORIENTATION = URIRef(SBOL_URI + "#orientation")
SBOL_LOCATIONS = URIRef(SBOL_URI + "#location")
SBOL_ROLE_INTEGRATION = URIRef(SBOL_URI + "#roleIntegration")
SBOL_MEMBERS = URIRef(SBOL_URI + "#member")
SBOL_AT = URIRef(SBOL_URI + "#at")
SBOL_OPERATOR = URIRef(SBOL_URI + "#operator")
SBOL_VARIABLE_COMPONENTS = URIRef(SBOL_URI + "#variableComponent")
SBOL_VARIABLE = URIRef(SBOL_URI + "#variable")
SBOL_VARIANTS = URIRef(SBOL_URI + "#variants")
SBOL_VARIANT_COLLECTIONS = URIRef(SBOL_URI + "#variantCollections")
SBOL_VARIANT_DERIVATIONS = URIRef(SBOL_URI + "#variantDeriviations")
SBOL_STRATEGY = URIRef(SBOL_URI + "#strategy")
SBOL_TEMPLATE = URIRef(SBOL_URI + "#template")
SBOL_ATTACHMENTS = URIRef(SBOL_URI + "#attachment")

# SBOL internal ontologies
SBOL_ACCESS_PRIVATE = URIRef(SBOL_URI + "#private")  # < Option for Component::access or FunctionalComponent::access property
SBOL_ACCESS_PUBLIC = URIRef(SBOL_URI + "#public")    # < Option for Component::access or FunctionalComponent::access property
SBOL_DIRECTION_IN = URIRef(SBOL_URI + "#in")         # < Option for FunctionalComponent::access property
SBOL_DIRECTION_OUT = URIRef(SBOL_URI + "#out")       # < Option for FunctionalComponent::direction property
SBOL_DIRECTION_IN_OUT = URIRef(SBOL_URI + "#inout")  # < Option for FunctionalComponent::direction property
SBOL_DIRECTION_NONE = URIRef(SBOL_URI + "#none")     # < Option for FunctionalComponent::direction property
SBOL_RESTRICTION_PRECEDES = URIRef(SBOL_URI + "#precedes")                     # < Option for SequenceConstraint::restriction property
SBOL_RESTRICTION_SAME_ORIENTATION_AS = URIRef("#sameOrientationAs")          # < Option for SequenceConstraint::restriction property
SBOL_RESTRICTION_OPPOSITE_ORIENTATION_AS = URIRef("#oppositeOrientationAs")  # < Option for SequenceConstraint::restriction property
SBOL_ENCODING_IUPAC = URIRef("http://www.chem.qmul.ac.uk/iubmb/misc/naseq.html")    # < Option for Sequence::encoding property
SBOL_ENCODING_IUPAC_PROTEIN = URIRef("http://www.chem.qmul.ac.uk/iupac/AminoAcid/") # < Option for Sequence::encoding property
SBOL_ENCODING_SMILES = URIRef("http://www.opensmiles.org/opensmiles.html")          # < Option for Sequence::encoding property
SBOL_ORIENTATION_INLINE = URIRef(SBOL_URI + "#inline")                        # < Option for Location::orientation property
SBOL_ORIENTATION_REVERSE_COMPLEMENT = URIRef(SBOL_URI + "#reverseComplement") # < Option for Location::orientation property
SBOL_REFINEMENT_USE_REMOTE = URIRef(SBOL_URI + "#useRemote") # < Option for FunctionalComponent::refinement property
SBOL_REFINEMENT_USE_LOCAL = URIRef(SBOL_URI + "#useLocal")   # < Option for FunctionalComponent::refinement property
SBOL_REFINEMENT_VERIFY_IDENTICAL = URIRef(SBOL_URI + "#verifyIdentical") # < Option for MapsTo::refinement property
SBOL_REFINEMENT_MERGE = URIRef(SBOL_URI + "#merge")                      # < Option for MapsTo::refinement property
SBOL_ROLE_INTEGRATION_MERGE = URIRef(SBOL_URI + "#mergeRoles")           # < Option for SequenceAnnotation::roleIntegration or Component::roleIntegration property
SBOL_ROLE_INTEGRATION_OVERRIDE = URIRef(SBOL_URI + "#overrideRoles")     # < Option for SequenceAnnotation::roleIntegration or Component::roleIntegration property
SBOL_DESIGN = URIRef(SBOL_URI + "#design")  # < Option for Usage::roles or Association::roles
SBOL_BUILD = URIRef(SBOL_URI + "#build")    # < Option for Usage::roles or Association::roles
SBOL_TEST = URIRef(SBOL_URI + "#test")  # < Option for Usage::roles or Association::roles
SBOL_LEARN = URIRef(SBOL_URI + "#learn")    # < Option for Usage::roles or Association::roles

# PROVO ontology
PROVO_ACTIVITY = URIRef(PROVO + "#Activity")
PROVO_USAGE = URIRef(PROVO + "#Usage")
PROVO_ASSOCIATION = URIRef(PROVO + "#Association")
PROVO_AGENT = URIRef(PROVO + "#Agent")
PROVO_PLAN = URIRef(PROVO + "#Plan")
PROVO_WAS_GENERATED_BY = URIRef(PROVO + "#wasGeneratedBy")
PROVO_STARTED_AT_TIME = URIRef(PROVO + "#startedAtTime")
PROVO_ENDED_AT_TIME = URIRef(PROVO + "#endedAtTime")
PROVO_QUALIFIED_ASSOCIATION = URIRef(PROVO + "#qualifiedAssociation")
PROVO_QUALIFIED_USAGE = URIRef(PROVO + "#qualifiedUsage")
PROVO_WAS_INFORMED_BY = URIRef(PROVO + "#wasInformedBy")
PROVO_HAD_PLAN = URIRef(PROVO + "#hadPlan")
PROVO_HAD_ROLE = URIRef(PROVO + "#hadRole")
PROVO_AGENT_PROPERTY = URIRef(PROVO + "#agent")
PROVO_ENTITY = URIRef(PROVO + "#entity")

# Systems Biology Ontology
# Interaction.types
SBO = URIRef("http://identifiers.org/biomodels.sbo/SBO:")  # < Namespace for Systems Biology Ontology (SBO) terms
SBO_INTERACTION = URIRef(SBO + "0000343")                  # < An SBO term and possible value for an Interaction::type property
SBO_INHIBITION = URIRef(SBO + "0000169")                   # < An SBO term and possible value for an Interaction::type property
SBO_GENETIC_PRODUCTION = URIRef(SBO + "0000589")           # < An SBO term and possible value for an Interaction::type property
SBO_NONCOVALENT_BINDING = URIRef(SBO + "0000177")          # < An SBO term and possible value for an Interaction::type property
SBO_STIMULATION = URIRef(SBO + "0000170")                  # < An SBO term and possible value for an Interaction::type property
SBO_DEGRADATION = URIRef(SBO + "0000179")                  # < An SBO term and possible value for an Interaction::type property
SBO_CONTROL = URIRef(SBO + "0000168")                      # < An SBO term and possible value for an Interaction::type property
SBO_BIOCHEMICAL_REACTION = URIRef(SBO + "0000176")         # < An SBO term and possible value for an Interaction::type property
SBO_STIMULATED = URIRef(SBO + "0000643")                   # < An SBO term and possible value for an Interaction::type property
SBO_CONVERSION = URIRef(SBO + "0000182")                   # < An SBO term and possible value for an Interaction::type property

# Participant.roles
SBO_PROMOTER = URIRef(SBO + "0000598")             # < An SBO term and possible value for an Participant::role property
SBO_GENE = URIRef(SBO + "0000243")                 # < An SBO term and possible value for an Participant::role property
SBO_INHIBITOR = URIRef(SBO + "0000020")            # < An SBO term and possible value for an Participant::role property
SBO_INHIBITED = URIRef(SBO + "0000642")            # < An SBO term and possible value for an Participant::role property
SBO_STIMULATOR = URIRef(SBO + "0000459")           # < An SBO term and possible value for an Participant::role property
SBO_REACTANT = URIRef(SBO + "0000010")             # < An SBO term and possible value for an Participant::role property
SBO_PRODUCT = URIRef(SBO + "0000011")              # < An SBO term and possible value for an Participant::role property
SBO_LIGAND = URIRef(SBO + "0000280")               # < An SBO term and possible value for an Participant::role property
SBO_NONCOVALENT_COMPLEX = URIRef(SBO + "0000253")  # < An SBO term and possible value for an Participant::role property
SBO_BINDING_SITE = URIRef(SBO + "0000494")         # < An SBO term and possible value for an Participant::role property
SBO_SUBSTRATE = URIRef(SBO + "0000015")
SBO_COFACTOR = URIRef(SBO + "0000604")
SBO_SIDEPRODUCT = URIRef(SBO + "0000603")
# SBO_PRODUCT = URIRef(SBO + "0000011")
SBO_ENZYME = URIRef(SBO + "0000014")

# URIs for common Sequence Ontology terms
SO = URIRef("http://identifiers.org/so/SO:")  # < Namespace for Sequence Ontology (SO) terms
SO_MISC = URIRef(SO + "0000001")              # < An SO term and possible value for ComponentDefinition::role property
SO_GENE = URIRef(SO + "0000704")              # < An SO term and possible value for ComponentDefinition::role property
SO_PROMOTER = URIRef(SO + "0000167")          # < An SO term and possible value for ComponentDefinition::role property
SO_CDS = URIRef(SO + "0000316")               # < An SO term and possible value for ComponentDefinition::role property
SO_RBS = URIRef(SO + "0000139")               # < An SO term and possible value for ComponentDefinition::role property
SO_TERMINATOR = URIRef(SO + "0000141")        # < An SO term and possible value for ComponentDefinition::role property
SO_SGRNA = URIRef(SO + "0001998")             # < An SO term and possible value for ComponentDefinition::role property
SO_LINEAR = URIRef(SO + "0000987")            # < An SO term and possible value for ComponentDefinition::role property
SO_CIRCULAR = URIRef(SO + "0000988")          # < An SO term and possible value for ComponentDefinition::role property
SO_PLASMID = URIRef(SO + "0000155")           # < An SO term and possible value for ComponentDefinition::role property

# BioPAX is used to indicate macromolecular and molecular types
# DNA
BIOPAX_DNA = URIRef("http://www.biopax.org/release/biopax-level3.owl#DnaRegion")  # < A BioPax term and possible value for ComponentDefinition::type property
# RNA
BIOPAX_RNA = URIRef("http://www.biopax.org/release/biopax-level3.owl#RnaRegion")  # < A BioPax term and possible value for ComponentDefinition::type property
# PROTEIN
BIOPAX_PROTEIN = URIRef("http://www.biopax.org/release/biopax-level3.owl#Protein")  # < A BioPax term and possible value for ComponentDefinition::type property
# SMALL_MOLECULE
BIOPAX_SMALL_MOLECULE = URIRef("http://www.biopax.org/release/biopax-level3.owl#SmallMolecule")  # < A BioPax term and possible value for ComponentDefinition::type property
# COMPLEX
BIOPAX_COMPLEX = URIRef("http://www.biopax.org/release/biopax-level3.owl#Complex")  # < A BioPax term and possible value for ComponentDefinition::type property

# EDAM ontology is used for Model.languages
EDAM_SBML = URIRef("http://identifiers.org/edam/format_2585")    # < An EDAM ontology term and option for Model::language
EDAM_CELLML = URIRef("http://identifiers.org/edam/format_3240")  # < An EDAM ontology term and option for Model::language
EDAM_BIOPAX = URIRef("http://identifiers.org/edam/format_3156")  # < An EDAM ontology term and option for Model::language

# Model.frameworks
SBO_CONTINUOUS = URIRef(SBO + "0000062")  # < SBO term and option for Model::framework
SBO_DISCRETE = URIRef(SBO + "0000063")    # < SBO term and option for Model::framework

# URIs for SBOL extension objects
SYSBIO_DESIGN = URIRef(SYSBIO_URI + "#Design")
SYSBIO_BUILD = URIRef(SYSBIO_URI + "#Build")
SYSBIO_TEST = URIRef(SYSBIO_URI + "#Test")
SYSBIO_ANALYSIS = URIRef(SYSBIO_URI + "#Analysis")
SYSBIO_SAMPLE_ROSTER = URIRef(SYSBIO_URI + "#SampleRoster")

IGEM_URI = URIRef("http://wiki.synbiohub.org/wiki/Terms/igem")
IGEM_STANDARD_ASSEMBLY = URIRef(IGEM_URI + "#assembly/RFC10")
