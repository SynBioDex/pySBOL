import unittest
from sbol3.config import *
from sbol3.moduledefinition import *


class TestIdentified(unittest.TestCase):

    def test_getDisplayId_SBOLCompliant(self):
        setHomespace('http://sbols.org/CRISPR_Example')
        Config.setOption('sbol_compliant_uris', True)
        Config.setOption('sbol_typed_uris', False)
        crispr_template = ModuleDefinition('CRISPR_Template')
        self.assertEqual('CRISPR_Template', crispr_template.displayId)

    def test_getPersistentIdentity_SBOLCompliant(self):
        setHomespace('http://sbols.org/CRISPR_Example')
        Config.setOption('sbol_compliant_uris', True)
        Config.setOption('sbol_typed_uris', False)
        crispr_template = ModuleDefinition('CRISPR_Template')
        self.assertEqual('http://sbols.org/CRISPR_Example/CRISPR_Template', crispr_template.persistentIdentity)

    def test_getVersion_SBOLCompliant(self):
        setHomespace('http://sbols.org/CRISPR_Example')
        Config.setOption('sbol_compliant_uris', True)
        Config.setOption('sbol_typed_uris', False)
        crispr_template = ModuleDefinition('CRISPR_Template')
        self.assertEqual('1', crispr_template.version)

    def test_setDisplayId_SBOLCompliant(self):
        setHomespace('http://sbols.org/CRISPR_Example')
        Config.setOption('sbol_compliant_uris', True)
        Config.setOption('sbol_typed_uris', False)
        crispr_template = ModuleDefinition('CRISPR_Template')
        crispr_template.displayId = 'test'
        self.assertEqual('test', crispr_template.displayId)

    def test_setPersistentIdentity_SBOLCompliant(self):
        setHomespace('http://sbols.org/CRISPR_Example')
        Config.setOption('sbol_compliant_uris', True)
        Config.setOption('sbol_typed_uris', False)
        crispr_template = ModuleDefinition('CRISPR_Template')
        crispr_template.persistentIdentity = 'test'
        self.assertEqual('test', crispr_template.persistentIdentity)

    def test_setVersion_SBOLCompliant(self):
        setHomespace('http://sbols.org/CRISPR_Example')
        Config.setOption('sbol_compliant_uris', True)
        Config.setOption('sbol_typed_uris', False)
        crispr_template = ModuleDefinition('CRISPR_Template')
        crispr_template.version = '2'
        self.assertEqual('2', crispr_template.version)

    def test_getDisplayId_hasHomespace(self):
        setHomespace('http://sbols.org/CRISPR_Example')
        Config.setOption('sbol_compliant_uris', False)
        Config.setOption('sbol_typed_uris', False)
        crispr_template = ModuleDefinition('CRISPR_Template')
        self.assertEqual(None, crispr_template.displayId)

    def test_getPersistentIdentity_hasHomespace(self):
        setHomespace('http://sbols.org/CRISPR_Example')
        Config.setOption('sbol_compliant_uris', False)
        Config.setOption('sbol_typed_uris', False)
        crispr_template = ModuleDefinition('CRISPR_Template')
        self.assertEqual('http://sbols.org/CRISPR_Example/CRISPR_Template', crispr_template.persistentIdentity)

    def test_getVersion_hasHomespace(self):
        setHomespace('http://sbols.org/CRISPR_Example')
        Config.setOption('sbol_compliant_uris', False)
        Config.setOption('sbol_typed_uris', False)
        crispr_template = ModuleDefinition('CRISPR_Template')
        self.assertEqual('1', crispr_template.version)

    def test_setPersistentIdentity_hasHomespace(self):
        setHomespace('http://sbols.org/CRISPR_Example')
        Config.setOption('sbol_compliant_uris', False)
        Config.setOption('sbol_typed_uris', False)
        crispr_template = ModuleDefinition('CRISPR_Template')
        crispr_template.persistentIdentity = 'test'
        self.assertEqual('test', crispr_template.persistentIdentity)

    def test_setVersion_hasHomespace(self):
        setHomespace('http://sbols.org/CRISPR_Example')
        Config.setOption('sbol_compliant_uris', False)
        Config.setOption('sbol_typed_uris', False)
        crispr_template = ModuleDefinition('CRISPR_Template')
        crispr_template.version = '2'
        self.assertEqual('2', crispr_template.version)


if __name__ == '__main__':
    unittest.main()
