Biological Parts Repositories
======================

---------------------------------------------
Mining Genetic Parts From Online Repositories
---------------------------------------------

In today's modern technological society, a variety of interesting technologies can be assembled from "off-the-shelf" components, including cars, computers, and airplanes. Synthetic biology is inspired by a similar idea. Synthetic biologists aim to program new biological functions into organisms by assembling genetic code from off-the-shelf DNA sequences. PySBOL puts an inventory of biological parts at your fingertips.

For example, the `iGEM Registry of Standard Biological Parts <http://parts.igem.org/Main_Page>`_ is an online resource that many synthetic biologists are familiar with.  The Registry is an online database that catalogs a vast inventory of genetic parts, mostly contributed by students in the iGEM competition. These parts are now available in SBOL format in the `SynBioHub <http://synbiohub.org>`_ knowledgebase, hosted by Newcastle University. The code example below demonstrates how a programmer can access these data.

The following code example shows how to pull data about biological components from the SynBioHub repository. In order to pull a part, simply locate the web address of that part by browsing the SynBioHub repository online. Alternatively, pySBOL also supports programmatic querying of SynBioHub (see below).

The interface with the SynBioHub repository is represented by a `PartShop` object. The following code retrieves parts corresponding to promoter, coding sequence (CDS), ribosome binding site (RBS), and transcriptional terminator. These parts are imported into a `Document` object, which must be initialized first. See `Getting Started with SBOL <https://pysbol2.readthedocs.io/en/latest/getting_started.html>`_ for more about creating `Documents`.

.. code:: python

    igem = PartShop("https://synbiohub.org")
    igem.pull("http://synbiohub.org/public/igem/BBa_T9002/1", doc)
    igem.pull("http://synbiohub.org/public/igem/BBa_B0032/1", doc)
    igem.pull("http://synbiohub.org/public/igem/BBa_E0040/1", doc)
    igem.pull("http://synbiohub.org/public/igem/BBa_B0012/1", doc)

    t9002 = doc.getComponentDefinition('http://synbiohub.org/public/igem/BBa_T9002/1')
    b0032 = doc.getComponentDefinition('http://synbiohub.org/public/igem/BBa_B0032/1')
    e0040 = doc.getComponentDefinition('http://synbiohub.org/public/igem/BBa_E0040/1')
    b0012 = doc.getComponentDefinition('http://synbiohub.org/public/igem/BBa_B0012/1')
.. end

--------------------
Searching Part Repos
--------------------

PySBOL supports three kinds of searches: a **general search**, an **exact search**, and an **advanced search**.

The following query conducts a **general search** which scans through `identity`, `name`, `description`, and `displayId` properties for a match to the search text, including partial, case-insensitive matches to substrings of the property value. Search results are returned as a `SearchResponse` object.

.. code:: python

    records = igem.search("plasmid")
.. end

By default, the general search looks only for `ComponentDefinitions`, and only returns 25 records at a time in order to prevent server overload. The search above is equivalent to the one below, which explicitly specifies which kind of SBOL object to search for, an offset of 0 (explained below), and a limit of 25 records.

.. code:: python

    records = igem.search("plasmid", SBOL_COMPONENT_DEFINITION, 0, 25)
.. end

Of course, these parameters can be changed to search for different type of SBOL objects or to return more records. For example, some searches may match a large number of objects, more than the specified limit allows. In this case, it is possible to specify an offset and to retrieve additional records in successive requests. The total number of objects in the repository matching the search criteria can be found using the searchCount method, which has the same call signature as the search method. It is a good idea to put a small delay between successive requests to prevent server overload. The following example demonstrates how to do this. The 100 millisecond delay is implemented using cross-platform C++11 headers chrono and thread. As of the writing of this documentation, this call retrieves 391 records.

.. code:: python

    import time

    records = SearchResponse()
    search_term = "plasmid"
    limit = 25
    total_hits = igem.searchCount(search_term)
    for offset in range(0, total_hits, limit):
        records.extend( igem.search(search_term, SBOL_COMPONENT_DEFINITION, offset, limit) )
        time.sleep(0.1)
.. end

A `SearchResponse` object is returned by a query and contains multiple records. Each record contains basic data, including identity, displayId, name, and description fields. *It is very important to realize however that the search does not retrieve the complete ComponentDefinition!* In order to retrieve the full object, the user must call `pullComponentDefinition` while specifying the target object's identity.

Records in a `SearchResponse` can be accessed using iterators or numeric indices. The interface for each record behaves exactly like any other SBOL object:

.. code:: python

    for record in records:
        print( record.identity.get() )
.. end

The preceding examples concern **general searches**, which scan through an object's metadata for partial matches to the search term. In contrast, the **exact search** explicitly specifies which property of an object to search, and the value of that property must exactly match the search term. The following **exact search** will search for `ComponentDefinitions` with a role of promoter:

.. code:: python

records = igem.search(SO_PROMOTER, SBOL_COMPONENT_DEFINITION, SBOL_ROLES, 0, 25);
.. end

Finally, the **advanced search** allows the user to configure a search with multiple criteria by constructing a `SearchQuery` object. The following query looks for promoters that have an additional annotation indicating that the promoter is regulated (as opposed to constitutive):

.. code:: python

    q = SearchQuery();
    q["objectType"].set(SBOL_COMPONENT_DEFINITION);
    q["limit"].set(25);
    q["offset"].set(0);
    q["role"].set(SO_PROMOTER);
    q["role"].add("http://wiki.synbiohub.org/wiki/Terms/igem#partType/Regulatory");
    total_hits = igem.searchCount(q);
    records = igem.search(q);
.. end

----------------------------
Submitting Designs to a Repo
----------------------------

Users can submit their SBOL data directly to a PartShop using the PySBOL API. This is important, so that other synthetic biologists may access the data and build off each other's work. Submitting to a repository is also important for reproducing published scientific work. The synthetic biology journal ACS Synthetic Biology now encourages authors to submit SBOL data about their genetically engineered DNA to a repository like `SynBioHub <https://synbiohub.org>`_ or `JBEI-ICE <https://acs-registry.jbei.org/login>`_. In order to submit to a PartShop remotely, the user must first vist the appropriate website and register. Once the user has established an account, they can then log in remotely using PySBOL.

.. code:: python

    login("johndoe@example.org", password)
    submit(doc)
.. end