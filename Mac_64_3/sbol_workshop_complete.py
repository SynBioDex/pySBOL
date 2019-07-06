
# coding: utf-8

# # Introduction
# Welcome to the SBOL developers tutorial. This tutorial will cover a few basic and advanced concepts when working with the core SBOL libraries. Primarily, we will learn how to read and write SBOL documents, create new
# devices, attach experiemental data to a device, and interact with external biological parts repositories such as SynBioHub. The high level goal is to create a new device from components drawn from different sources, attach experiement data to that device, and upload that device to a remote repository.
# 
# The tutorial will proceed through the following major steps:
# 1. Read in a simple device from an SBOL Compliant XML.
# 2. Extract a promoter from a characterized device from the iGEM interlab study. This data is housed in a remote repoitory.
# 3. Create a new device with the iGEM promoter swapped in for the original promoter.
# 4. Add an attachment to the new device representing experimental data.
# 5. Upload the new device, and its attachment, to SynBioHub
# 

# ## Prework
# 1. Create an account on SynBioHub
# 2. Download the data file they will need to attach
# 3. Download the SBOL document with the second part

# ## Python Installation
# `pip install pysbol`

# # Getting a Device from an SBOL Compliant XML
# In this section, we will read in a new device from an SBOL compliant XML and explore its contents.

# In[ ]:


from sbol import *

# Set your Homespace. All new SBOL objects will be created in this namespace
my_namespace = 'http://sys-bio.org'  # Ex: http://my_namespace.org
setHomespace(my_namespace)

# Start a new SBOL Document to hold the device
doc = Document()
my_device = doc.componentDefinitions.create('my_device')
print(my_device)

# Load some genetic parts taken from the Cello paper
cello_parts = Document('cello_parts.xml')
cello_parts.read('cello_parts.xml')

# Inspect the Document's contents
len(cello_parts)
print(cello_parts)

# Read in the XML and explore its contents. Notice it is composed of
# componentDefinitions and sequences
for obj in cello_parts:
    print(obj)

# Import these objects into your Document
cello_parts.copy('http://examples.org', doc)

# Notice the objects have been imported into your Homespace
for obj in doc:
	print(obj)

# # Retrieve an object from the Document using its uniform resource identifier (URI)
promoter_collection = doc.getCollection(my_namespace + '/Collection/promoters')

# A Collection contains a list of URI references to objects, not the object themselves
for p in promoter_collection.members:
	print(p)

# Retrieve a component, using its full URI
promoter = doc.getComponentDefinition(my_namespace + '/ComponentDefinition/pPhlF/1')

# Retrieve the same component, using its displayId
promoter = doc.componentDefinitions['pPhlF']

# Review the BioPAX and Sequence Ontology terms that describe this component
print(promoter.types)
print(promoter.roles)

# # Getting a Device from Synbiohub
# In this section, we are going to download a device from SynBioHub. We want the medium strength promoter device from the iGEM interlab study. This device will contain a number of components, sequences, and other objects as well.

# In[ ]:

# Start an interface to the part shop
part_shop = sbol.PartShop('https://synbiohub.org/public/igem')


# In[ ]:


# Search for records from the interlab study
records = part_shop.search('interlab')
for record in records:
    print('{}: {}'.format(record.displayId, record))


# In[ ]:


# Import the medium device into the user's Document
medium_comp_uri = records[0].identity
part_shop.pull(medium_comp_uri, doc)


# # In[ ]:


# Explore the new parts
for obj in doc:
    print('{}: {}'.format(sbol.parseClassName(obj.type), obj))


# # Extracting a ComponentDefinition from a Pre-existing Device
# In this section, we will extract the medium strength promoter from the interlab study and add it to the cassette document

# In[ ]:


# Extract the medium strength promoter
medium_strength_promoter = doc.componentDefinitions['BBa_J23106']


# # Creating a New Device
# In this section, we will create a new device by swapping in the promoter from the device in interlab study into the device from the XML. We will start by grabbing the necessary parts from cassette document, and then assembling them together into a new device.

# In[ ]:


# Get parts for a new circuit
rbs = doc.componentDefinitions[ 'LuxR' ]
cds = doc.componentDefinitions[ 'Q2' ]
terminator = doc.componentDefinitions[ 'ECK120010818' ]


# In[ ]:

# Assemble a new gene
my_device.assemblePrimaryStructure([ medium_strength_promoter, rbs, cds, terminator ])

# In[ ]:

# Annotate the target construct with a Sequence Ontology term
my_device.roles = sbol.SO_GENE

# In[ ]:


# Explore the newly assembled gene
for comp in my_device.getPrimaryStructure():
    print(comp.displayId)


# In[ ]:


# This causes a seg fault. In fact, any call to `modified_gene.sequence`
# causes a seg fault. This is an issue because we cannot add the device
# to synbiohub without the gene having an attached sequence.


target_sequence = my_device.compile()
print(my_device.sequence.elements)

# # Managing a Design-Build-Test-Learn workflow
# Now that we have a target construct, we will hand the design off to the laboratory 
# for construction and characterization. To represent a workflow we use Activity objects.
# Each Activity has an Agent who executes a Plan.

design = doc.designs.create('my_device')
design.structure = my_device
design.function = None  # This tutorial does not cover ModuleDefinitions and interactions

workflow_step_1 = Activity('build_1')
workflow_step_2 = Activity('build_2')
workflow_step_3 = Activity('test_1')
workflow_step_4 = Activity('analysis_1')

workflow_step_1.plan = Plan('gibson_assembly')
workflow_step_2.plan = Plan('transformation')
workflow_step_3.plan = Plan('promoter_characterization')
workflow_step_4.plan = Plan('parameter_optimization')

setHomespace('')
Config.setOption('sbol_compliant_uris', False)  # Temporarily disable auto-construction of URIs

workflow_step_1.agent = Agent('mailto:jdoe@%s' %my_namespace)
workflow_step_2.agent = workflow_step_1.agent
workflow_step_3.agent = Agent('http://sys-bio.org/plate_reader_1')
workflow_step_4.agent = Agent('http://tellurium.analogmachine.org')

Config.setOption('sbol_compliant_uris', True)
setHomespace('https://sys-bio.org')

doc.addActivity([workflow_step_1, workflow_step_2, workflow_step_3, workflow_step_4])

gibson_mix = workflow_step_1.generateBuild('gibson_mix', design)
clones = workflow_step_2.generateBuild(['clone1', 'clone2', 'clone3'], design, gibson_mix)
experiment1 = workflow_step_3.generateTest('experiment1', clones)
analysis1 = workflow_step_4.generateAnalysis('analysis1', experiment1)

# Validate the Document

print(doc.validate())
doc.write('dbtl_example.xml')

# # In[ ]:


# # TODO I couldn't figure out how to do this :-\


# # # Uploading the Device back to SynBioHub
# # Finally, we can create a new collection on SynBioHub with the new device and its workflow history.

# # In[ ]:


# user_name = <USERNAME>

# # In[ ]:


# part_shop.login(user_name)


# # In[ ]:

# # Upon submission, the Document will be converted to a Collection with the following properties
# # The new Collection will have a URI that conforms to the following pattern:
# # https://synbiohub.org/user/<USERNAME>/<DOC.DISPLAYID>/<DOC.DISPLAYID>_collection
# doc.displayId = 'my_device'
# doc.name = 'my device'
# doc.description = 'a description of the cassette'


# # In[ ]:

# part_shop.submit(doc)

# # Attach raw experimental data to the Test object here. Note the pattern
# test_uri = 'https://synbiohub.org/user/' + user_name + '/' + doc.displayId + '/Test_experiment1/1'
# part_shop.attachFile(test_uri, <ENTER PATH TO ATTACHED FILE HERE>)

# #Attach processed experimental data here
# part_shop.attachFile(<ENTER THE URI OF THE ANALYSIS OBJECT HERE>, <ENTER ATTACHMENT FILE PATH HERE>)
