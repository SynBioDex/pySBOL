"""
Read an SBOL file and display its contents
"""

# Add SBOL directory to PYTHONPATH
import os, sys
lib_path = os.path.abspath('..')
sys.path.append(lib_path)

import sbol

doc = sbol.Document()
doc.read('test.xml')
print('Total SBOL Objects: %d' %doc.num_sbol_objects)
print('Collections: %d' %len(doc.collections))
print('Components: %d' %len(doc.components))
print('Annotations: %d' %len(doc.annotations))
print('Sequences: %d' %len(doc.sequences))
for obj in doc.collections:
    print obj
for obj in doc.components:
    print obj
for obj in doc.annotations:
    print obj
for obj in doc.sequences:
    print obj
