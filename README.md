pySBOL 2.0.1
======================================

**pySBOL** is a SWIG-Python wrapper around [libSBOL](https://github.com/SynBioDex/libSBOL), a module for reading, writing, and constructing genetic designs according to the standardized specifications of the [Synthetic Biology Open Language (SBOL)](http://www.sbolstandard.org/).  

USE CASE
========
![](crispr_repression2.png)

**Illustration of a hierarchical CRISPR-based repression module represented in SBOL 2.0 (adapted from Figure~1a in [this paper from *Nature Methods*](http://www.nature.com/nmeth/journal/v11/n7/full/nmeth.2969.html) by Kiani, *et al*. The inner Module consists of a CRISPR Repression Circuit that combines a Cas9 protein with a gRNA to form a complex (represented by the dashed arrows) that permanently inactivates a target gene by excising its promoter (represented by the arc with the T-shaped head).   The outer Module is a 3-color Characterization Circuit that expresses blue, yellow, and red fluorescent proteins. The characterization module is coupled to the characterization module in to produce a visual read of the state of the cell. Red is a control signal that calibrates the blue and yellow signals in relation to the bioenergetic state of the cell under different metabolic loads. The dashed lines connecting Modules show how FunctionalComponents in one Module correspond or map to FunctionalComponents in another.**

CODE EXAMPLE
============
For the full code, see CRISPR_example.py

```
from sbol import *

# Define the two modules, denoted by the black boxes in the figure.  Note the use of CamelCase for displayId's, to distinguish ModuleDefinitions from Modules
CRISPRTemplate = ModuleDefinition(ns, "CRISPRTemplate", v)
CRPbCircuit = ModuleDefinition(ns, "CRPbCircuit", v)

# Components in the CRISPR Template
Cas9 = ComponentDefinition(ns, "Cas9", v, BIOPAX_PROTEIN)
GuideRNA = ComponentDefinition(ns, "GuideRNA", v, BIOPAX_RNA)
Cas9GuideRNAComplex = ComponentDefinition(ns, "Cas9-GuideRNAComplex", v, BIOPAX_COMPLEX)
TargetPromoter = ComponentDefinition(ns, "TargetPromoter", v, BIOPAX_DNA)
TargetGene = ComponentDefinition(ns, "TargetGene", v, BIOPAX_DNA)
TargetProtein = ComponentDefinition(ns, "TargetProtein", v, BIOPAX_PROTEIN)

# Start the CRPb Characterization Module
# For simplicity, only components that interface with the CRISPRTemplate Module are defined here.  For now, the rest of the module is treated like a black box
# Components in the CRPb Characterization Module
Cas9mBFP = ComponentDefinition(ns, "Cas9-mBFP", v, BIOPAX_PROTEIN)  # This is an output of the Module
GuideRNAb = ComponentDefinition(ns, "GuideRNAb", v, BIOPAX_RNA)  # This is an output of the Module
Cas9mBFPGuideRNAComplex = ComponentDefinition(ns, "Cas9mBFPGuideRNAComplex", v, BIOPAX_RNA)
CRPbPromoter = ComponentDefinition(ns, "CRPbPromoter", v, BIOPAX_DNA)
EYFPGene = ComponentDefinition(ns, "EYFPGene", v, BIOPAX_DNA)
EYFP = ComponentDefinition(ns, "EYFP", v, BIOPAX_PROTEIN)  # This is the input of the Module

# Instantiate Modules
crispr_template = Module(ns, "crispr_template", v, "sys-bio.org/ModuleDefinition/CRISPRTemplate/1.0.0")
CRISPRTemplate.modules.add(crispr_template)
crpb_circuit = Module(ns, "crpb_circuit", v, "sys-bio.org/ModuleDefinition/CRPbPromoter/1.0.0")
CRPbCircuit.modules.add(crpb_circuit)

# Define the Components at the interface of the two Modules
cas9 = FunctionalComponent(ns, "cas9", v, "sys-bio.org/ComponentDefinition/Cas9/1.0.0", SBOL_ACCESS_PUBLIC, SBOL_DIRECTION_IN)
guide_rna = FunctionalComponent(ns, "guide_rna", v, GuideRNA.identity.get(), SBOL_ACCESS_PUBLIC, SBOL_DIRECTION_IN)
target_protein = FunctionalComponent(ns, "target_protein", v, TargetProtein.identity.get(), SBOL_ACCESS_PUBLIC, SBOL_DIRECTION_OUT)
cas9_mbfp = FunctionalComponent(ns, "cas9_mbfp", v, Cas9mBFP.identity.get(), SBOL_ACCESS_PUBLIC, SBOL_DIRECTION_OUT);
guide_rna_b = FunctionalComponent(ns, "guide_rna_b", v, GuideRNAb.identity.get(), SBOL_ACCESS_PUBLIC, SBOL_DIRECTION_OUT);
eyfp = FunctionalComponent(ns, "eyfp", v, EYFP.identity.get(), SBOL_ACCESS_PUBLIC, SBOL_DIRECTION_OUT);

# Connect the modules
cas9_input = MapsTo(ns, "cas9_input", v, cas9.identity.get(), cas9_mbfp.identity.get(), SBOL_REFINEMENT_USE_REMOTE)
guide_rna_input = MapsTo(ns, "guide_rna_input", v, guide_rna.identity.get(), guide_rna_b.identity.get(), SBOL_REFINEMENT_USE_REMOTE)
eyfp_output = MapsTo(ns, "eyfp_output", v, target_protein.identity.get(), eyfp.identity.get(), SBOL_REFINEMENT_USE_REMOTE)

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
