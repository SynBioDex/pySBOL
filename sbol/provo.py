from identified import *
from constants import *
from toplevel import *

class Association(Identified):
    # The agent property is REQUIRED and MUST contain a URI that refers to an Agent object.
    agent = None

    # The role property is REQUIRED and MUST contain a URI that refers
    # to a particular term describing the usage of the agent.
    roles = None

    # The plan property is OPTIONAL and contains a URI that refers to a Plan.
    plan = None

    def __init__(self, uri="example", agent="", role="", version=VERSION_STRING, rdf_type=PROVO_ASSOCIATION):
        """Constructor.

        :param uri: A full URI including a scheme, namespace, and identifier.
        If SBOLCompliance configuration is enabled, then this argument is simply the displayId for the new object
        and a full URI will automatically be constructed.
        :param agent:
        :param role:
        :param version:
        :param rdf_type: The RDF type for an extension class derived from this one.
        """
        super().__init__(rdf_type, uri, version)


class Usage(Identified):
    # The entity property is REQUIRED and MUST contain a URI which MAY refer to an SBOL Identified object.
    entity = None

    # The role property is REQUIRED and MAY contain a URI that refers to a particular term describing
    # the usage of an entity referenced by the entity property.
    roles = None

    def __init__(self, uri="example", entity="", role="", version=VERSION_STRING, rdf_type=PROVO_USAGE):
        """Constructor.

        :param uri: A full URI including a scheme, namespace, and identifier.
        If SBOLCompliance configuration is enabled, then this argument is simply the displayId for the new object
        and a full URI will automatically be constructed.
        :param entity:
        :param role:
        :param version:
        :param type: The RDF type for an extension class derived from this one.
        """
        super().__init__(rdf_type, uri, version)


class Agent(TopLevel):
    """Examples of agents are person, organisation or software.
    These agents should be annotated with additional information, such as software version
    needed to be able to run the same software again.
    """
    def __init__(self, uri="example", version=VERSION_STRING, rdf_type=PROVO_AGENT):
        """Constructor.

        :param uri: A full URI including a scheme, namespace, and identifier.
        If SBOLCompliance configuration is enabled, then this argument is simply the displayId for the new object
        and a full URI will automatically be constructed.
        :param version:
        """
        super().__init__(rdf_type, uri, version)


class Plan(TopLevel):
    def __init__(self, uri="example", version=VERSION_STRING, rdf_type=PROVO_PLAN):
        """Constructor.

        :param uri: A full URI including a scheme, namespace, and identifier.
        If SBOLCompliance configuration is enabled, then this argument is simply the displayId for the new object
        and a full URI will automatically be constructed.
        :param version:
        """
        super().__init__(rdf_type, uri, version)


class Activity(TopLevel):
    """A generated Entity is linked through a wasGeneratedBy relationship to an Activity,
    which is used to describe how different Agents and other entities were used. An Activity is linked through
    a qualifiedAssociation to Associations, to describe the role of agents, and is linked through qualifiedUsage
    to Usages to describe the role of other entities used as part of the activity. Moreover, each Activity includes
    optional startedAtTime and endedAtTime properties. When using Activity to capture how an entity was derived,
    it is expected that any additional information needed will be attached as annotations. This may include
    software settings or textual notes. Activities can also be linked together using the wasInformedBy relationship
    to provide dependency without explicitly specifying start and end times.
    """
    startedAtTime = None

    # The endedAtTime property is OPTIONAL and contains a dateTime (see section Section 12.7) value,
    # indicating when the activity ended.
    endedAtTime = None

    # The wasInformedBy property is OPTIONAL and contains a URI of another activity.
    wasInformedBy = None

    # The qualifiedAssociation property is OPTIONAL and MAY contain a set of URIs that refers to Association.
    associated = None

    # The qualifiedUsage property is OPTIONAL and MAY contain a set of URIs that refers to Usage objects.
    usages = None

    # An Agent object may be specified here, and it will be synced with the Association::agent property.
    agent = None

    # A Plan object may be specified here, and it will be synced with the Association::plan property.
    plan = None

    def __init__(self, uri="example", action_type="", version=VERSION_STRING, rdf_type=PROVO_ACTIVITY):
        """Constructor

        :param uri: A full URI including a scheme, namespace, and identifier.
        If SBOLCompliance configuration is enabled, then this argument is simply the displayId for the new object
        and a full URI will automatically be constructed.
        :param action_type:
        :param version:
        :param rdf_type: The RDF type for an extension class derived from this one.
        """
        super().__init__(rdf_type, uri, version)
