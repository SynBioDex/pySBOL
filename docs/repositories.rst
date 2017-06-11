Using Repositories
======================

---------------------------------------------
Mining Genetic Parts From Online Repositories
---------------------------------------------

In today's modern technological society, a variety of interesting and complicated products are built from off-the-shelf components. Imagine searching for an automotive part at your local parts shop. You might tell the clerk which part you are looking for, at which point she will look that part up in the company database, and then assist you to pull the part from the shelves. LibSBOL puts an inventory of biological parts at your fingertips.
LibSBOL makes it easy for users to pull data about biological components from online databases. The [iGEM Registry of Standard Biological Parts](http://parts.igem.org/Main_Page) is an online database that catalogs a vast inventory of genetic parts, many contributed by students competing in iGEM. These parts are available in SBOL format in the [SynBioHub](http://synbiohub.org) knowledgebase, hosted by Newcastle University. Using a part's web address, the user can fetch data about that part. Feel free to browse available parts online. Alternatively, users can use LibSBOL's search methods to locate interesting parts.
The following code example shows how to pull data about biological components from the SynBioHub repository. The SynBioHub repository is represented with a PartShop object. The following code retrieves parts  corresponding to promoter, coding sequence (CDS), ribosome binding site (RBS), and transcriptional terminator. These are imported into a Document object, which must be initialized first. See @ref getting_started for more about creating Documents.

.. code:: python

igem = PartShop("http://synbiohub.org")
igem.pull("http://synbiohub.org/public/igem/BBa_T9002/1", doc)
igem.pull("http://synbiohub.org/public/igem/BBa_B0032/1", doc)
igem.pull("http://synbiohub.org/public/igem/BBa_E0040/1", doc)
igem.pull("http://synbiohub.org/public/igem/BBa_B0012/1", doc)

t9002 = doc.getComponentDefinition('http://synbiohub.org/public/igem/BBa_T9002/1')
b0032 = doc.getComponentDefinition('http://synbiohub.org/public/igem/BBa_B0032/1')
e0040 = doc.getComponentDefinition('http://synbiohub.org/public/igem/BBa_E0040/1')
b0012 = doc.getComponentDefinition('http://synbiohub.org/public/igem/BBa_B0012/1')

--------------------
Searching Part Repos
--------------------

The easiest search is a general search, which scans the fields of an object for a partial, case-insensitive match to the search term. The type of object should be specified using the type definition for an SBOL Object. The response is returned as a list of dictionary objects, where each dictionary contains a record about a part in the PartShop. By default the search only returns a maximum of 25 records. If more than 25 objects in the repository match the search criteria, then the user may specify an offset and limit to obtain additional records.

.. code:: python

# This returns 14 records as of 9 Jun 2017
records = igem.search("repressilator", SBOL_COMPONENT_DEFINITION)

# The search for "enzyme" returns 25 records, the default limit. User can specify a different limit.
all_records = []
records = igem.search("enzyme", SBOL_COMPONENT_DEFINITION)
offset = len(records)

# Continue requesting records until the end is reached (a total of 173 records)
while len(records) > 0 :
    records = igem.search("enzyme", SBOL_COMPONENT_DEFINITION, offset)
    offset += len(records)
    all_records.extend(records)

----------------------------
Submitting Designs to a Repo
----------------------------

Users can submit their SBOL data directly to a PartShop using the PySBOL API. This is important, so that other synthetic biologists may access the data and build off each other's work. Submitting to a repository is also important for reproducing published scientific work. The synthetic biology journal ACS Synthetic Biology now encourages authors to submit SBOL data about their genetically engineered DNA to a repository like [SynBioHub](https://synbiohub.org) or [JBEI-ICE](https://acs-registry.jbei.org/login). In order to submit to a PartShop remotely, the user must first vist the appropriate website and register. Once the user has established an account, they can then log in remotely using PySBOL.

.. code:: python

login("bbartley@sys-bio.org", password)
submit(doc)
