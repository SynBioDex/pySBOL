import unittest
from document import *
from componentdefinition import *
import os, sys

MODULE_LOCATION = os.path.dirname(os.path.abspath(__file__))

class TestComponentDefinitions(unittest.TestCase):

    def setUp(self):
        pass

    def test_typesSet(self):
        cas9 = ComponentDefinition('Cas9', BIOPAX_PROTEIN)  # Constructs a protein component
        self.assertEqual(BIOPAX_PROTEIN, cas9.types)

    def test_typesNotSet(self):
        target_promoter = ComponentDefinition('target_promoter')
        self.assertEqual(BIOPAX_DNA, target_promoter.types)

    def test_multipleRoles(self):
        """pysbol2 - 'Getting, Setting, and Editing Attributes"""
        plasmid = ComponentDefinition('pBB1', BIOPAX_DNA, '1.0.0')
        plasmid.roles = [SO_PLASMID]
        plasmid.roles.append(SO_CIRCULAR)
        self.assertEqual(len(plasmid.roles), 2)
        self.assertTrue(SO_PLASMID in plasmid.roles)
        self.assertTrue(SO_CIRCULAR in plasmid.roles)

    def testAddComponentDefinition(self):
        setHomespace('http://sbols.org/CRISPR_Example')
        Config.setOption('sbol_compliant_uris', True)
        Config.setOption('sbol_typed_uris', False)
        test_CD = ComponentDefinition("BB0001")
        doc = Document()
        doc.addComponentDefinition(test_CD)
        self.assertIsNotNone(doc.componentDefinitions.get("BB0001"))
        displayId = doc.componentDefinitions.get("BB0001").displayId
        self.assertEqual(displayId, "BB0001")

    def testRemoveComponentDefinition(self):
        test_CD = ComponentDefinition("BB0001")
        doc = Document()
        doc.addComponentDefinition(test_CD)
        doc.componentDefinitions.remove(0)
        # NOTE: changed the test to expect the 'sbol error type' as opposed to a RuntimeError.
        self.assertRaises(SBOLError, lambda: doc.componentDefinitions.get("BB0001"))

    def testCDDisplayId(self):
        listCD_read = []
        doc = Document()
        doc.read(os.path.join(MODULE_LOCATION, 'crispr_example.xml'))

        # List of displayIds
        listCD = ['CRP_b', 'CRa_U6', 'EYFP', 'EYFP_cds', 'EYFP_gene', 'Gal4VP16',
                  'Gal4VP16_cds', 'Gal4VP16_gene', 'cas9_gRNA_complex', 'cas9_generic',
                  'cas9m_BFP', 'cas9m_BFP_cds', 'cas9m_BFP_gRNA_b', 'cas9m_BFP_gene',
                  'gRNA_b', 'gRNA_b_gene', 'gRNA_b_nc', 'gRNA_b_terminator',
                  'gRNA_generic', 'mKate', 'mKate_cds', 'mKate_gene', 'pConst',
                  'target', 'target_gene']

        for CD in doc.componentDefinitions:
            listCD_read.append(CD.displayId)

        self.assertSequenceEqual(listCD_read, listCD)
        # Python 3 compatability
        if sys.version_info[0] < 3:
            self.assertItemsEqual(listCD_read, listCD)
        else:
            self.assertCountEqual(listCD_read, listCD)

    def testPrimaryStructureIteration(self):
        listCD = []
        listCD_true = ["R0010", "E0040", "B0032", "B0012"]
        doc = Document()
        gene = ComponentDefinition("BB0001")
        promoter = ComponentDefinition("R0010")
        RBS = ComponentDefinition("B0032")
        CDS = ComponentDefinition("E0040")
        terminator = ComponentDefinition("B0012")

        doc.addComponentDefinition([gene, promoter, RBS, CDS, terminator])

        gene.assemblePrimaryStructure([ promoter, RBS, CDS, terminator ])
        primary_sequence = gene.getPrimaryStructure()
        for component in primary_sequence:
            listCD.append(component.displayId)

        # Python 3 compatability
        if sys.version_info[0] < 3:
            self.assertItemsEqual(listCD, listCD_true)
        else:
            self.assertCountEqual(listCD, listCD_true)


if __name__ == '__main__':
    unittest.main()
