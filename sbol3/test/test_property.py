import unittest
from sbol3.componentdefinition import ComponentDefinition
from sbol3.document import Document
from sbol3.constants import *
from sbol3.config import *
import os

MODULE_LOCATION = os.path.dirname(os.path.abspath(__file__))
TEST_LOCATION = os.path.join(MODULE_LOCATION, 'resources', 'crispr_example.xml')


class TestProperty(unittest.TestCase):
    def test_listProperty(self):
        plasmid = ComponentDefinition('pBB1', BIOPAX_DNA, '1.0.0')
        plasmid.roles = [SO_PLASMID, SO_CIRCULAR]
        self.assertEqual(len(plasmid.roles), 2)

    def test_noListProperty(self):
        plasmid = ComponentDefinition('pBB1', BIOPAX_DNA, '1.0.0')
        with self.assertRaises(TypeError):
            plasmid.version = ['1', '2']

    def test_addPropertyToList(self):
        plasmid = ComponentDefinition('pBB1', BIOPAX_DNA, '1.0.0')
        plasmid.roles = [SO_PLASMID]
        plasmid.addRole(SO_CIRCULAR)
        self.assertEqual(len(plasmid.roles), 2)

    def test_removePropertyFromList(self):
        plasmid = ComponentDefinition('pBB1', BIOPAX_DNA, '1.0.0')
        plasmid.roles = [SO_PLASMID, SO_CIRCULAR]
        plasmid.removeRole()
        self.assertEqual(len(plasmid.roles), 1)

    def test_lenOwnedObject(self):
        d = Document()
        d.read(TEST_LOCATION)
        self.assertEqual(25, len(d.componentDefinitions))
        self.assertEqual(2, len(d.moduleDefinitions))
        self.assertEqual(4, len(d.sequences))

    def test_getitem(self):
        setHomespace('http://sbols.org/CRISPR_Example/')
        d = Document()
        d.read(TEST_LOCATION)
        s1 = d.sequences['CRa_U6_seq']
        self.assertEqual('http://sbols.org/CRISPR_Example/CRa_U6_seq/1.0.0', str(s1))


if __name__ == '__main__':
    unittest.main()
