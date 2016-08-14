pySBOL 2.0.1
======================================

**pySBOL** is a SWIG-Python wrapper around [libSBOL](https://github.com/SynBioDex/libSBOL), a module for reading, writing, and constructing genetic designs according to the standardized specifications of the [Synthetic Biology Open Language (SBOL)](http://www.sbolstandard.org/).  

USE CASE
========
![](crispr_repression2.png)

**Illustration of a hierarchical CRISPR-based repression module represented in SBOL 2.0 (adapted from Figure~1a in [this paper from *Nature Methods*](http://www.nature.com/nmeth/journal/v11/n7/full/nmeth.2969.html) by Kiani, *et al*. The inner Module consists of a CRISPR Repression Circuit that combines a Cas9 protein with a gRNA to form a complex (represented by the dashed arrows) that permanently inactivates a target gene by excising its promoter (represented by the arc with the T-shaped head).   The outer Module is a 3-color Characterization Circuit that expresses blue, yellow, and red fluorescent proteins. The characterization module is coupled to the characterization module in to produce a visual read of the state of the cell. Red is a control signal that calibrates the blue and yellow signals in relation to the bioenergetic state of the cell under different metabolic loads. The dashed lines connecting Modules show how FunctionalComponents in one Module correspond or map to FunctionalComponents in another.**

EXAMPLE CODE
============
The example code below can be used to construct the biological design in the figure.  See the @ref getting_started, @ref sequences, and @ref modular_design tutorials to learn more about how libSBOL enables high-level design for synthetic biology.
![](gene_cassette.png)
 
**A diagram of a gene cassette, consisting of a promoter, ribosome binding site (RBS), coding sequence (CDS), and transcriptional terminator, expressed in SBOLVisual symbols. The design was programmatically generated with the code below, and then visualized with the SBOLDesigner tool.**
 
```python
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
```

INSTALLATION
============
Package installation requires setuptools, available here https://pypi.python.org/pypi/setuptools#downloads. (Setuptools is a stable and well-supported library that makes distributing Python projects easier)

1 - Git the package.

2 - After setuptools is installed, run the installer script using the following command line in the package's root directory :
```
$ python setup.py bdist
$ python setup.py install
```
3 - Test import of the modules in your python environment. 
```
>>> import sbol
```
(Caution!  If you have trouble importing the module with the setup script, check to see if there are multiple Python installations on your machine and also check the output of the setup script to see which version of Python is the install target.  You can also test the module locally from inside the Mac_OSX/sbol or Win_32/sbol folders.)

PLATFORMS
=========
Tested on Mac OSX Version 10.9.5 and Windows 7 Enterprise with Python 2.7.9 32 bit. Python 3 not currently supported.

DEPENDENCIES
============
pySBOL is packaged with precompiled binaries for libSBOL.


ACKNOWLEDGEMENTS
================

Current support for the development of libSBOL is generously provided by the NSF through the [Synthetic Biology Open Language Resource](http://www.nsf.gov/awardsearch/showAward?AWD_ID=1355909) collaborative award.
