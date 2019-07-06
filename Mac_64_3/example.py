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
#print(gene.sequence.elements)

result = doc.write('gene_cassette.xml')
print(result)
