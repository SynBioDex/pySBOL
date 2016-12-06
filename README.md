pySBOL 2.1.0
======================================

**pySBOL2** is a SWIG-Python wrapper around [libSBOL](https://github.com/SynBioDex/libSBOL), a module for reading, writing, and constructing genetic designs according to the standardized specifications of the [Synthetic Biology Open Language (SBOL)](http://www.sbolstandard.org/).  

EXAMPLE CODE
============
To import pySBOL classes and methods:
```
from sbol import *
```
The example code below can be used to construct the biological design in the figure. 

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

1 - [Download the latest release.](https://github.com/SynBioDex/pysbol2/releases/latest)

If you want the latest snapshot instead, use [git](https://git-scm.com/) and type following command in the console or terminal.
```
git clone https://github.com/SynBioDex/pysbol2.git
```

2 - Run the installer script by using the following command line in the package's root directory :
```
python setup.py install
```
3 - Test the module in your python environment by importing it. 
```
>>> import sbol
```
(Caution!  If you have trouble importing the module with the setup script, check to see if there are multiple Python installations on your machine and also check the output of the setup script to see which version of Python is the install target. You can also test the module locally from inside the Mac_OSX/sbol or Win_32/sbol folders.)

ACKNOWLEDGEMENTS
================
libSBOL is brought to you by Bryan Bartley, Kiri Choi, and SBOL Developers.

Current support for the development of libSBOL is generously provided by the NSF through the [Synthetic Biology Open Language Resource](http://www.nsf.gov/awardsearch/showAward?AWD_ID=1355909) collaborative award.

<p align="center">
  <img src="./logo.jpg" height="100" />
</p>
