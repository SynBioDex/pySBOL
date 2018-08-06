""" This example script demonstrates pySBOL's API for genetic design automation. A multi-level abstraction hierarchy is assembled and recursively compiled into a target sequence. """

from sbol import *

setHomespace('http://sys-bio.org')
doc = Document()
doc.displayId = 'example'
doc.name = 'example'
doc.description = 'Example BioBrick assembly for ACS Syn Bio'

igem = PartShop('https://synbiohub.org/public/igem')
igem.pull('BBa_R0010', doc)
igem.pull('BBa_B0032', doc)
igem.pull('BBa_E0040', doc)
igem.pull('BBa_B0012', doc)
igem.pull('pSB1A3', doc)

print(doc)
for obj in doc:
	print (obj)

r0010 = doc.componentDefinitions['BBa_R0010']
b0032 = doc.componentDefinitions['BBa_B0032']
e0040 = doc.componentDefinitions['BBa_E0040']
b0012 = doc.componentDefinitions['BBa_B0012']
backbone = doc.componentDefinitions['pSB1A3']

insert = ComponentDefinition('insert')
vector = ComponentDefinition('vector')

doc.addComponentDefinition(insert)
doc.addComponentDefinition(vector)

insert.assemblePrimaryStructure([ r0010, b0032, e0040, b0012 ], IGEM_STANDARD_ASSEMBLY)
for component in insert.getPrimaryStructure():
	print(component)

vector.assemblePrimaryStructure([backbone, insert])
target_sequence = vector.compile()
print(target_sequence)

result = doc.write('gene_cassette.xml')
print(result)

igem.login(<USERNAME>)  # User must register at https://synbiohub.org
igem.submit(doc)
