import unittest
from sequence import *
from document import *
from config import *
import os, sys
import shutil

MODULE_LOCATION = os.path.dirname(os.path.abspath(__file__))


class TestSequences(unittest.TestCase):

    def setUp(self):
        pass

    def testAddSequence(self):
        test_seq = Sequence("R0010", "ggctgca")
        doc = Document()
        doc.addSequence(test_seq)
        seq = doc.sequences.get("R0010").elements

        self.assertEqual(seq, 'ggctgca')

    def testRemoveSequence(self):
        test_seq = Sequence("R0010", "ggctgca")
        doc = Document()
        doc.addSequence(test_seq)
        doc.sequences.remove(0)
        self.assertRaises(RuntimeError, lambda: doc.sequences.get("R0010"))

    def testSeqDisplayId(self):
        listseq_read = []
        doc = Document()
        doc.read(os.path.join(MODULE_LOCATION, 'crispr_example.xml'))

        # List of displayIds
        listseq = ['CRP_b_seq', 'CRa_U6_seq', 'gRNA_b_seq', 'mKate_seq']

        for seq in doc.sequences:
            listseq_read.append(seq.displayId)

        # Python 3 compatability
        if sys.version_info[0] < 3:
            self.assertItemsEqual(listseq_read, listseq)
        else:
            self.assertCountEqual(listseq_read, listseq)

    def testSequenceElement(self):
        setHomespace('http://sbols.org/CRISPR_Example')
        Config.setOption('sbol_typed_uris', False)
        doc = Document()
        doc.read(os.path.join(MODULE_LOCATION, 'resources/crispr_example.xml'))
        # Sequence to test against
        seq = ('GCTCCGAATTTCTCGACAGATCTCATGTGATTACGCCAAGCTACGGGCGGAGTACTGTCCTC'
               'CGAGCGGAGTACTGTCCTCCGAGCGGAGTACTGTCCTCCGAGCGGAGTACTGTCCTCCGAGC'
               'GGAGTTCTGTCCTCCGAGCGGAGACTCTAGATACCTCATCAGGAACATGTTGGAATTCTAGG'
               'CGTGTACGGTGGGAGGCCTATATAAGCAGAGCTCGTTTAGTGAACCGTCAGATCGCCTCGAG'
               'TACCTCATCAGGAACATGTTGGATCCAATTCGACC')

        seq_read = doc.sequences.get('CRP_b_seq').elements
        self.assertEquals(seq_read, seq)

    def testUpdateSequenceElement(self):
        setHomespace('http://sbols.org/CRISPR_Example')
        Config.setOption('sbol_typed_uris', False)
        doc = Document()
        doc.read(os.path.join(MODULE_LOCATION, 'resources/crispr_example.xml'))
        # Sequence to test against
        seq = 'AAAAA'
        doc.sequences.get('CRP_b_seq').elements = seq
        seq_read = doc.sequences.get('CRP_b_seq').elements
        self.assertEquals(seq_read, seq)

    # File I/O Tests
    def testUpdateWrite(self):
        setHomespace('http://sbols.org/CRISPR_Example')
        Config.setOption('sbol_typed_uris', False)
        doc = Document()
        doc.read(os.path.join(MODULE_LOCATION, 'resources/crispr_example.xml'))
        # Sequence to test against
        seq = 'AAAAA'
        doc.sequences.get('CRP_b_seq').elements = seq
        # Write to disk
        print('WRITING MODIFIED FILE TO DISK')
        doc.write('test.xml')
        # Compare
        print('READING MODIFIED FILE FROM DISK')
        doc2 = Document()  # Document to compare for equality
        doc2.read('test.xml')
        seq_read = doc2.sequences.get('CRP_b_seq').elements
        self.assertEquals(seq_read, seq)


if __name__ == '__main__':
    unittest.main()
