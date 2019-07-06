from sbol import *

doc = Document()
nand_gate = ModuleDefinition('nand_gate')
not_gate = ModuleDefinition('not_gate')
tumor_killer = ModuleDefinition('tumor_killer')
doc.addModuleDefinition([nand_gate, not_gate, tumor_killer])

# Assemble tumor killer circuit out of nand and not gates
tumor_killer.assemble([nand_gate, not_gate])

# In order to connect these black boxes, their inputs and outputs must be defined. The following process defines an interface for the modules, while their internal workings still remain abstract. First, configure the NAND gate
tissue_marker = ComponentDefinition('tissue_marker', BIOPAX_PROTEIN)
tumor_marker = ComponentDefinition('tumor_marker', BIOPAX_RNA)
lacI = ComponentDefinition('lacI', BIOPAX_PROTEIN)
doc.addComponentDefinition([tissue_marker, tumor_marker, lacI])

nand_input1 = nand_gate.setInput(tissue_marker)
nand_input2 = nand_gate.setInput(tumor_marker)
nand_output = nand_gate.setOutput(lacI)
# Next configure the NOT gate. Note that LacI's ComponentDefinition was already defined above.

hBax = ComponentDefinition('hBax', BIOPAX_PROTEIN)
doc.addComponentDefinition(hBax)
not_input = not_gate.setInput(lacI)
not_output = nand_gate.setOutput(hBax)

# Finally, these two modules can be connected with a metaphorical, yet very satisfying, "click"."
nand_output.connect(not_input)
doc.write('intermodular_interactions.xml')
