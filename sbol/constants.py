# All SBOL objects will be created in the default namespace, unless otherwise specified
DEFAULT_NS = "http://examples.org/"

# The URIs defined here determine the appearance of serialized RDF/XML nodes.
# Change these URIs to change the appearance of an SBOL class or property name
SBOL_URI = "http://sbols.org/v2"  #< Namespace for the SBOL standard.
RDF_URI = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
PURL_URI = "http://purl.org/dc/terms/"
PROV_URI = "http://www.w3.org/ns/prov"
PROVO = "http://www.w3.org/ns/prov"
SYSBIO_URI = "http://sys-bio.org"
# PROVO = "https://www.w3.org/TR/prov-o/"

# rdf nodes used in SBOL
NODENAME_ABOUT = "rdf:about"
NODENAME_RESOURCE = "rdf:resource"

VERSION_STRING = "1"

# URIs for SBOL objects
SBOL_DOCUMENT = SBOL_URI + "#Document"
SBOL_IDENTIFIED = SBOL_URI + "#Identified"
SBOL_DOCUMENTED = SBOL_URI + "#Documented"
SBOL_TOP_LEVEL = SBOL_URI + "#TopLevel"
SBOL_GENERIC_TOP_LEVEL = SBOL_URI + "#GenericTopLevel"
SBOL_SEQUENCE_ANNOTATION = SBOL_URI + "#SequenceAnnotation"
SBOL_COMPONENT = SBOL_URI + "#Component"
SBOL_FUNCTIONAL_COMPONENT = SBOL_URI + "#FunctionalComponent"
SBOL_COMPONENT_DEFINITION = SBOL_URI + "#ComponentDefinition"
SBOL_SEQUENCE = SBOL_URI + "#Sequence"
SBOL_MODULE_DEFINITION = SBOL_URI + "#ModuleDefinition"
SBOL_MODULE = SBOL_URI + "#Module"
SBOL_MODEL = SBOL_URI + "#Model"
SBOL_MAPS_TO = SBOL_URI + "#MapsTo"
SBOL_INTERACTION = SBOL_URI + "#Interaction"
SBOL_PARTICIPATION = SBOL_URI + "#Participation"
SBOL_SEQUENCE_CONSTRAINT = SBOL_URI + "#SequenceConstraint"
SBOL_LOCATION = SBOL_URI + "#Location"
# SBOL_DOCUMENT = SBOL_URI + "#Document"
SBOL_RANGE = SBOL_URI + "#Range"
SBOL_CUT = SBOL_URI + "#Cut"
SBOL_COLLECTION = SBOL_URI + "#Collection"
SBOL_GENERIC_LOCATION = SBOL_URI + "#GenericLocation"
SBOL_VARIABLE_COMPONENT = SBOL_URI + "#VariableComponent"
SBOL_COMBINATORIAL_DERIVATION = SBOL_URI + "#CombinatorialDerivation"
SBOL_ATTACHMENT = SBOL_URI + "#Attachment"
SBOL_IMPLEMENTATION = SBOL_URI + "#Implementation"
SBOL_EXPERIMENT = SBOL_URI + "#Experiment"
SBOL_EXPERIMENTAL_DATA = SBOL_URI + "#ExperimentalData"

UNDEFINED = SBOL_URI + "#Undefined"

# URIs for SBOL Properties
SBOL_IDENTITY = SBOL_URI + "#identity"
SBOL_PERSISTENT_IDENTITY = SBOL_URI + "#persistentIdentity"
SBOL_VERSION = SBOL_URI + "#version"
SBOL_DISPLAY_ID = SBOL_URI + "#displayId"
SBOL_NAME = PURL_URI + "title"
SBOL_DESCRIPTION = PURL_URI + "description"
SBOL_TYPES = SBOL_URI + "#type"
SBOL_START = SBOL_URI + "#start"
SBOL_END = SBOL_URI + "#end"
SBOL_SEQUENCE_ANNOTATIONS = SBOL_URI + "#sequenceAnnotation"
SBOL_COMPONENTS = SBOL_URI + "#component"
SBOL_COMPONENT_PROPERTY = SBOL_URI + "#component"
SBOL_ROLES = SBOL_URI + "#role"
SBOL_ELEMENTS = SBOL_URI + "#elements"
SBOL_ENCODING = SBOL_URI + "#encoding"
SBOL_SEQUENCE_PROPERTY = SBOL_URI + "#sequence"
SBOL_WAS_DERIVED_FROM = PROV_URI + "#wasDerivedFrom"
SBOL_DEFINITION = SBOL_URI + "#definition"
SBOL_ACCESS = SBOL_URI + "#access"
SBOL_DIRECTION = SBOL_URI + "#direction"
SBOL_MODELS = SBOL_URI + "#model"
SBOL_MODULES = SBOL_URI + "#module"
SBOL_FUNCTIONAL_COMPONENTS = SBOL_URI + "#functionalComponent"
SBOL_INTERACTIONS = SBOL_URI + "#interaction"
SBOL_MAPS_TOS = SBOL_URI + "#mapsTo"
SBOL_PARTICIPATIONS = SBOL_URI + "#participation"
SBOL_PARTICIPANT = SBOL_URI + "#participant"
SBOL_LOCAL = SBOL_URI + "#local"
SBOL_REMOTE = SBOL_URI + "#remote"
SBOL_REFINEMENT = SBOL_URI + "#refinement"
SBOL_SOURCE = SBOL_URI + "#source"
SBOL_LANGUAGE = SBOL_URI + "#language"
SBOL_FRAMEWORK = SBOL_URI + "#framework"
SBOL_SEQUENCE_CONSTRAINTS = SBOL_URI + "#sequenceConstraint"
SBOL_SUBJECT = SBOL_URI + "#subject"
SBOL_OBJECT = SBOL_URI + "#object"
SBOL_RESTRICTION = SBOL_URI + "#restriction"
SBOL_ORIENTATION = SBOL_URI + "#orientation"
SBOL_LOCATIONS = SBOL_URI + "#location"
SBOL_ROLE_INTEGRATION = SBOL_URI + "#roleIntegration"
SBOL_MEMBERS = SBOL_URI + "#member"
SBOL_AT = SBOL_URI + "#at"
SBOL_OPERATOR = SBOL_URI + "#operator"
SBOL_VARIABLE_COMPONENTS = SBOL_URI + "#variableComponent"
SBOL_VARIABLE = SBOL_URI + "#variable"
SBOL_VARIANTS = SBOL_URI + "#variants"
SBOL_VARIANT_COLLECTIONS = SBOL_URI + "#variantCollections"
SBOL_VARIANT_DERIVATIONS = SBOL_URI + "#variantDeriviations"
SBOL_STRATEGY = SBOL_URI + "#strategy"
SBOL_TEMPLATE = SBOL_URI + "#template"
SBOL_ATTACHMENTS = SBOL_URI + "#attachment"

# SBOL internal ontologies
SBOL_ACCESS_PRIVATE = SBOL_URI + "#private"  # < Option for Component::access or FunctionalComponent::access property
SBOL_ACCESS_PUBLIC = SBOL_URI + "#public"    # < Option for Component::access or FunctionalComponent::access property
SBOL_DIRECTION_IN = SBOL_URI + "#in"         # < Option for FunctionalComponent::access property
SBOL_DIRECTION_OUT = SBOL_URI + "#out"       # < Option for FunctionalComponent::direction property
SBOL_DIRECTION_IN_OUT = SBOL_URI + "#inout"  # < Option for FunctionalComponent::direction property
SBOL_DIRECTION_NONE = SBOL_URI + "#none"     # < Option for FunctionalComponent::direction property
SBOL_RESTRICTION_PRECEDES = SBOL_URI + "#precedes"                     # < Option for SequenceConstraint::restriction property
SBOL_RESTRICTION_SAME_ORIENTATION_AS = "#sameOrientationAs"          # < Option for SequenceConstraint::restriction property
SBOL_RESTRICTION_OPPOSITE_ORIENTATION_AS = "#oppositeOrientationAs"  # < Option for SequenceConstraint::restriction property
SBOL_ENCODING_IUPAC = "http://www.chem.qmul.ac.uk/iubmb/misc/naseq.html"    # < Option for Sequence::encoding property
SBOL_ENCODING_IUPAC_PROTEIN = "http://www.chem.qmul.ac.uk/iupac/AminoAcid/" # < Option for Sequence::encoding property
SBOL_ENCODING_SMILES = "http://www.opensmiles.org/opensmiles.html"          # < Option for Sequence::encoding property
SBOL_ORIENTATION_INLINE = SBOL_URI + "#inline"                        # < Option for Location::orientation property
SBOL_ORIENTATION_REVERSE_COMPLEMENT = SBOL_URI + "#reverseComplement" # < Option for Location::orientation property
SBOL_REFINEMENT_USE_REMOTE = SBOL_URI + "#useRemote" # < Option for FunctionalComponent::refinement property
SBOL_REFINEMENT_USE_LOCAL = SBOL_URI + "#useLocal"   # < Option for FunctionalComponent::refinement property
SBOL_REFINEMENT_VERIFY_IDENTICAL = SBOL_URI + "#verifyIdentical" # < Option for MapsTo::refinement property
SBOL_REFINEMENT_MERGE = SBOL_URI + "#merge"                      # < Option for MapsTo::refinement property
SBOL_ROLE_INTEGRATION_MERGE = SBOL_URI + "#mergeRoles"           # < Option for SequenceAnnotation::roleIntegration or Component::roleIntegration property
SBOL_ROLE_INTEGRATION_OVERRIDE = SBOL_URI + "#overrideRoles"     # < Option for SequenceAnnotation::roleIntegration or Component::roleIntegration property
SBOL_DESIGN = SBOL_URI + "#design"  # < Option for Usage::roles or Association::roles
SBOL_BUILD = SBOL_URI + "#build"    # < Option for Usage::roles or Association::roles
SBOL_TEST = SBOL_URI + "#test"  # < Option for Usage::roles or Association::roles
SBOL_LEARN = SBOL_URI + "#learn"    # < Option for Usage::roles or Association::roles

# PROVO ontology
PROVO_ACTIVITY = PROVO + "#Activity"
PROVO_USAGE = PROVO + "#Usage"
PROVO_ASSOCIATION = PROVO + "#Association"
PROVO_AGENT = PROVO + "#Agent"
PROVO_PLAN = PROVO + "#Plan"
PROVO_WAS_GENERATED_BY = PROVO + "#wasGeneratedBy"
PROVO_STARTED_AT_TIME = PROVO + "#startedAtTime"
PROVO_ENDED_AT_TIME = PROVO + "#endedAtTime"
PROVO_QUALIFIED_ASSOCIATION = PROVO + "#qualifiedAssociation"
PROVO_QUALIFIED_USAGE = PROVO + "#qualifiedUsage"
PROVO_WAS_INFORMED_BY = PROVO + "#wasInformedBy"
PROVO_HAD_PLAN = PROVO + "#hadPlan"
PROVO_HAD_ROLE = PROVO + "#hadRole"
PROVO_AGENT_PROPERTY = PROVO + "#agent"
PROVO_ENTITY = PROVO + "#entity"

# Systems Biology Ontology
# Interaction.types
SBO = "http://identifiers.org/biomodels.sbo/SBO:"  # < Namespace for Systems Biology Ontology (SBO) terms
SBO_INTERACTION = SBO + "0000343"                  # < An SBO term and possible value for an Interaction::type property
SBO_INHIBITION = SBO + "0000169"                   # < An SBO term and possible value for an Interaction::type property
SBO_GENETIC_PRODUCTION = SBO + "0000589"           # < An SBO term and possible value for an Interaction::type property
SBO_NONCOVALENT_BINDING = SBO + "0000177"          # < An SBO term and possible value for an Interaction::type property
SBO_STIMULATION = SBO + "0000170"                  # < An SBO term and possible value for an Interaction::type property
SBO_DEGRADATION = SBO + "0000179"                  # < An SBO term and possible value for an Interaction::type property
SBO_CONTROL = SBO + "0000168"                      # < An SBO term and possible value for an Interaction::type property
SBO_BIOCHEMICAL_REACTION = SBO + "0000176"         # < An SBO term and possible value for an Interaction::type property
SBO_STIMULATED = SBO + "0000643"                   # < An SBO term and possible value for an Interaction::type property
SBO_CONVERSION = SBO + "0000182"                   # < An SBO term and possible value for an Interaction::type property

# Participant.roles
SBO_PROMOTER = SBO + "0000598"             # < An SBO term and possible value for an Participant::role property
SBO_GENE = SBO + "0000243"                 # < An SBO term and possible value for an Participant::role property
SBO_INHIBITOR = SBO + "0000020"            # < An SBO term and possible value for an Participant::role property
SBO_INHIBITED = SBO + "0000642"            # < An SBO term and possible value for an Participant::role property
SBO_STIMULATOR = SBO + "0000459"           # < An SBO term and possible value for an Participant::role property
SBO_REACTANT = SBO + "0000010"             # < An SBO term and possible value for an Participant::role property
SBO_PRODUCT = SBO + "0000011"              # < An SBO term and possible value for an Participant::role property
SBO_LIGAND = SBO + "0000280"               # < An SBO term and possible value for an Participant::role property
SBO_NONCOVALENT_COMPLEX = SBO + "0000253"  # < An SBO term and possible value for an Participant::role property
SBO_BINDING_SITE = SBO + "0000494"         # < An SBO term and possible value for an Participant::role property
SBO_SUBSTRATE = SBO + "0000015"
SBO_COFACTOR = SBO + "0000604"
SBO_SIDEPRODUCT = SBO + "0000603"
# SBO_PRODUCT = SBO + "0000011"
SBO_ENZYME = SBO + "0000014"

# URIs for common Sequence Ontology terms
SO = "http://identifiers.org/so/SO:"  # < Namespace for Sequence Ontology (SO) terms
SO_MISC = SO + "0000001"              # < An SO term and possible value for ComponentDefinition::role property
SO_GENE = SO + "0000704"              # < An SO term and possible value for ComponentDefinition::role property
SO_PROMOTER = SO + "0000167"          # < An SO term and possible value for ComponentDefinition::role property
SO_CDS = SO + "0000316"               # < An SO term and possible value for ComponentDefinition::role property
SO_RBS = SO + "0000139"               # < An SO term and possible value for ComponentDefinition::role property
SO_TERMINATOR = SO + "0000141"        # < An SO term and possible value for ComponentDefinition::role property
SO_SGRNA = SO + "0001998"             # < An SO term and possible value for ComponentDefinition::role property
SO_LINEAR = SO + "0000987"            # < An SO term and possible value for ComponentDefinition::role property
SO_CIRCULAR = SO + "0000988"          # < An SO term and possible value for ComponentDefinition::role property
SO_PLASMID = SO + "0000155"           # < An SO term and possible value for ComponentDefinition::role property

# BioPAX is used to indicate macromolecular and molecular types
# DNA
BIOPAX_DNA = "http://www.biopax.org/release/biopax-level3.owl#DnaRegion"  # < A BioPax term and possible value for ComponentDefinition::type property
# RNA
BIOPAX_RNA = "http://www.biopax.org/release/biopax-level3.owl#RnaRegion"  # < A BioPax term and possible value for ComponentDefinition::type property
# PROTEIN
BIOPAX_PROTEIN = "http://www.biopax.org/release/biopax-level3.owl#Protein"  # < A BioPax term and possible value for ComponentDefinition::type property
# SMALL_MOLECULE
BIOPAX_SMALL_MOLECULE = "http://www.biopax.org/release/biopax-level3.owl#SmallMolecule"  # < A BioPax term and possible value for ComponentDefinition::type property
# COMPLEX
BIOPAX_COMPLEX = "http://www.biopax.org/release/biopax-level3.owl#Complex"  # < A BioPax term and possible value for ComponentDefinition::type property

# EDAM ontology is used for Model.languages
EDAM_SBML = "http://identifiers.org/edam/format_2585"    # < An EDAM ontology term and option for Model::language
EDAM_CELLML = "http://identifiers.org/edam/format_3240"  # < An EDAM ontology term and option for Model::language
EDAM_BIOPAX = "http://identifiers.org/edam/format_3156"  # < An EDAM ontology term and option for Model::language

# Model.frameworks
SBO_CONTINUOUS = SBO + "0000062"  # < SBO term and option for Model::framework
SBO_DISCRETE = SBO + "0000063"    # < SBO term and option for Model::framework

# URIs for SBOL extension objects
SYSBIO_DESIGN = SYSBIO_URI + "#Design"
SYSBIO_BUILD = SYSBIO_URI + "#Build"
SYSBIO_TEST = SYSBIO_URI + "#Test"
SYSBIO_ANALYSIS = SYSBIO_URI + "#Analysis"
SYSBIO_SAMPLE_ROSTER = SYSBIO_URI + "#SampleRoster"

IGEM_URI = "http://wiki.synbiohub.org/wiki/Terms/igem"
IGEM_STANDARD_ASSEMBLY = IGEM_URI + "#assembly/RFC10"
