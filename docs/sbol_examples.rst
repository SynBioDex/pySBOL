SBOL Examples
======================

See `Full Example Code <https://pysbol2.readthedocs.io/en/latest/sbol_examples.html#id2>`_ for full example code.

---------------------------------
Computer-aided Design with PySBOL
---------------------------------

An advantage of the SBOL data format over GenBank is the ability to represent DNA as abstract components without specifying an exact sequence. An **abstract design** can be used as a template, with sequence information filled in later. In SBOL, a ComponentDefinition represents a biological component whose general function is known while its sequence is currently either unknown or unspecified. The intended function of the component is specified using a descriptive term from the Sequence Ontology (SO), a standard vocabulary for describing genetic parts. As the following example shows, some common SO terms are built in to PySBOL as pre-defined constants (see `constants.h <https://github.com/SynBioDex/pySBOL/blob/develop/source/constants.h>`_). This code example defines the new component as a gene by setting its `roles` property to the SO term for `gene`.  Other terms may be found by browsing the `Sequence Ontology <http://www.sequenceontology.org/browser/obob.cgi>`_ online.

.. code:: python

    # Construct an abstract design for a gene
    gene = ComponentDefinition('gene_example')
    gene.roles = SO_GENE

.. end

**Design abstraction** is an important engineering principle for synthetic biology. Abstraction enables the engineer to think at a high-level about functional characteristics of a system while hiding low-level physical details. For example, in electronics, abstract schematics are used to describe the function of a circuit, while hiding the physical details of how a printed circuit board is laid out. Computer-aided design (CAD) programs allow the engineer to easily switch back and forth between abstract and physical representations of a circuit. In the same spirit, PySBOL enables a CAD approach for designing genetic constructs and other forms of synthetic biology.

-------------------------------
Hierarchical DNA Assembly
-------------------------------

PySBOL also includes methods for assembling biological components into **abstraction hierarchies**. This is important rom a biological perspective, because DNA sequences and biological structures in general exhibit hierarchical organization, from the genome, to operons, to genes, to lower level genetic operators. The following code assembles an abstraction hierarchy that describes a gene cassete. Note that subcomponents must belong to a `Document` in order to be assembled, so a `Document` is passed as a parameter.

The gene cassette below is composed of genetic subcomponents including a promoter, ribosome binding site (RBS), coding sequence (CDS), and transcriptional terminator, expressed in SBOL Visual schematic glyphs. The next example demonstrates how an abstract design for this gene is assembled from its subcomponents.

.. code:: python

    gene.assemblePrimaryStructure([ r0010, b0032, e0040, b0012 ], doc)
.. end

After creating an abstraction hierarchy, it is then possible to iterate through an object's primary structure of components:

.. code:: python

    for component_definition in gene.getPrimaryStructure()):
        print (component_definition.identity)
.. end

This returns a list of `ComponentDefinitions` arranged in their primary sequence. *Caution!* It is also possible to iterate through components as follows, but this way is *not* guaranteed to return components in sequential order. This is because SBOL supports a variety of structural descriptions, not just primary structure.

.. code:: python

    for component in gene.components:
        print (component.definition)
.. end

-------------------------------
Sequence Assembly
-------------------------------

A **complete design** adds explicit sequence information to the components in a **template design** or **abstraction hierarchy**. In order to complete a design, `Sequence` objects must first be created and associated with the promoter, CDS, RBS, terminator subcomponents. In contrast to the `ComponentDefinition.assemble() <https://pysbol2.readthedocs.io/en/latest/API.html#sbol.pySBOL.ComponentDefinition.assemble>`_ method, which assembles a template design, the `ComponentDefinition.compile` method recursively generates the complete sequence of a hierarchical design from the sequence of its subcomponents. Compiling a DNA sequence is analogous to a programmer compiling their code. *In order to `compile` a `ComponentDefinition`, you must first assemble a template design from `ComponentDefinitions`, as described in the previous section.*

.. code:: python 

    target_sequence = gene.compile()
.. end

The `compile` method returns the target sequence as a string. In addition, it creates a new `Sequence` object and assigns the target sequence to its `elements` property
 
--------------------------------------------------------------
Iterating through a Primary Sequence of Components
--------------------------------------------------------------

Sometimes it is desired to iterate through individual components inside a sequence of components. One application of this is to check the order of a sequence of components. To do so, one can simply implement typical forloop used in Python. The example below shows how one would iterate through a primary sequence of components to validate the correct order.

.. code:: python

    doc = Document()

    gene = ComponentDefinition('BB0001')
    promoter = ComponentDefinition('R0010')
    CDS = ComponentDefinition('B0032')
    RBS = ComponentDefinition('E0040')
    terminator = ComponentDefinition('B0012')

    doc.addComponentDefinition([gene, promoter, CDS, RBS, terminator])

    gene.assemble([ promoter, RBS, CDS, terminator ])
    primary_sequence = gene.getPrimaryStructure()
    for component in primary_sequence:
        print(component.displayId)

.. end

The output is shown below, which captures the correct order.

.. code:: python

    R0010
    E0040
    B0032
    B0012

.. end
    
-------------------------------
Full Example Code
-------------------------------

Full example code is provided below, which will create a file called "gene_cassette.xml"

.. code:: python

    from sbol import *

    setHomespace('http://sys-bio.org')
    doc = Document()

    gene = ComponentDefinition('gene_example')
    promoter = ComponentDefinition('R0010')
    CDS = ComponentDefinition('B0032')
    RBS = ComponentDefinition('E0040')
    terminator = ComponentDefinition('B0012')

    promoter.roles = SO_PROMOTER
    CDS.roles = SO_CDS
    RBS.roles = SO_RBS
    terminator.roles = SO_TERMINATOR

    doc.addComponentDefinition(gene)
    doc.addComponentDefinition([ promoter, CDS, RBS, terminator ])

    gene.assemblePrimaryStructure([ promoter, RBS, CDS, terminator ])

    first = gene.getFirstComponent()
    print(first.identity)
    last = gene.getLastComponent()
    print(last.identity)

    promoter.sequence = Sequence('R0010', 'ggctgca')
    CDS.sequence = Sequence('B0032', 'aattatataaa')
    RBS.sequence = Sequence('E0040', "atgtaa")
    terminator.sequence = Sequence('B0012', 'attcga')

    target_sequence = gene.compile()
    print(gene.sequence.elements)

    result = doc.write('gene_cassette.xml')
    print(result)

.. end
