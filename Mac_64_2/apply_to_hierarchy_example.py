from sbol import *

# Assemble module hierarchy
doc = Document()
root = ModuleDefinition('root')
sub = ModuleDefinition('sub')
leaf = ModuleDefinition('leaf')
doc.addModuleDefinition([root, sub, leaf])
root.assemble([sub])
sub.assemble([leaf])


# Define callback which performs an operation on every ModuleDefinition in the hierarchy
def callback(md, params):
    level = params[0]
    print('%s is at level %d in the hierarchy' %(md.displayId, level))
    level += 1
    params[0] = level

# Apply callback
level = 0
params = [ level ]
flattened_module_tree = root.applyToModuleHierarchy(callback, params)
for module in flattened_module_tree:
    print(module)
level = params[0]
print(level)

