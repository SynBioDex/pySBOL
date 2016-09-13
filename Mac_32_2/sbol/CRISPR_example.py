from sbol import *

ns = "sys-bio.org"  # Namespace
v = "1.0.0";  # Versioning uses Maven semantics
        
# Here we use CamelCase for displayId's, to distinguish Definitions from instances
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
    
crispr_template.mapsTos.add(cas9_input)
crispr_template.mapsTos.add(guide_rna_input)
crispr_template.mapsTos.add(eyfp_output)

# The crispr_template and crpb_circuit modules are now connected!  Note that the modules are essentially black boxes at this point -- we haven't described their internal workings yet!
# Define the inner workings of the CRISPR_Template ModuleDefinition.  The Module contains two interactions, one for complex formation and the other for gene expression.
# We'll start with complex formation...
Cas9ComplexFormation = Interaction(ns, "complex_formation", v, SBO_NONCOVALENT_BINDING)
CRISPRRepression = Interaction(ns, "gene_inhibition", v, SBO_INHIBITION)
TargetProduction = Interaction(ns, "target_production", v, SBO_GENETIC_PRODUCTION)
    
CRISPRTemplate.interactions.add(Cas9ComplexFormation)
CRISPRTemplate.interactions.add(CRISPRRepression)
CRISPRTemplate.interactions.add(TargetProduction)
    
# Here we represent complex formation as the reaction A + B = AB
A = Participation(ns, "A", v, "sys-bio.org/FunctionalComponent/cas9/1.0.0")
B = Participation(ns, "B", v, "sys-bio.org/FunctionalComponent/guide_rna/1.0.0")
AB = Participation(ns, "AB", v, "sys-bio.org/FunctionalComponent/cas9-guide_rna_complex/1.0.0") # Note that this is a weak reference.  The FunctionalComponent it refers to hasn't been created yet!
A.roles.set( SBO_REACTANT )
B.roles.set( SBO_REACTANT )
AB.roles.set( SBO_PRODUCT )

Cas9ComplexFormation.participations.add(A)
Cas9ComplexFormation.participations.add(B)
Cas9ComplexFormation.participations.add(AB)

# Here we define gene expression
target_promoter = FunctionalComponent(ns, "target_promoter", v, TargetPromoter.identity.get(), SBOL_ACCESS_PRIVATE, SBOL_DIRECTION_NONE)
cas9_grna_complex = FunctionalComponent(ns, "cas9_grna_complex", v, Cas9GuideRNAComplex.identity.get(), SBOL_ACCESS_PRIVATE, SBOL_DIRECTION_NONE )
        
TargetProduction.participations.create(ns, "TargetProduction/promoter", v)  # The create method is general and not specialized for every class like libSBOLj's.
TargetProduction.participations.create(ns, "TargetProduction/gene", v)
TargetProduction.participations.create(ns, "TargetProduction/gene_product", v)

# Child objects (corresponding to black diamonds in UML) can be accessed by uri
TargetProduction.participations[ "sys-bio.org/Participation/TargetProduction/promoter/1.0.0" ].roles.set(SBO_PROMOTER)
TargetProduction.participations[ "sys-bio.org/Participation/TargetProduction/gene/1.0.0" ].roles.set(SBO_PROMOTER)
TargetProduction.participations[ "sys-bio.org/Participation/TargetProduction/gene_product/1.0.0" ].roles.set(SBO_PRODUCT)

# Child objects can be dereferenced by numerical index, too.
TargetProduction.participations[ 0 ].participant.setReference(ns, "target_promoter")
TargetProduction.participations[ 1 ].participant.setReference(ns, "target_gene")
TargetProduction.participations[ 2 ].participant.setReference(ns, "target_protein")

CRISPRRepression.participations.create(ns, "CRISPRRepression/inhibitor", v )
CRISPRRepression.participations.create(ns, "CRISPRRepression/promoter", v )
    
CRISPRRepression.participations["sys-bio.org/Participation/CRISPRRepression/inhibitor/1.0.0"].roles.set( SBO_INHIBITOR )
CRISPRRepression.participations["sys-bio.org/Participation/CRISPRRepression/inhibitor/1.0.0"].participant.set( cas9_grna_complex.identity.get() )

CRISPRRepression.participations["sys-bio.org/Participation/CRISPRRepression/promoter/1.0.0"].roles.set( SBO_PROMOTER )
CRISPRRepression.participations["sys-bio.org/Participation/CRISPRRepression/promoter/1.0.0"].participant.set( target_promoter.identity.get() )
    
# Iterate through child objects (indicated by black diamond properties in UML specification)
for participation in Cas9ComplexFormation.participations:
    print (participation.identity.get())
    print (participation.roles.get())
    
# Iterate through references (indicated by white diamond properties in UML specification)
AB.roles.add(SBO + "0000253")  # Appends the synonymous SBO term "non-covalent complex" to the list of roles for this Participation
for role in AB.roles:
    print (role)

# Specify the order of abstract genetic components using SequenceConstraints
TargetPromoter.sequenceConstraints.create(ns, "0", v);
TargetPromoter.sequenceConstraints[0].subject.setReference( ns, "TargetPromoter", v );
TargetPromoter.sequenceConstraints[0].object.setReference( ns, "TargetGene", v );
TargetPromoter.sequenceConstraints[0].restriction.set( SBOL_RESTRICTION_PRECEDES );
    
# CRPbCircuit Module
CRPbPromoterSeq = Sequence(ns, "CRPbPromoterSeq", v, "GCTCCGAATTTCTCGACAGATCTCATGTGATTACGCCAAGCTACGGGCGGAGTACTGTCCTCCGAGCGGAGTACTGTCCTCCGAGCGGAGTACTGTCCTCCGAGCGGAGTACTGTCCTCCGAGCGGAGTTCTGTCCTCCGAGCGGAGACTCTAGATACCTCATCAGGAACATGTTGGAATTCTAGGCGTGTACGGTGGGAGGCCTATATAAGCAGAGCTCGTTTAGTGAACCGTCAGATCGCCTCGAGTACCTCATCAGGAACATGTTGGATCCAATTCGACC", SBOL_ENCODING_IUPAC);
CRPbPromoter.sequence.set( CRPbPromoterSeq.identity.get() );
EYFPSeq = Sequence(ns, "EYFPSequence", v, "atggtgagcaagggcgaggagctgttcaccggggtggtgcccatcctggtcgagctggacggcgacgtaaacggccacaagttcagcgtgtccggcgagggcgagggcgatgccacctacggcaagctgaccctgaagttcatctgcaccaccggcaagctgcccgtgccctggcccaccctcgtgaccaccttcggctacggcctgcaatgcttcgcccgctaccccgaccacatgaagctgcacgacttcttcaagtccgccatgcccgaaggctacgtccaggagcgcaccatcttcttcaaggacgacggcaactacaagacccgcgccgaggtgaagttcgagggcgacaccctggtgaaccgcatcgagctgaagggcatcgacttcaaggaggacggcaacatcctggggcacaagctggagtacaactacaacagccacaacgtctatatcatggccgacaagcagaagaacggcatcaaggtgaacttcaagatccgccacaacatcgaggacggcagcgtgcagctcgccgaccactaccagcagaacacccccatcggcgacggccccgtgctgctgcccgacaaccactacctgagctaccagtccgccctgagcaaagaccccaacgagaagcgcgatcacatggtcctgctggagttcgtgaccgccgccgggatcactctcggcatggacgagctgtacaagtaataa", SBOL_ENCODING_IUPAC)

# Serialize an SBOL file in RDF/XML format
doc = Document()
doc.addModuleDefinition(CRISPRTemplate)
doc.addComponentDefinition(Cas9)
doc.addComponentDefinition(GuideRNA)
doc.addComponentDefinition(Cas9GuideRNAComplex)
doc.addComponentDefinition(TargetPromoter)
doc.addComponentDefinition(TargetGene)
doc.addComponentDefinition(TargetProtein)
    
doc.addModuleDefinition(CRPbCircuit)
doc.addComponentDefinition(Cas9mBFP)
doc.addComponentDefinition(GuideRNAb)
doc.addComponentDefinition(Cas9mBFPGuideRNAComplex)
doc.addComponentDefinition(CRPbPromoter)
doc.addComponentDefinition(EYFPGene)
doc.addComponentDefinition(EYFP)

doc.addSequence(CRPbPromoterSeq)
doc.addSequence(EYFPSeq)

doc.write("CRISPR_example.xml")