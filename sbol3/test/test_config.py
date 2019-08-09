import unittest
from sbol3.config import *
from sbol3.moduledefinition import *
from sbol3.componentdefinition import *
from sbol3.sbolerror import *


class TestConfig(unittest.TestCase):

    def test_setOption_invalidOption(self):
        with self.assertRaises(SBOLError):
            Config.setOption('invalid_option', 2)

    def test_setOption_invalidOptionVal(self):
        with self.assertRaises(SBOLError):
            Config.setOption(ConfigOptions.VERBOSE.value, 'Yellow')

    def test_hasHomespace_True(self):
        setHomespace('http://sbols.org/CRISPR_Example/')
        self.assertTrue(hasHomespace())

    def test_hasHomespace_False(self):
        setHomespace('')
        self.assertFalse(hasHomespace())

    def test_openworld_noHomespace(self):
        """See: https://pysbol2.readthedocs.io/en/latest/getting_started.html"""
        setHomespace('')
        Config.setOption('sbol_compliant_uris', False)
        Config.setOption('sbol_typed_uris', False)
        crispr_template = ModuleDefinition('http://sbols.org/CRISPR_Example/CRISPR_Template')
        print(crispr_template)
        self.assertEqual("<http://sbols.org/CRISPR_Example/CRISPR_Template>", str(crispr_template))
        self.assertEqual("<http://sbols.org/CRISPR_Example/CRISPR_Template>", crispr_template.identity.n3())

    def test_openworld_useHomespace(self):
        """See: https://pysbol2.readthedocs.io/en/latest/getting_started.html"""
        # Note: In tutorial CRISPR_Example is followed by a trailing slash.
        # This results in two slashes instead of one in both the original pySBOL
        # and the new code.
        setHomespace('http://sbols.org/CRISPR_Example')
        Config.setOption('sbol_compliant_uris', False)
        Config.setOption('sbol_typed_uris', False)
        crispr_template = ModuleDefinition('CRISPR_Template')
        print(crispr_template)
        self.assertEqual("<http://sbols.org/CRISPR_Example/CRISPR_Template>", str(crispr_template))
        self.assertEqual("<http://sbols.org/CRISPR_Example/CRISPR_Template>", crispr_template.identity.n3())

    def test_SBOLCompliant(self):
        """See: https://pysbol2.readthedocs.io/en/latest/getting_started.html"""
        setHomespace('http://sbols.org/CRISPR_Example')
        Config.setOption('sbol_compliant_uris', True)
        Config.setOption('sbol_typed_uris', False)
        crispr_template = ModuleDefinition('CRISPR_Template')
        print(crispr_template)
        self.assertEqual("<http://sbols.org/CRISPR_Example/CRISPR_Template/1>", str(crispr_template))
        self.assertEqual("<http://sbols.org/CRISPR_Example/CRISPR_Template/1>", crispr_template.identity.n3())

    def test_SBOLCompliant_typed(self):
        """See: https://pysbol2.readthedocs.io/en/latest/getting_started.html"""
        setHomespace('http://sbols.org/CRISPR_Example')
        Config.setOption('sbol_compliant_uris', True)
        Config.setOption('sbol_typed_uris', True)
        crispr_template_md = ModuleDefinition('CRISPR_Template')
        print(crispr_template_md)
        crispr_template_cd = ComponentDefinition('CRISPR_Template')
        print(crispr_template_cd)
        expected_crispr_template_md = "<http://sbols.org/CRISPR_Example/ModuleDefinition/CRISPR_Template/1>"
        expected_crispr_template_cd = "<http://sbols.org/CRISPR_Example/ComponentDefinition/CRISPR_Template/1>"
        self.assertEqual(expected_crispr_template_md, str(crispr_template_md))
        self.assertEqual(expected_crispr_template_md, crispr_template_md.identity.n3())
        self.assertEqual(expected_crispr_template_cd, str(crispr_template_cd))
        self.assertEqual(expected_crispr_template_cd, crispr_template_cd.identity.n3())


if __name__ == '__main__':
    unittest.main()
