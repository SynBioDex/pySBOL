SBOL Examples
======================

See `Full Example Code <https://pysbol2.readthedocs.io/en/latest/sbol_examples.html#id2>`_ for full example code.

---------------------------------
Computer-aided Design with PySBOL
---------------------------------

Design abstraction enables the synthetic biologist to think about the high-level, functional characteristics of a biological system independently of its structural characteristics. This enables a computer-aided design (CAD) approach similar to electronics, in which the functional or schematic representation of an electronic circuit can be represented separately from the physical dimensions of the electronic components. One advantage of the SBOL standard over GenBank is the ability to represent DNA as abstract components without knowing their exact sequence. An abstract design can be used as a template, with sequence information filled in later.
A ComponentDefinition represents a biological component whose general function is known while its sequence is currently unknown or unspecified. The intended function of a component is specified using a term from the Sequence Ontology (SO), a standard vocabulary for describing genetic parts. The following example shows how to construct a simple abstract component. As the following example shows, some common SO terms are built in to libSBOL as pre-defined constants (see @file constants.h ). This code example defines the new component as a gene. Other terms may be found by browsing the [Sequence Ontology](http://www.sequenceontology.org/browser/obob.cgi) online.
Below is a diagram of a gene cassette. It is composed of genetic subcomponents including a promoter, ribosome binding site (RBS), coding sequence (CDS), and transcriptional terminator, expressed in SBOLVisual symbols. The next example will demonstrate how an abstract design for this gene is assembled from its subcomponents.

.. figure:: ../gene_cassette.png
    :align: center
    :figclass: align-center

.. code:: python

    # Construct an abstract design for a gene
    gene_example = ComponentDefinition("gene_example");
    gene_example.roles.set(SO_GENE);

    # Fetch the subcomponents for this design from an online repository
    igem = PartShop("https://synbiohub.org")
    igem.pull("https://synbiohub.org/public/igem/BBa_R0010/1", doc)
    igem.pull("https://synbiohub.org/public/igem/BBa_B0032/1", doc)
    igem.pull("https://synbiohub.org/public/igem/BBa_E0040/1", doc)
    igem.pull("https://synbiohub.org/public/igem/BBa_B0012/1", doc)

    r0010 = doc.getComponentDefinition('https://synbiohub.org/public/igem/BBa_R0010/1')
    b0032 = doc.getComponentDefinition('https://synbiohub.org/public/igem/BBa_B0032/1')
    e0040 = doc.getComponentDefinition('https://synbiohub.org/public/igem/BBa_E0040/1')
    b0012 = doc.getComponentDefinition('https://synbiohub.org/public/igem/BBa_B0012/1')
.. end

-------------------------------
Hierarchical DNA Assembly
-------------------------------

DNA sequences and biological structures in general exhibit hierarchical organization, from the genome, to operons, to genes, to lower level genetic operators. An important advantage of SBOL over GenBank is the ability to represent DNA as an abstraction hierarchy. LibSBOL includes methods that assemble components into hierarchical compositions. The following code example generates a hierarchical description of the gene  created previously. Note that the subcomponents must be added to a Document for assembly, so a Document is passed as a parameter.


.. code:: python

    gene_example.assemble([ r0010, b0032, e0040, b0012 ], doc)
.. end

-------------------------------
Sequence Assembly
-------------------------------

A complete design adds explicit sequence information to the components in a template design. In order to complete the DNA sequence for a design, Sequence objects must be created and associated with the template design previously created. In contrast to the `ComponentDefinition.assemble() <https://pysbol2.readthedocs.io/en/latest/API.html#sbol.libsbol.ComponentDefinition.assemble>`_ method, which assembles a template design, the `Sequence.assemble() <https://pysbol2.readthedocs.io/en/latest/API.html#sbol.libsbol.Sequence.assemble>`_ method calculates the complete sequence of a design from the sequence of its subcomponents. You must assemble the template design prior to assembling the the complete sequence.

.. code:: python 

    gene_seq = Sequence("gene_seq")
    gene_seq.sequences.set(gene_seq.identity.get())
    gene_seq.assemble()
    print (gene_seq.elements.get())
.. end

-------------------------------
Full Example Code
-------------------------------

Full example code is provided below, which will create a file called "gene_cassette.xml"

.. code:: python

    from sbol import *
    
    setHomespace("http://sys-bio.org")
    doc = Document()
    
    gene_example = ComponentDefinition("gene_example")
    promoter = ComponentDefinition("R0010")
    cds = ComponentDefinition("B0032")
    RBS = ComponentDefinition("E0040")
    terminator = ComponentDefinition("B0012")
    
    promoter.roles.set(SO_PROMOTER)
    CDS.roles.set(SO_CDS)
    RBS.roles.set(SO_RBS)
    terminator.roles.set(SO_TERMINATOR)
    
    doc.addComponentDefinition(gene)
    doc.addComponentDefinition(promoter)
    doc.addComponentDefinition(CDS)
    doc.addComponentDefinition(RBS)
    doc.addComponentDefinition(terminator)
    
    gene.assemble([ promoter, RBS, CDS, terminator ])
    
    first = gene.getFirstComponent()
    print(first.identity.get())
    last = gene.getLastComponent()
    print(last.identity.get())
    
    promoter_seq = Sequence("R0010", "ggctgca")
    RBS_seq = Sequence("B0032", "aattatataaa")
    CDS_seq = Sequence("E0040", "atgtaa")
    terminator_seq = Sequence("B0012", "attcga")
    gene_seq = Sequence("BB0001")
    
    doc.addSequence([promoter_seq, CDS_seq, RBS_seq, terminator_seq, gene_seq])
    
    promoter.sequences.set(promoter_seq.identity.get())
    CDS.sequences.set(CDS_seq.identity.get())
    RBS.sequences.set(RBS_seq.identity.get())
    terminator.sequences.set(terminator_seq.identity.get())
    gene.sequences.set(gene_seq.identity.get())
    
    gene_seq.assemble()
    
    print(promoter_seq.elements.get())
    print(RBS_seq.elements.get())
    print(CDS_seq.elements.get())
    print(terminator_seq.elements.get())
    print(gene_seq.elements.get())
    
    result = doc.write("gene_cassette.xml")
    print(result)
.. end