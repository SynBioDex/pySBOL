from sbol import *

Config.setOption('sbol_typed_uris', False)
setHomespace('http://examples.org')

doc = Document()

lacZ = ComponentDefinition('lacZ_cassette', BIOPAX_DNA, '1')
doc.addComponentDefinition(lacZ)

pLac = ComponentDefinition('pLac', BIOPAX_DNA, '1')
doc.addComponentDefinition(pLac)

pLac_comp = lacZ.components.create('pLac_comp')
pLac_comp.definition = pLac.identity

pLac_anno = lacZ.sequenceAnnotations.create('pLac_anno')
pLac_anno.locations.createGenericLocation('pLac_loc')
pLac_anno.component = pLac_comp.identity

setHomespace('http://testing.org')

print(lacZ)
print(lacZ.sequenceAnnotations[0])
print(lacZ.sequenceAnnotations[0].component)

lacZ_copy = lacZ.copy(doc, 'http://examples.org')
print(lacZ_copy)
print(lacZ_copy.sequenceAnnotations[0])
print(lacZ_copy.sequenceAnnotations[0].component)

doc.write('copy_test.xml')
