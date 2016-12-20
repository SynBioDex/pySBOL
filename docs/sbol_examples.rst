Examples of pySBOL
======================

To import pySBOL classes and methods:

``from sbol import *``

The example code below can be used to construct the biological design in the figure. 

.. figure:: ../gene_cassette.png
    :align: center
    :figclass: align-center

**A diagram of a gene cassette, consisting of a promoter, ribosome binding site (RBS), coding sequence (CDS), and transcriptional terminator, expressed in SBOLVisual symbols. The design was programmatically generated with the code below, and then visualized with the SBOLDesigner tool.**
 
.. code:: python

	setHomespace("http://sys-bio.org")
	doc = Document()

	gene = ComponentDefinition("BB0001")
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

	doc.addSequence([ promoter_seq, CDS_seq, RBS_seq, terminator_seq, gene_seq ]);

	promoter.sequence.set(promoter_seq.identity.get())
	CDS.sequence.set(CDS_seq.identity.get())
	RBS.sequence.set(RBS_seq.identity.get())
	terminator.sequence.set(terminator_seq.identity.get())
	gene.sequence.set(gene_seq.identity.get())

	gene_seq.assemble()
	print(gene_seq.elements.get())

	doc.write("gene_cassette.xml")
