import unittest
from sbol3.document import *
from sbol3.config import *
from sbol3.moduledefinition import *
from sbol3.componentdefinition import *
from constants import *


class TestDocument(unittest.TestCase):

    def test_empty_len0(self):
        doc = Document()
        print(doc)
        self.assertEqual(0, len(doc), "Length of document should be 0")

    def test_addGetTopLevel_uri(self):
        doc = Document()
        setHomespace('http://sbols.org/CRISPR_Example')  # Tutorial doesn't drop final forward slash, but this isn't right.
        Config.setOption('sbol_compliant_uris', True)
        Config.setOption('sbol_typed_uris', False)
        crispr_template = ModuleDefinition('CRISPR_Template')
        cas9 = ComponentDefinition('Cas9', BIOPAX_PROTEIN)
        doc.addModuleDefinition(crispr_template)
        doc.addComponentDefinition(cas9)

        crispr_template_2 = doc.getModuleDefinition('http://sbols.org/CRISPR_Example/CRISPR_Template/1')  # Note: tutorial has 1.0.0 instead of 1 but this doesn't work
        cas9_2 = doc.getComponentDefinition('http://sbols.org/CRISPR_Example/Cas9/1')
        self.assertEqual(crispr_template, crispr_template_2)
        self.assertEqual(cas9, cas9_2)

    def test_addGetTopLevel_displayId(self):
        doc = Document()
        setHomespace('http://sbols.org/CRISPR_Example')
        Config.setOption('sbol_compliant_uris', True)
        Config.setOption('sbol_typed_uris', False)
        crispr_template = ModuleDefinition('CRISPR_Template')
        cas9 = ComponentDefinition('Cas9', BIOPAX_PROTEIN)
        doc.addModuleDefinition(crispr_template)
        doc.addComponentDefinition(cas9)

        crispr_template_2 = doc.moduleDefinitions['CRISPR_Template']
        cas9_2 = doc.componentDefinitions['Cas9']
        self.assertEqual(crispr_template, crispr_template_2)
        self.assertEqual(cas9, cas9_2)

    def test_addGetTopLevel_indexing(self):
        doc = Document()
        setHomespace('http://sbols.org/CRISPR_Example')  # Tutorial doesn't drop final forward slash, but this isn't right.
        Config.setOption('sbol_compliant_uris', True)
        Config.setOption('sbol_typed_uris', False)
        crispr_template = ModuleDefinition('CRISPR_Template')
        cas9 = ComponentDefinition('Cas9', BIOPAX_PROTEIN)
        doc.addModuleDefinition(crispr_template)
        doc.addComponentDefinition(cas9)

        crispr_template_2 = doc.moduleDefinitions[0]
        cas9_2 = doc.componentDefinitions[0]
        self.assertEqual(crispr_template, crispr_template_2)
        self.assertEqual(cas9, cas9_2)

    def test_iteration(self):
        doc = Document()
        doc.read('resources/crispr_example.xml')
        i = 0
        for obj in doc:
            i += 1
            print(obj)
        self.assertEqual(len(doc), 31)
        print(doc)

if __name__ == '__main__':
    unittest.main()
