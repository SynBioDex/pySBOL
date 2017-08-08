from __future__ import print_function
from sbol import *

setHomespace("http://sbols.org/CRISPR_Example")
toggleSBOLCompliantTypes()
version = "1.0.0"
doc = Document()

cas9_generic = ComponentDefinition("cas9_generic", BIOPAX_PROTEIN, version)
doc.addComponentDefinition(cas9_generic)

gRNA_generic = ComponentDefinition("gRNA_generic", BIOPAX_RNA, version)
gRNA_generic.roles.set(SO_SGRNA)
doc.addComponentDefinition(gRNA_generic)

cas9_gRNA_complex = ComponentDefinition("cas9_gRNA_complex", BIOPAX_COMPLEX, version)
doc.addComponentDefinition(cas9_gRNA_complex)

target_gene = ComponentDefinition("target_gene", BIOPAX_DNA, version)
target_gene.roles.set(SO_PROMOTER)
doc.addComponentDefinition(target_gene)

target = ComponentDefinition("target", BIOPAX_PROTEIN, version)
doc.addComponentDefinition(target)

CRISPR_Template = ModuleDefinition("CRISPR_Template", version)
doc.addModuleDefinition(CRISPR_Template)

Cas9Complex_Formation = CRISPR_Template.interactions.create("cas9_complex_formation")
Cas9Complex_Formation.types.set(SBO_NONCOVALENT_BINDING)

cas9_generic_fc = CRISPR_Template.functionalComponents.create("cas9_generic")
cas9_generic_fc.definition.set(cas9_generic.persistentIdentity.get())
cas9_generic_fc.access.set(SBOL_ACCESS_PUBLIC)
cas9_generic_fc.direction.set(SBOL_DIRECTION_IN_OUT)
cas9_generic_fc.version.set(version)

cas9_generic_participation = Cas9Complex_Formation.participations.create("cas9_generic")
cas9_generic_participation.roles.set(SBO_REACTANT)
cas9_generic_participation.participant.set(cas9_generic_fc.identity.get())

gRNA_generic_fc = CRISPR_Template.functionalComponents.create("gRNA_generic")
gRNA_generic_fc.definition.set(gRNA_generic.persistentIdentity.get())
gRNA_generic_fc.access.set(SBOL_ACCESS_PUBLIC)
gRNA_generic_fc.direction.set(SBOL_DIRECTION_IN_OUT)
gRNA_generic_fc.version.set(version)

gRNA_generic_participation = Cas9Complex_Formation.participations.create("gRNA_generic")
gRNA_generic_participation.roles.set(SBO_REACTANT)
gRNA_generic_participation.participant.set(gRNA_generic_fc.identity.get())

cas9_gRNA_complex_fc = CRISPR_Template.functionalComponents.create("cas9_gRNA_complex")
cas9_gRNA_complex_fc.definition.set(cas9_gRNA_complex.persistentIdentity.get())
cas9_gRNA_complex_fc.access.set(SBOL_ACCESS_PUBLIC)
cas9_gRNA_complex_fc.direction.set(SBOL_DIRECTION_IN_OUT)
cas9_gRNA_complex_fc.version.set(version)

cas9_gRNA_complex_participation = Cas9Complex_Formation.participations.create("cas9_gRNA_complex")
cas9_gRNA_complex_participation.roles.set(SBO_PRODUCT)
cas9_gRNA_complex_participation.participant.set(cas9_gRNA_complex_fc.identity.get())

EYFP_production = CRISPR_Template.interactions.create("target_production")
EYFP_production.types.set(SBO_GENETIC_PRODUCTION)

target_gene_fc = CRISPR_Template.functionalComponents.create("target_gene")
target_gene_fc.definition.set(target_gene.persistentIdentity.get())
target_gene_fc.access.set(SBOL_ACCESS_PUBLIC)
target_gene_fc.direction.set(SBOL_DIRECTION_IN_OUT)
target_gene_fc.version.set(version)

target_gene_participation = EYFP_production.participations.create("target_gene")
target_gene_participation.roles.set(SBO_PROMOTER)
target_gene_participation.participant.set(target_gene_fc.identity.get())

target_fc = CRISPR_Template.functionalComponents.create("target")
target_fc.definition.set(target.persistentIdentity.get())
target_fc.access.set(SBOL_ACCESS_PUBLIC)
target_fc.direction.set(SBOL_DIRECTION_IN_OUT)
target_fc.version.set(version)

target_participation = EYFP_production.participations.create("target")
target_participation.roles.set(SBO_PRODUCT)
target_participation.participant.set(target_fc.identity.get())

target_generic_gene_inhibition = CRISPR_Template.interactions.create("target_gene_inhibition")
target_generic_gene_inhibition.types.set(SBO_INHIBITION)

cas9_gRNA_complex_participation1 = target_generic_gene_inhibition.participations.create("cas9_gRNA_complex")
cas9_gRNA_complex_participation1.roles.set(SBO_INHIBITOR)
cas9_gRNA_complex_participation1.participant.set(cas9_gRNA_complex_fc.identity.get())
	
target_gene_participation2 = target_generic_gene_inhibition.participations.create("target_gene")
target_gene_participation2.roles.set(SBO_PROMOTER)
target_gene_participation2.participant.set(target_gene_fc.identity.get())

CRa_U6_seq_elements = ("GGTTTACCGAGCTCTTATTGGTTTTCAAACTTCATTGACTGTGCC" 
										"AAGGTCGGGCAGGAAGAGGGCCTATTTCCCATGATTCCTTCATAT" 
										"TTGCATATACGATACAAGGCTGTTAGAGAGATAATTAGAATTAAT" 
										"TTGACTGTAAACACAAAGATATTAGTACAAAATACGTGACGTAGA" 
										"AAGTAATAATTTCTTGGGTAGTTTGCAGTTTTAAAATTATGTTTT" 
										"AAAATGGACTATCATATGCTTACCGTAACTTGAAATATAGAACCG" 
										"ATCCTCCCATTGGTATATATTATAGAACCGATCCTCCCATTGGCT" 
										"TGTGGAAAGGACGAAACACCGTACCTCATCAGGAACATGTGTTTA" 
										"AGAGCTATGCTGGAAACAGCAGAAATAGCAAGTTTAAATAAGGCT" 
										"AGTCCGTTATCAACTTGAAAAAGTGGCACCGAGTCGGTGCTTTTT" 
										"TTGGTGCGTTTTTATGCTTGTAGTATTGTATAATGTTTTT")
CRa_U6_seq = Sequence("CRa_U6_seq", CRa_U6_seq_elements, SBOL_ENCODING_IUPAC, version)
doc.addSequence(CRa_U6_seq)

gRNA_b_elements = ("AAGGTCGGGCAGGAAGAGGGCCTATTTCCCATGATTCCTTCATAT" 
		"TTGCATATACGATACAAGGCTGTTAGAGAGATAATTAGAATTAAT" 
		"TTGACTGTAAACACAAAGATATTAGTACAAAATACGTGACGTAGA" 
		"AAGTAATAATTTCTTGGGTAGTTTGCAGTTTTAAAATTATGTTTT" 
		"AAAATGGACTATCATATGCTTACCGTAACTTGAAAGTATTTCGAT" 
		"TTCTTGGCTTTATATATCTTGTGGAAAGGACGAAACACCGTACCT" 
		"CATCAGGAACATGTGTTTAAGAGCTATGCTGGAAACAGCAGAAAT" 
		"AGCAAGTTTAAATAAGGCTAGTCCGTTATCAACTTGAAAAAGTGG" 
		"CACCGAGTCGGTGCTTTTTTT")
gRNA_b_seq = Sequence("gRNA_b_seq", gRNA_b_elements, SBOL_ENCODING_IUPAC, version)
doc.addSequence(gRNA_b_seq)

mKate_seq_elements = ("TCTAAGGGCGAAGAGCTGATTAAGGAGAACATGCACATGAAGCTG" 
		"TACATGGAGGGCACCGTGAACAACCACCACTTCAAGTGCACATCC" 
		"GAGGGCGAAGGCAAGCCCTACGAGGGCACCCAGACCATGAGAATC" 
		"AAGGTGGTCGAGGGCGGCCCTCTCCCCTTCGCCTTCGACATCCTG" 
		"GCTACCAGCTTCATGTACGGCAGCAAAACCTTCATCAACCACACC" 
		"CAGGGCATCCCCGACTTCTTTAAGCAGTCCTTCCCTGAGGTAAGT" 
		"GGTCCTACCTCATCAGGAACATGTGTTTTAGAGCTAGAAATAGCA" 
		"AGTTAAAATAAGGCTAGTCCGTTATCAACTTGAAAAAGTGGCACC" 
		"GAGTCGGTGCTACTAACTCTCGAGTCTTCTTTTTTTTTTTCACAG" 
		"GGCTTCACATGGGAGAGAGTCACCACATACGAAGACGGGGGCGTG" 
		"CTGACCGCTACCCAGGACACCAGCCTCCAGGACGGCTGCCTCATC" 
		"TACAACGTCAAGATCAGAGGGGTGAACTTCCCATCCAACGGCCCT" 
		"GTGATGCAGAAGAAAACACTCGGCTGGGAGGCCTCCACCGAGATG" 
		"CTGTACCCCGCTGACGGCGGCCTGGAAGGCAGAAGCGACATGGCC" 
		"CTGAAGCTCGTGGGCGGGGGCCACCTGATCTGCAACTTGAAGACC" 
		"ACATACAGATCCAAGAAACCCGCTAAGAACCTCAAGATGCCCGGC" 
		"GTCTACTATGTGGACAGAAGACTGGAAAGAATCAAGGAGGCCGAC" 
		"AAAGAGACCTACGTCGAGCAGCACGAGGTGGCTGTGGCCAGATAC" 
		"TGCG")
mKate_seq = Sequence("mKate_seq", mKate_seq_elements, SBOL_ENCODING_IUPAC, version)
doc.addSequence(mKate_seq)

CRP_b_seq_elements = ("GCTCCGAATTTCTCGACAGATCTCATGTGATTACGCCAAGCTACG" 
		"GGCGGAGTACTGTCCTCCGAGCGGAGTACTGTCCTCCGAGCGGAG" 
		"TACTGTCCTCCGAGCGGAGTACTGTCCTCCGAGCGGAGTTCTGTC" 
		"CTCCGAGCGGAGACTCTAGATACCTCATCAGGAACATGTTGGAAT" 
		"TCTAGGCGTGTACGGTGGGAGGCCTATATAAGCAGAGCTCGTTTA" 
		"GTGAACCGTCAGATCGCCTCGAGTACCTCATCAGGAACATGTTGG" 
		"ATCCAATTCGACC")
CRP_b_seq = Sequence("CRP_b_seq", CRP_b_seq_elements, SBOL_ENCODING_IUPAC, version)
doc.addSequence(CRP_b_seq)

pConst = ComponentDefinition("pConst", BIOPAX_DNA, version)
pConst.roles.set(SO_PROMOTER)
doc.addComponentDefinition(pConst)

cas9m_BFP_cds = ComponentDefinition("cas9m_BFP_cds", BIOPAX_DNA, version)
cas9m_BFP_cds.roles.set(SO_CDS)
doc.addComponentDefinition(cas9m_BFP_cds)

cas9m_BFP_gene = ComponentDefinition("cas9m_BFP_gene", BIOPAX_DNA, version)
cas9m_BFP_gene.roles.set(SO_PROMOTER)
doc.addComponentDefinition(cas9m_BFP_gene)

pConst_c2 = cas9m_BFP_gene.components.create("pConst")
pConst_c2.definition.set(pConst.persistentIdentity.get())
pConst_c2.access.set(SBOL_ACCESS_PUBLIC)
pConst_c2.version.set(version)

cas9m_BFP_cds_c = cas9m_BFP_gene.components.create("cas9m_BFP_cds")
cas9m_BFP_cds_c.definition.set(cas9m_BFP_cds.persistentIdentity.get())
cas9m_BFP_cds_c.access.set(SBOL_ACCESS_PUBLIC)
cas9m_BFP_cds_c.version.set(version)

cas9m_BFP_gene_constraint = cas9m_BFP_gene.sequenceConstraints.create("cas9m_BFP_gene_constraint")
cas9m_BFP_gene_constraint.subject.set(pConst_c2.identity.get())
cas9m_BFP_gene_constraint.object.set(cas9m_BFP_cds_c.identity.get())
cas9m_BFP_gene_constraint.restriction.set(SBOL_RESTRICTION_PRECEDES)

cas9m_BFP = ComponentDefinition("cas9m_BFP", BIOPAX_PROTEIN, version)
doc.addComponentDefinition(cas9m_BFP)

CRa_U6 = ComponentDefinition("CRa_U6", BIOPAX_DNA, version)
CRa_U6.sequences.add(CRa_U6_seq.persistentIdentity.get())
CRa_U6.roles.set(SO_PROMOTER)
doc.addComponentDefinition(CRa_U6)

gRNA_b_nc = ComponentDefinition("gRNA_b_nc", BIOPAX_DNA, version)
gRNA_b_nc.roles.set(SO_CDS)
gRNA_b_nc.sequences.add(gRNA_b_seq.persistentIdentity.get())
doc.addComponentDefinition(gRNA_b_nc)

gRNA_b_terminator = ComponentDefinition("gRNA_b_terminator", BIOPAX_DNA, version)
gRNA_b_terminator.roles.set(SO_TERMINATOR)
doc.addComponentDefinition(gRNA_b_terminator)

gRNA_b_gene = ComponentDefinition("gRNA_b_gene", BIOPAX_DNA, version)
gRNA_b_gene.roles.set(SO_PROMOTER)
doc.addComponentDefinition(gRNA_b_gene)

CRa_U6_c = gRNA_b_gene.components.create("CRa_U6")
CRa_U6_c.definition.set(CRa_U6.persistentIdentity.get())
CRa_U6_c.access.set(SBOL_ACCESS_PUBLIC)
CRa_U6_c.version.set(version)

gRNA_b_nc_c = gRNA_b_gene.components.create("gRNA_b_nc")
gRNA_b_nc_c.definition.set(gRNA_b_nc.persistentIdentity.get())
gRNA_b_nc_c.access.set(SBOL_ACCESS_PUBLIC)
gRNA_b_nc_c.version.set(version)

gRNA_b_terminator_c = gRNA_b_gene.components.create("gRNA_b_terminator")
gRNA_b_terminator_c.definition.set(gRNA_b_terminator.persistentIdentity.get())
gRNA_b_terminator_c.access.set(SBOL_ACCESS_PUBLIC)
gRNA_b_terminator_c.version.set(version)

gRNA_gene_constraint1 = gRNA_b_gene.sequenceConstraints.create("gRNA_b_gene_constraint1")
gRNA_gene_constraint1.subject.set(CRa_U6_c.identity.get())
gRNA_gene_constraint1.object.set(gRNA_b_nc_c.identity.get())
gRNA_gene_constraint1.restriction.set(SBOL_RESTRICTION_PRECEDES)

gRNA_gene_constraint2 = gRNA_b_gene.sequenceConstraints.create("gRNA_b_gene_constraint2")
gRNA_gene_constraint2.subject.set(gRNA_b_nc_c.identity.get())
gRNA_gene_constraint2.object.set(gRNA_b_terminator_c.identity.get())
gRNA_gene_constraint2.restriction.set(SBOL_RESTRICTION_PRECEDES)

gRNA_b = ComponentDefinition("gRNA_b", BIOPAX_RNA, version)
gRNA_b.roles.set(SO_SGRNA)
doc.addComponentDefinition(gRNA_b)

cas9m_BFP_gRNA_b = ComponentDefinition("cas9m_BFP_gRNA_b", BIOPAX_COMPLEX, version)
doc.addComponentDefinition(cas9m_BFP_gRNA_b)

mKate_cds = ComponentDefinition("mKate_cds", BIOPAX_DNA, version)
mKate_cds.roles.set(SO_CDS)
mKate_cds.sequences.add(mKate_seq.persistentIdentity.get())
doc.addComponentDefinition(mKate_cds)

mKate_gene = ComponentDefinition("mKate_gene", BIOPAX_DNA, version)
mKate_gene.roles.set(SO_PROMOTER)
doc.addComponentDefinition(mKate_gene)

pConst_c = mKate_gene.components.create("pConst")
pConst_c.definition.set(pConst.persistentIdentity.get())
pConst_c.access.set(SBOL_ACCESS_PUBLIC)
pConst_c.version.set(version)

mKate_cds_c = mKate_gene.components.create("mKate_cds")
mKate_cds_c.definition.set(mKate_cds.persistentIdentity.get())
mKate_cds_c.access.set(SBOL_ACCESS_PUBLIC)
mKate_cds_c.version.set(version)

mKate_gene_constraint = mKate_gene.sequenceConstraints.create("mKate_gene_constraint")
mKate_gene_constraint.subject.set(pConst_c.identity.get())
mKate_gene_constraint.object.set(mKate_cds_c.identity.get())
mKate_gene_constraint.restriction.set(SBOL_RESTRICTION_PRECEDES)

mKate = ComponentDefinition("mKate", BIOPAX_PROTEIN, version)
doc.addComponentDefinition(mKate)

Gal4VP16_cds = ComponentDefinition("Gal4VP16_cds", BIOPAX_DNA, version)
Gal4VP16_cds.roles.set(SO_CDS)
doc.addComponentDefinition(Gal4VP16_cds)

Gal4VP16_gene = ComponentDefinition("Gal4VP16_gene", BIOPAX_DNA, version)
Gal4VP16_gene.roles.set(SO_PROMOTER)
doc.addComponentDefinition(Gal4VP16_gene)

pConst_c3 = Gal4VP16_gene.components.create("pConst")
pConst_c3.definition.set(pConst.persistentIdentity.get())
pConst_c3.access.set(SBOL_ACCESS_PUBLIC)
pConst_c3.version.set(version)

Gal4VP16_cds_c = Gal4VP16_gene.components.create("Gal4VP16_cds")
Gal4VP16_cds_c.definition.set(Gal4VP16_cds.persistentIdentity.get())
Gal4VP16_cds_c.access.set(SBOL_ACCESS_PUBLIC)
Gal4VP16_cds_c.version.set(version)

GAL4VP16_gene_constraint = Gal4VP16_gene.sequenceConstraints.create("GAL4VP16_gene_constraint")
GAL4VP16_gene_constraint.subject.set(pConst_c3.identity.get())
GAL4VP16_gene_constraint.object.set(Gal4VP16_cds_c.identity.get())
GAL4VP16_gene_constraint.restriction.set(SBOL_RESTRICTION_PRECEDES)

Gal4VP16 = ComponentDefinition("Gal4VP16", BIOPAX_PROTEIN, version)
doc.addComponentDefinition(Gal4VP16)

CRP_b = ComponentDefinition("CRP_b", BIOPAX_DNA, version)
CRP_b.roles.set(SO_PROMOTER)
CRP_b.sequences.add(CRP_b_seq.persistentIdentity.get())
doc.addComponentDefinition(CRP_b)

EYFP_cds = ComponentDefinition("EYFP_cds", BIOPAX_DNA, version)
EYFP_cds.roles.set(SO_CDS)
doc.addComponentDefinition(EYFP_cds)

EYFP_gene =  ComponentDefinition("EYFP_gene", BIOPAX_DNA, version)
EYFP_gene.roles.set(SO_PROMOTER)
doc.addComponentDefinition(EYFP_gene)

CRP_b_c = EYFP_gene.components.create("CRP_b")
CRP_b_c.definition.set(CRP_b.persistentIdentity.get())
CRP_b_c.access.set(SBOL_ACCESS_PUBLIC)
CRP_b_c.version.set(version)

EYFP_cds_c = EYFP_gene.components.create("EYFP_cds")
EYFP_cds_c.definition.set(EYFP_cds.persistentIdentity.get())
EYFP_cds_c.access.set(SBOL_ACCESS_PUBLIC)
EYFP_cds_c.version.set(version)

EYFP_gene_constraint = EYFP_gene.sequenceConstraints.create("EYFP_gene_constraint")
EYFP_gene_constraint.subject.set(CRP_b_c.identity.get())
EYFP_gene_constraint.object.set(EYFP_cds_c.identity.get())
EYFP_gene_constraint.restriction.set(SBOL_RESTRICTION_PRECEDES)

EYFP =  ComponentDefinition("EYFP", BIOPAX_PROTEIN, version)
doc.addComponentDefinition(EYFP)

CRPb_circuit =  ModuleDefinition("CRPb_characterization_Circuit", version)
doc.addModuleDefinition(CRPb_circuit)

cas9m_BFP_fc = CRPb_circuit.functionalComponents.create("cas9m_BFP")
cas9m_BFP_fc.definition.set(cas9m_BFP.identity.get())
cas9m_BFP_fc.access.set(SBOL_ACCESS_PRIVATE)
cas9m_BFP_fc.direction.set(SBOL_DIRECTION_NONE)
cas9m_BFP_fc.version.set(version)

cas9m_BFP_gene_fc = CRPb_circuit.functionalComponents.create("cas9m_BFP_gene")
cas9m_BFP_gene_fc.definition.set(cas9m_BFP_gene.identity.get())
cas9m_BFP_gene_fc.access.set(SBOL_ACCESS_PRIVATE)
cas9m_BFP_gene_fc.direction.set(SBOL_DIRECTION_NONE)
cas9m_BFP_gene_fc.version.set(version)

gRNA_b_fc = CRPb_circuit.functionalComponents.create("gRNA_b")
gRNA_b_fc.definition.set(gRNA_b.identity.get())
gRNA_b_fc.access.set(SBOL_ACCESS_PRIVATE)
gRNA_b_fc.direction.set(SBOL_DIRECTION_NONE)
gRNA_b_fc.version.set(version)
	
gRNA_b_gene_fc = CRPb_circuit.functionalComponents.create("gRNA_b_gene")
gRNA_b_gene_fc.definition.set(gRNA_b_gene.identity.get())
gRNA_b_gene_fc.access.set(SBOL_ACCESS_PRIVATE)
gRNA_b_gene_fc.direction.set(SBOL_DIRECTION_NONE)
gRNA_b_gene_fc.version.set(version)

mKate_fc = CRPb_circuit.functionalComponents.create("mKate")
mKate_fc.definition.set(mKate.identity.get())
mKate_fc.access.set(SBOL_ACCESS_PRIVATE)
mKate_fc.direction.set(SBOL_DIRECTION_NONE)
mKate_fc.version.set(version)
	
mKate_gene_fc = CRPb_circuit.functionalComponents.create("mKate_gene")
mKate_gene_fc.definition.set(mKate_gene.identity.get())
mKate_gene_fc.access.set(SBOL_ACCESS_PRIVATE)
mKate_gene_fc.direction.set(SBOL_DIRECTION_NONE)
mKate_gene_fc.version.set(version)

Gal4VP16_fc = CRPb_circuit.functionalComponents.create("Gal4VP16")
Gal4VP16_fc.definition.set(Gal4VP16.identity.get())
Gal4VP16_fc.access.set(SBOL_ACCESS_PRIVATE)
Gal4VP16_fc.direction.set(SBOL_DIRECTION_NONE)
Gal4VP16_fc.version.set(version)

Gal4VP16_gene_fc = CRPb_circuit.functionalComponents.create("Gal4VP16_gene")
Gal4VP16_gene_fc.definition.set(Gal4VP16_gene.identity.get())
Gal4VP16_gene_fc.access.set(SBOL_ACCESS_PRIVATE)
Gal4VP16_gene_fc.direction.set(SBOL_DIRECTION_NONE)
Gal4VP16_gene_fc.version.set(version)

EYFP_fc = CRPb_circuit.functionalComponents.create("EYFP")
EYFP_fc.definition.set(EYFP.identity.get())
EYFP_fc.access.set(SBOL_ACCESS_PRIVATE)
EYFP_fc.direction.set(SBOL_DIRECTION_NONE)
EYFP_fc.version.set(version)

EYFP_gene_fc = CRPb_circuit.functionalComponents.create("EYFP_gene")
EYFP_gene_fc.definition.set(EYFP_gene.identity.get())
EYFP_gene_fc.access.set(SBOL_ACCESS_PRIVATE)
EYFP_gene_fc.direction.set(SBOL_DIRECTION_NONE)
EYFP_gene_fc.version.set(version)

cas9m_BFP_gRNA_b_fc = CRPb_circuit.functionalComponents.create("cas9m_BFP_gRNA_b")
cas9m_BFP_gRNA_b_fc.definition.set(cas9m_BFP_gRNA_b.identity.get())
cas9m_BFP_gRNA_b_fc.access.set(SBOL_ACCESS_PRIVATE)
cas9m_BFP_gRNA_b_fc.direction.set(SBOL_DIRECTION_NONE)
cas9m_BFP_gRNA_b_fc.version.set(version)

mKate_production = CRPb_circuit.interactions.create("mKate_production") 
mKate_production.types.set(SBO_GENETIC_PRODUCTION)

mKate_participation = mKate_production.participations.create("mKate")
mKate_participation.roles.set(SBO_PRODUCT)
mKate_participation.participant.set(mKate_fc.identity.get())

mKate_gene_participation = mKate_production.participations.create("mKate_gene") 
mKate_gene_participation.roles.set(SBO_PROMOTER)
mKate_gene_participation.participant.set(mKate_gene_fc.identity.get())

GAL4VP16_production = CRPb_circuit.interactions.create("Gal4VP16_production") 
GAL4VP16_production.types.set(SBO_GENETIC_PRODUCTION)

Gal4VP16_gene_participation = GAL4VP16_production.participations.create("Gal4VP16_gene") 
Gal4VP16_gene_participation.roles.set(SBO_PROMOTER)
Gal4VP16_gene_participation.participant.set(Gal4VP16_gene_fc.identity.get())

Gal4VP16_participation1 = GAL4VP16_production.participations.create("Gal4VP16") 
Gal4VP16_participation1.roles.set(SBO_PRODUCT)
Gal4VP16_participation1.participant.set(Gal4VP16_fc.identity.get())

cas9m_BFP_production = CRPb_circuit.interactions.create("cas9m_BFP_production") 
cas9m_BFP_production.types.set(SBO_GENETIC_PRODUCTION)

cas9m_BFP_gene_participation = cas9m_BFP_production.participations.create("cas9m_BFP_gene") 
cas9m_BFP_gene_participation.roles.set(SBO_PROMOTER)
cas9m_BFP_gene_participation.participant.set(cas9m_BFP_gene_fc.identity.get())

cas9m_BFP_participation = cas9m_BFP_production.participations.create("cas9m_BFP") 
cas9m_BFP_participation.roles.set(SBO_PRODUCT)
cas9m_BFP_participation.participant.set(cas9m_BFP_fc.identity.get())

gRNA_b_production = CRPb_circuit.interactions.create("gRNA_b_production") 
gRNA_b_production.types.set(SBO_GENETIC_PRODUCTION)

gRNA_b_gene_participation = gRNA_b_production.participations.create("gRNA_b_gene") 
gRNA_b_gene_participation.roles.set(SBO_PROMOTER)
gRNA_b_gene_participation.participant.set(gRNA_b_gene_fc.identity.get())

gRNA_b_participation = gRNA_b_production.participations.create("gRNA_b") 
gRNA_b_participation.roles.set(SBO_PRODUCT)
gRNA_b_participation.participant.set(gRNA_b_fc.identity.get())

EYFP_Activation = CRPb_circuit.interactions.create("EYFP_Activation") 
EYFP_Activation.types.set(SBO_STIMULATION)

Gal4VP16_participation = EYFP_Activation.participations.create("Gal4VP16") 
Gal4VP16_participation.roles.set(SBO_STIMULATOR)
Gal4VP16_participation.participant.set(Gal4VP16_fc.identity.get())

EYFP_gene_participation = EYFP_Activation.participations.create("EYFP_gene") 
EYFP_gene_participation.roles.set(SBO_PROMOTER)
EYFP_gene_participation.participant.set(EYFP_gene_fc.identity.get())

mKate_deg = CRPb_circuit.interactions.create("mKate_deg") 
mKate_deg.types.set(SBO_DEGRADATION) 

mKate_participation1 = mKate_deg.participations.create("mKate") 
mKate_participation1.roles.set(SBO_REACTANT)
mKate_participation1.participant.set(mKate_fc.identity.get())

GAL4VP16_deg = CRPb_circuit.interactions.create("Gal4VP16_deg") 
GAL4VP16_deg.types.set(SBO_DEGRADATION)

Gal4VP16_participation2 = GAL4VP16_deg.participations.create("Gal4VP16")
Gal4VP16_participation2.roles.set(SBO_REACTANT)
Gal4VP16_participation2.participant.set(Gal4VP16_fc.identity.get())

cas9m_BFP_deg = CRPb_circuit.interactions.create("cas9m_BFP_deg") 
cas9m_BFP_deg.types.set(SBO_DEGRADATION)

cas9m_BFP_participation1 = cas9m_BFP_deg.participations.create("cas9m_BFP")
cas9m_BFP_participation1.roles.set(SBO_REACTANT)
cas9m_BFP_participation1.participant.set(cas9m_BFP_fc.identity.get())

gRNA_b_deg = CRPb_circuit.interactions.create("gRNA_b_deg") 
gRNA_b_deg.types.set(SBO_DEGRADATION)

gRNA_b_participation1 = gRNA_b_deg.participations.create("gRNA_b")
gRNA_b_participation1.roles.set(SBO_REACTANT)
gRNA_b_participation1.participant.set(gRNA_b_fc.identity.get())

EYFP_deg = CRPb_circuit.interactions.create("EYFP_deg")
EYFP_deg.types.set(SBO_DEGRADATION)

EYFP_participation = EYFP_deg.participations.create("EYFP")
EYFP_participation.roles.set(SBO_REACTANT)
EYFP_participation.participant.set(EYFP_fc.identity.get())

cas9m_BFP_gRNA_b_deg = CRPb_circuit.interactions.create("cas9m_BFP_gRNA_b_deg") 
cas9m_BFP_gRNA_b_deg.types.set(SBO_DEGRADATION)

cas9m_BFP_gRNA_b_participation = cas9m_BFP_gRNA_b_deg.participations.create("cas9m_BFP_gRNA_b")
cas9m_BFP_gRNA_b_participation.roles.set(SBO_REACTANT)
cas9m_BFP_gRNA_b_participation.participant.set(cas9m_BFP_gRNA_b_fc.identity.get())

Template_Module = CRPb_circuit.modules.create("CRISPR_Template")
Template_Module.definition.set(CRISPR_Template.identity.get())

cas9m_BFP_map = Template_Module.mapsTos.create("cas9m_BFP_map")
cas9m_BFP_map.refinement.set(SBOL_REFINEMENT_USE_LOCAL)
cas9m_BFP_map.local.set(cas9m_BFP_fc.identity.get())
cas9m_BFP_map.remote.set(cas9_generic_fc.identity.get())

gRNA_b_map = Template_Module.mapsTos.create("gRNA_b_map")
gRNA_b_map.refinement.set(SBOL_REFINEMENT_USE_LOCAL)
gRNA_b_map.local.set(gRNA_b_fc.identity.get())
gRNA_b_map.remote.set(gRNA_generic_fc.identity.get())

cas9m_BFP_gRNA_map = Template_Module.mapsTos.create("cas9m_BFP_gRNA_map")
cas9m_BFP_gRNA_map.refinement.set(SBOL_REFINEMENT_USE_LOCAL)
cas9m_BFP_gRNA_map.local.set(cas9m_BFP_gRNA_b_fc.identity.get())
cas9m_BFP_gRNA_map.remote.set(cas9_gRNA_complex_fc.identity.get())

EYFP_map = Template_Module.mapsTos.create("EYFP_map")
EYFP_map.refinement.set(SBOL_REFINEMENT_USE_LOCAL)
EYFP_map.local.set(EYFP_fc.identity.get())
EYFP_map.remote.set(target_fc.identity.get())

EYFP_gene_map = Template_Module.mapsTos.create("EYFP_gene_map")
EYFP_gene_map.refinement.set(SBOL_REFINEMENT_USE_LOCAL)
EYFP_gene_map.local.set(EYFP_gene_fc.identity.get())
EYFP_gene_map.remote.set(target_gene_fc.identity.get())

doc.write("new_example1.xml")
