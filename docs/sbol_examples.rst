SBOL Examples
======================

See `Full Example Code <https://pysbol2.readthedocs.io/en/latest/sbol_examples.html#id2>`_ for full example code.

---------------------------------
Computer-aided Design with PySBOL
---------------------------------

An advantage of the SBOL data format over GenBank is the ability to represent DNA as abstract components without specifying an exact sequence. An **abstract design** can be used as a template, with sequence information filled in later. In SBOL, a ComponentDefinition represents a biological component whose general function is known while its sequence is currently either unknown or unspecified. The intended function of the component is specified using a descriptive term from the Sequence Ontology (SO), a standard vocabulary for describing genetic parts. As the following example shows, some common SO terms are built in to PySBOL as pre-defined constants (see `constants.h <https://github.com/SynBioDex/pySBOL/blob/develop/source/constants.h>`_). This code example defines the new component as a gene by setting its `roles` property to the SO term for `gene`.  Other terms may be found by browsing the `Sequence Ontology <http://www.sequenceontology.org/browser/obob.cgi>`_ online.

.. code:: python

    # Construct an abstract design for a gene
    gene = ComponentDefinition("gene_example");
    gene.roles.set(SO_GENE);
.. end

**Design abstraction** is an important engineering principle for synthetic biology. Abstraction enables the engineer to think at a high-level about functional characteristics of a system while hiding low-level physical details. For example, in electronics, abstract schematics are used to describe the function of a circuit, while hiding the physical details of how a printed circuit board is laid out. Computer-aided design (CAD) programs allow the engineer to easily switch back and forth between abstract and physical representations of a circuit. In the same spirit, PySBOL enables a CAD approach for designing genetic constructs and other forms of synthetic biology.

-------------------------------
Hierarchical DNA Assembly
-------------------------------

PySBOL also includes methods for assembling biological components into **abstraction hierarchies**. This is important rom a biological perspective, because DNA sequences and biological structures in general exhibit hierarchical organization, from the genome, to operons, to genes, to lower level genetic operators. The following code assembles an abstraction hierarchy that describes a gene cassete. Note that subcomponents must belong to a `Document` in order to be assembled, so a `Document` is passed as a parameter.

The gene cassette below is composed of genetic subcomponents including a promoter, ribosome binding site (RBS), coding sequence (CDS), and transcriptional terminator, expressed in SBOL Visual schematic glyphs. The next example demonstrates how an abstract design for this gene is assembled from its subcomponents.

.. code:: python

    gene.assemble([ r0010, b0032, e0040, b0012 ], doc)
.. end

After creating an abstraction hierarchy, it is then possible to iterate through an object's primary structure of components:

.. code:: python

    for component_definition in gene.getPrimaryStructure()):
        print (component_definition.identity.get())
.. end

This returns a list of `ComponentDefinitions` arranged in their primary sequence. *Caution!* It is also possible to iterate through components as follows, but this way is *not* guaranteed to return components in sequential order. This is because SBOL supports a variety of structural descriptions, not just primary structure.

.. code:: python

    for component in gene.components:
        print (component.definition.get())
.. end

-------------------------------
Sequence Assembly
-------------------------------

A **complete design** adds explicit sequence information to the components in a **template design** or **abstraction hierarchy**. In order to complete a design, `Sequence` objects must first be created and associated with the promoter, CDS, RBS, terminator subcomponents. In contrast to the `ComponentDefinition.assemble() <https://pysbol2.readthedocs.io/en/latest/API.html#sbol.pySBOL.ComponentDefinition.assemble>`_ method, which assembles a template design, the `Sequence.compile` method recursively generates the complete sequence of a hierarchical design from the sequence of its subcomponents. Compiling a DNA sequence is analogous to a programmer compiling their code. *In order to compile a `Sequence`, you must first assemble a template design from `ComponentDefinitions`, as described in the previous section.*

.. code:: python 

    gene_seq = Sequence("gene_seq")
    gene_seq.sequences.set(gene_seq.identity.get())
    gene_seq.compile()
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
    
    gene = ComponentDefinition("gene_example")
    promoter = ComponentDefinition("R0010")
    CDS = ComponentDefinition("B0032")
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