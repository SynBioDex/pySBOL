import unittest
from sbol import *
import random
import string
import os
import sys

#####################
# utility functions
#####################

URIS_USED = set()
RANDOM_CHARS = string.ascii_letters
NUM_FAST_TESTS = 10000
NUM_SLOW_TESTS =   100
TEST_LOCATION = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test')
TEST_LOC_SBOL1 = os.path.join(TEST_LOCATION, 'SBOL1')
TEST_LOC_SBOL2 = os.path.join(TEST_LOCATION, 'SBOL2')
TEST_LOC_RDF = os.path.join(TEST_LOCATION, 'RDF')
TEST_LOC_Invalid = os.path.join(TEST_LOCATION, 'InvalidFiles')
TEST_LOC_GB = os.path.join(TEST_LOCATION, 'GenBank')
TEST_FILES_SBOL2 = os.listdir(TEST_LOC_SBOL2)

def random_string(limit=10):
    length = random.randint(0, limit)
    string = ''.join(random.choice(RANDOM_CHARS) for n in range(length))
    return string

def random_uri(limit=10):
    while True:
        uri = random_string()
        global URIS_USED
        if not uri in URIS_USED:
            URIS_USED.add(uri)
            return uri

def random_valid_position(limit=1000):
    return random.randint(0, limit)

def random_invalid_position(limit=1000):
    position = 0
    while position == 0:
        position = -1 * random_valid_position(limit)
    return position

##############
# unit tests
##############

#class TestParse(unittest.TestCase):

#class TestWrite(unittest.TestCase):

class TestRoundTripSBOL2(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run_round_trip(self, test_file):
        if test_file.endswith('xml'):
            file_format = '.xml'
        elif test_file.endswith('rdf'):
            file_format = '.rdf'
        self.doc = Document()   # Document for read and write
        self.doc.read(os.path.join(TEST_LOC_SBOL2, os.path.splitext(test_file)[0] + file_format))
        self.doc.write(os.path.join(TEST_LOC_SBOL2, os.path.splitext(test_file)[0] + '_out' + file_format))

        self.doc2 = Document()  # Document to compare for equality
        self.doc2.read(os.path.join(TEST_LOC_SBOL2, os.path.splitext(test_file)[0] + '_out' + file_format))
        self.assertEqual(self.doc.compare(self.doc2), 1)
        os.remove(os.path.join(TEST_LOC_SBOL2, os.path.splitext(test_file)[0] + '_out' + file_format))
    
    def test_case00(self):
        print(str(TEST_FILES_SBOL2[0]))
        self.run_round_trip(str(TEST_FILES_SBOL2[0]))

    def test_case01(self):
        print(str(TEST_FILES_SBOL2[1]))
        self.run_round_trip(str(TEST_FILES_SBOL2[1]))

    def test_case02(self):
        print(str(TEST_FILES_SBOL2[2]))
        self.run_round_trip(str(TEST_FILES_SBOL2[2]))

    def test_case03(self):
        print(str(TEST_FILES_SBOL2[3]))
        self.run_round_trip(str(TEST_FILES_SBOL2[3]))

    def test_case04(self):
        print(str(TEST_FILES_SBOL2[4]))
        self.run_round_trip(str(TEST_FILES_SBOL2[4]))

    def test_case05(self):
        print(str(TEST_FILES_SBOL2[5]))
        self.run_round_trip(str(TEST_FILES_SBOL2[5]))

    def test_case06(self):
        print(str(TEST_FILES_SBOL2[6]))
        self.run_round_trip(str(TEST_FILES_SBOL2[6]))

    def test_case07(self):
        print(str(TEST_FILES_SBOL2[7]))
        self.run_round_trip(str(TEST_FILES_SBOL2[7]))

    def test_case08(self):
        print(str(TEST_FILES_SBOL2[8]))
        self.run_round_trip(str(TEST_FILES_SBOL2[8]))

    def test_case09(self):
        print(str(TEST_FILES_SBOL2[9]))
        self.run_round_trip(str(TEST_FILES_SBOL2[9]))

    def test_case10(self):
        print(str(TEST_FILES_SBOL2[10]))
        self.run_round_trip(str(TEST_FILES_SBOL2[10]))

    def test_case11(self):
        print(str(TEST_FILES_SBOL2[11]))
        self.run_round_trip(str(TEST_FILES_SBOL2[11]))

    def test_case12(self):
        print(str(TEST_FILES_SBOL2[12]))
        self.run_round_trip(str(TEST_FILES_SBOL2[12]))

    def test_case13(self):
        print(str(TEST_FILES_SBOL2[13]))
        self.run_round_trip(str(TEST_FILES_SBOL2[13]))

    def test_case14(self):
        print(str(TEST_FILES_SBOL2[14]))
        self.run_round_trip(str(TEST_FILES_SBOL2[14]))

#emptyJSONFile.json
#    def test_case15(self):
#        print(str(TEST_FILES_SBOL2[15]))
#        self.run_round_trip(str(TEST_FILES_SBOL2[15]))

    def test_case16(self):
        print(str(TEST_FILES_SBOL2[16]))
        self.run_round_trip(str(TEST_FILES_SBOL2[16]))

    def test_case17(self):
        print(str(TEST_FILES_SBOL2[17]))
        self.run_round_trip(str(TEST_FILES_SBOL2[17]))

    def test_case18(self):
        print(str(TEST_FILES_SBOL2[18]))
        self.run_round_trip(str(TEST_FILES_SBOL2[18]))

    def test_case19(self):
        print(str(TEST_FILES_SBOL2[19]))
        self.run_round_trip(str(TEST_FILES_SBOL2[19]))

    def test_case20(self):
        print(str(TEST_FILES_SBOL2[20]))
        self.run_round_trip(str(TEST_FILES_SBOL2[20]))

    def test_case21(self):
        print(str(TEST_FILES_SBOL2[21]))
        self.run_round_trip(str(TEST_FILES_SBOL2[21]))

    def test_case22(self):
        print(str(TEST_FILES_SBOL2[22]))
        self.run_round_trip(str(TEST_FILES_SBOL2[22]))

    def test_case23(self):
        print(str(TEST_FILES_SBOL2[23]))
        self.run_round_trip(str(TEST_FILES_SBOL2[23]))

    def test_case24(self):
        print(str(TEST_FILES_SBOL2[24]))
        self.run_round_trip(str(TEST_FILES_SBOL2[24]))

    def test_case25(self):
        print(str(TEST_FILES_SBOL2[25]))
        self.run_round_trip(str(TEST_FILES_SBOL2[25]))

    def test_case26(self):
        print(str(TEST_FILES_SBOL2[26]))
        self.run_round_trip(str(TEST_FILES_SBOL2[26]))

    def test_case27(self):
        print(str(TEST_FILES_SBOL2[27]))
        self.run_round_trip(str(TEST_FILES_SBOL2[27]))

    def test_case28(self):
        print(str(TEST_FILES_SBOL2[28]))
        self.run_round_trip(str(TEST_FILES_SBOL2[28]))

    def test_case29(self):
        print(str(TEST_FILES_SBOL2[29]))
        self.run_round_trip(str(TEST_FILES_SBOL2[29]))

    def test_case30(self):
        print(str(TEST_FILES_SBOL2[30]))
        self.run_round_trip(str(TEST_FILES_SBOL2[30]))

    def test_case31(self):
        print(str(TEST_FILES_SBOL2[31]))
        self.run_round_trip(str(TEST_FILES_SBOL2[31]))

    def test_case32(self):
        print(str(TEST_FILES_SBOL2[32]))
        self.run_round_trip(str(TEST_FILES_SBOL2[32]))

    def test_case33(self):
        print(str(TEST_FILES_SBOL2[33]))
        self.run_round_trip(str(TEST_FILES_SBOL2[33]))

    def test_case34(self):
        print(str(TEST_FILES_SBOL2[34]))
        self.run_round_trip(str(TEST_FILES_SBOL2[34]))

    def test_case35(self):
        print(str(TEST_FILES_SBOL2[35]))
        self.run_round_trip(str(TEST_FILES_SBOL2[35]))

    def test_case36(self):
        print(str(TEST_FILES_SBOL2[36]))
        self.run_round_trip(str(TEST_FILES_SBOL2[36]))

    def test_case37(self):
        print(str(TEST_FILES_SBOL2[37]))
        self.run_round_trip(str(TEST_FILES_SBOL2[37]))

    def test_case38(self):
        print(str(TEST_FILES_SBOL2[38]))
        self.run_round_trip(str(TEST_FILES_SBOL2[38]))

    def test_case39(self):
        print(str(TEST_FILES_SBOL2[39]))
        self.run_round_trip(str(TEST_FILES_SBOL2[39]))

    def test_case40(self):
        print(str(TEST_FILES_SBOL2[40]))
        self.run_round_trip(str(TEST_FILES_SBOL2[40]))

    def test_case41(self):
        print(str(TEST_FILES_SBOL2[41]))
        self.run_round_trip(str(TEST_FILES_SBOL2[41]))

    def test_case42(self):
        print(str(TEST_FILES_SBOL2[42]))
        self.run_round_trip(str(TEST_FILES_SBOL2[42]))

    def test_case43(self):
        print(str(TEST_FILES_SBOL2[43]))
        self.run_round_trip(str(TEST_FILES_SBOL2[43]))

    def test_case44(self):
        print(str(TEST_FILES_SBOL2[44]))
        self.run_round_trip(str(TEST_FILES_SBOL2[44]))

    def test_case45(self):
        print(str(TEST_FILES_SBOL2[45]))
        self.run_round_trip(str(TEST_FILES_SBOL2[45]))

    def test_case46(self):
        print(str(TEST_FILES_SBOL2[46]))
        self.run_round_trip(str(TEST_FILES_SBOL2[46]))

    def test_case47(self):
        print(str(TEST_FILES_SBOL2[47]))
        self.run_round_trip(str(TEST_FILES_SBOL2[47]))

    def test_case48(self):
        print(str(TEST_FILES_SBOL2[48]))
        self.run_round_trip(str(TEST_FILES_SBOL2[48]))

    def test_case49(self):
        print(str(TEST_FILES_SBOL2[49]))
        self.run_round_trip(str(TEST_FILES_SBOL2[49]))

    def test_case50(self):
        print(str(TEST_FILES_SBOL2[50]))
        self.run_round_trip(str(TEST_FILES_SBOL2[50]))

    def test_case51(self):
        print(str(TEST_FILES_SBOL2[51]))
        self.run_round_trip(str(TEST_FILES_SBOL2[51]))

    def test_case52(self):
        print(str(TEST_FILES_SBOL2[52]))
        self.run_round_trip(str(TEST_FILES_SBOL2[52]))

    def test_case53(self):
        print(str(TEST_FILES_SBOL2[53]))
        self.run_round_trip(str(TEST_FILES_SBOL2[53]))

    def test_case54(self):
        print(str(TEST_FILES_SBOL2[54]))
        self.run_round_trip(str(TEST_FILES_SBOL2[54]))

    def test_case55(self):
        print(str(TEST_FILES_SBOL2[55]))
        self.run_round_trip(str(TEST_FILES_SBOL2[55]))

    def test_case56(self):
        print(str(TEST_FILES_SBOL2[56]))
        self.run_round_trip(str(TEST_FILES_SBOL2[56]))

    def test_case57(self):
        print(str(TEST_FILES_SBOL2[57]))
        self.run_round_trip(str(TEST_FILES_SBOL2[57]))

    def test_case58(self):
        print(str(TEST_FILES_SBOL2[58]))
        self.run_round_trip(str(TEST_FILES_SBOL2[58]))

    def test_case59(self):
        print(str(TEST_FILES_SBOL2[59]))
        self.run_round_trip(str(TEST_FILES_SBOL2[59]))

    def test_case60(self):
        print(str(TEST_FILES_SBOL2[60]))
        self.run_round_trip(str(TEST_FILES_SBOL2[60]))

    def test_case61(self):
        print(str(TEST_FILES_SBOL2[61]))
        self.run_round_trip(str(TEST_FILES_SBOL2[61]))

    def test_case62(self):
        print(str(TEST_FILES_SBOL2[62]))
        self.run_round_trip(str(TEST_FILES_SBOL2[62]))

    def test_case63(self):
        print(str(TEST_FILES_SBOL2[63]))
        self.run_round_trip(str(TEST_FILES_SBOL2[63]))

    def test_case64(self):
        print(str(TEST_FILES_SBOL2[64]))
        self.run_round_trip(str(TEST_FILES_SBOL2[64]))

    def test_case65(self):
        print(str(TEST_FILES_SBOL2[65]))
        self.run_round_trip(str(TEST_FILES_SBOL2[65]))

    def test_case66(self):
        print(str(TEST_FILES_SBOL2[66]))
        self.run_round_trip(str(TEST_FILES_SBOL2[66]))

    def test_case67(self):
        print(str(TEST_FILES_SBOL2[67]))
        self.run_round_trip(str(TEST_FILES_SBOL2[67]))

    def test_case68(self):
        print(str(TEST_FILES_SBOL2[68]))
        self.run_round_trip(str(TEST_FILES_SBOL2[68]))

    def test_case69(self):
        print(str(TEST_FILES_SBOL2[69]))
        self.run_round_trip(str(TEST_FILES_SBOL2[69]))

    def test_case70(self):
        print(str(TEST_FILES_SBOL2[70]))
        self.run_round_trip(str(TEST_FILES_SBOL2[70]))

    def test_case71(self):
        print(str(TEST_FILES_SBOL2[71]))
        self.run_round_trip(str(TEST_FILES_SBOL2[71]))

    def test_case72(self):
        print(str(TEST_FILES_SBOL2[72]))
        self.run_round_trip(str(TEST_FILES_SBOL2[72]))

    def test_case73(self):
        print(str(TEST_FILES_SBOL2[73]))
        self.run_round_trip(str(TEST_FILES_SBOL2[73]))

    #SBOL1and2Test
    #def test_case74(self):
    #    print(str(TEST_FILES_SBOL2[74]))
    #    self.run_round_trip(str(TEST_FILES_SBOL2[74]))

    def test_case75(self):
        print(str(TEST_FILES_SBOL2[75]))
        self.run_round_trip(str(TEST_FILES_SBOL2[75]))

    def test_case76(self):
        print(str(TEST_FILES_SBOL2[76]))
        self.run_round_trip(str(TEST_FILES_SBOL2[76]))

    def test_case77(self):
        print(str(TEST_FILES_SBOL2[77]))
        self.run_round_trip(str(TEST_FILES_SBOL2[77]))

    def test_case78(self):
        print(str(TEST_FILES_SBOL2[78]))
        self.run_round_trip(str(TEST_FILES_SBOL2[78]))

    def test_case79(self):
        print(str(TEST_FILES_SBOL2[79]))
        self.run_round_trip(str(TEST_FILES_SBOL2[79]))

    def test_case80(self):
        print(str(TEST_FILES_SBOL2[80]))
        self.run_round_trip(str(TEST_FILES_SBOL2[80]))

    def test_case81(self):
        print(str(TEST_FILES_SBOL2[81]))
        self.run_round_trip(str(TEST_FILES_SBOL2[81]))

    def test_case82(self):
        print(str(TEST_FILES_SBOL2[82]))
        self.run_round_trip(str(TEST_FILES_SBOL2[82]))

    def test_case83(self):
        print(str(TEST_FILES_SBOL2[83]))
        self.run_round_trip(str(TEST_FILES_SBOL2[83]))

    def test_case84(self):
        print(str(TEST_FILES_SBOL2[84]))
        self.run_round_trip(str(TEST_FILES_SBOL2[84]))

    def test_case85(self):
        print(str(TEST_FILES_SBOL2[85]))
        self.run_round_trip(str(TEST_FILES_SBOL2[85]))

    def test_case86(self):
        print(str(TEST_FILES_SBOL2[86]))
        self.run_round_trip(str(TEST_FILES_SBOL2[86]))

    def test_case87(self):
        print(str(TEST_FILES_SBOL2[87]))
        self.run_round_trip(str(TEST_FILES_SBOL2[87]))

    def test_case88(self):
        print(str(TEST_FILES_SBOL2[88]))
        self.run_round_trip(str(TEST_FILES_SBOL2[88]))

    def test_case89(self):
        print(str(TEST_FILES_SBOL2[89]))
        self.run_round_trip(str(TEST_FILES_SBOL2[89]))

    def test_case90(self):
        print(str(TEST_FILES_SBOL2[90]))
        self.run_round_trip(str(TEST_FILES_SBOL2[90]))

    def test_case91(self):
        print(str(TEST_FILES_SBOL2[91]))
        self.run_round_trip(str(TEST_FILES_SBOL2[91]))

    def test_case92(self):
        print(str(TEST_FILES_SBOL2[92]))
        self.run_round_trip(str(TEST_FILES_SBOL2[92]))

    def test_case93(self):
        print(str(TEST_FILES_SBOL2[93]))
        self.run_round_trip(str(TEST_FILES_SBOL2[93]))

    def test_case94(self):
        print(str(TEST_FILES_SBOL2[94]))
        self.run_round_trip(str(TEST_FILES_SBOL2[94]))

    def test_case95(self):
        print(str(TEST_FILES_SBOL2[95]))
        self.run_round_trip(str(TEST_FILES_SBOL2[95]))

    def test_case96(self):
        print(str(TEST_FILES_SBOL2[96]))
        self.run_round_trip(str(TEST_FILES_SBOL2[96]))

    def test_case97(self):
        print(str(TEST_FILES_SBOL2[97]))
        self.run_round_trip(str(TEST_FILES_SBOL2[97]))

    def test_case98(self):
        print(str(TEST_FILES_SBOL2[98]))
        self.run_round_trip(str(TEST_FILES_SBOL2[98]))

    def test_case99(self):
        print(str(TEST_FILES_SBOL2[99]))
        self.run_round_trip(str(TEST_FILES_SBOL2[99]))

class TestComponentDefinitions(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def testAddComponentDefinition(self):
        test_CD = ComponentDefinition("BB0001")
        doc = Document()
        doc.addComponentDefinition(test_CD)
        
        self.assertIsNotNone(doc.getComponentDefinition("BB0001"))
        
        displayId = doc.getComponentDefinition("BB0001").displayId.get()
        
        self.assertEqual(displayId, "BB0001")
        
    def testRemoveComponentDefinition(self):
        test_CD = ComponentDefinition("BB0001")
        doc = Document()
        doc.addComponentDefinition(test_CD)
        doc.componentDefinitions.remove(0)
        self.assertRaises(RuntimeError, lambda: doc.sequences.get("BB0001"))
        
    def testCDDisplayId(self):
        listCD_read = []
        doc = Document()
        doc.read(os.path.join(TEST_LOC_SBOL2, str(TEST_FILES_SBOL2[72])))

        # List of displayIds        
        listCD = ['CRP_b', 'CRa_U6', 'EYFP', 'EYFP_cds', 'EYFP_gene', 'Gal4VP16',
                  'Gal4VP16_cds', 'Gal4VP16_gene', 'cas9_gRNA_complex', 'cas9_generic',
                  'cas9m_BFP', 'cas9m_BFP_cds', 'cas9m_BFP_gRNA_b', 'cas9m_BFP_gene',
                  'gRNA_b', 'gRNA_b_gene', 'gRNA_b_nc', 'gRNA_b_terminator',
                  'gRNA_generic', 'mKate', 'mKate_cds', 'mKate_gene', 'pConst',
                  'target', 'target_gene']
        
        for CD in doc.componentDefinitions:
            listCD_read.append(CD.displayId.get())
            
        self.assertItemsEqual(listCD_read, listCD)
             
    #def testCDSeq(self):
    #    doc = Document()
    #    doc.read(os.path.join(TEST_LOCATION, str(TEST_LOC_SBOL2[72])))
        
    #def testCDpersistentIdentity(self):
    #def testCDrole(self):
    #def testCDtype(self):
    #def testCDcomponent(self):
    #def testCDsequenceConstraint(self):
        
        

        
#    def testComponentDefinitionElement(self):
#        doc = Document()
#        doc.read(os.path.join(TEST_LOCATION, str(TEST_FILES[4])))
#        # Sequence to test against
#        seq = ('GCTCCGAATTTCTCGACAGATCTCATGTGATTACGCCAAGCTACGGGCGGAGTACTGTCCTC'
#               'CGAGCGGAGTACTGTCCTCCGAGCGGAGTACTGTCCTCCGAGCGGAGTACTGTCCTCCGAGC'
#               'GGAGTTCTGTCCTCCGAGCGGAGACTCTAGATACCTCATCAGGAACATGTTGGAATTCTAGG'
#               'CGTGTACGGTGGGAGGCCTATATAAGCAGAGCTCGTTTAGTGAACCGTCAGATCGCCTCGAG'
#               'TACCTCATCAGGAACATGTTGGATCCAATTCGACC')
#               
#        seq_read = doc.getSequence('CRP_b_seq').elements.get()
#        self.assertEquals(seq_read, seq)

#class TestSBOLObject(unittest.TestCase):
#    def assertReadOnly(self, obj, attr):
#        try:
#            obj.__getattribute__(attr)
#            obj.__setattr__(attr, None)
#            raise AssertionError
#        except AttributeError:
#            pass

#def assertReadWrite(self, obj, attr, content=None):
#    if not content:
#        content = random_string()
#        self.assertEqual(obj.__getattribute__(attr), None)
#        obj.__setattr__(attr, content)
#        self.assertEqual(obj.__getattribute__(attr), content)
#        obj.__setattr__(attr, None)
#        self.assertEqual(obj.__getattribute__(attr), None)
#
#    def setUp(self):
#        self.doc = sbol.Document()
#        self.assertEqual(self.doc.num_sbol_objects, 0)
#        self.uris    = []
#        self.testees = []
#        self.createTestees()
#        self.assertEqual(len(self.uris), len(self.testees))
#        self.assertEqual(len(self.uris), self.doc.num_sbol_objects)
#        self.assertEqual(len(self.uris), sbol.libsbol.getNumSBOLObjects(self.doc.ptr))
#
#def tearDown(self):
#    self.assertEqual(len(self.uris), self.doc.num_sbol_objects)
#        self.assertEqual(len(self.uris), sbol.libsbol.getNumSBOLObjects(self.doc.ptr))
#        del self.doc
#    # todo check that everything was deleted?
#    
#    def createTestees(self):
#        for obj in (sbol.DNASequence,
#                    sbol.SequenceAnnotation,
#                    sbol.DNAComponent,
#                    sbol.Collection):
#            uri = random_uri()
#            self.uris.append(uri)
#            self.testees.append(obj(self.doc, uri))
#
#def testURI(self):
#    for n in range( len(self.testees) ):
#        testee = self.testees[n]
#            uri = self.uris[n]
#            self.assertEqual(testee.uri, uri)
#            self.assertReadOnly(testee, 'uri')
#
#class TestSBOLCompoundObject(TestSBOLObject):
#    def createTestees(self):
#        for obj in (sbol.DNAComponent,
#                    sbol.Collection):
#            uri = random_uri()
#            self.uris.append(uri)
#            self.testees.append(obj(self.doc, uri))
#
#def testDisplayID(self):
#    for testee in self.testees:
#        self.assertReadWrite(testee, 'display_id')
#
#    def testName(self):
#        for testee in self.testees:
#            self.assertReadWrite(testee, 'name')
#
#def testDescription(self):
#    for testee in self.testees:
#        self.assertReadWrite(testee, 'description')
#
#class TestDNASequence(TestSBOLObject):
#    def createTestees(self):
#        uri = random_uri()
#        self.uris.append(uri)
#        self.testees.append( sbol.DNASequence(self.doc, uri) )
#    
#    def testNucleotides(self):
#        self.assertReadWrite(self.testees[0], 'nucleotides')
#
#class TestSequenceAnnotation(TestSBOLObject):
#    def assertPositionWorking(self, obj, attr):
#        self.assertEqual(obj.__getattribute__(attr), None)
#        # check that setting valid positions works
#        for n in range(NUM_FAST_TESTS):
#            position = random_valid_position()
#            obj.__setattr__(attr, position)
#            self.assertEqual(obj.__getattribute__(attr), position)
#        # check that setting invalid positions raises error
#        for n in range(NUM_FAST_TESTS):
#            obj.__setattr__(attr, None)
#            position = random_invalid_position()
#            self.assertRaises(sbol.PositionError, obj.__setattr__, attr, position)
#        # check that resetting to None works
#        obj.__setattr__(attr, 1)
#        self.assertEqual(obj.__getattribute__(attr), 1)
#        obj.__setattr__(attr, None)
#        self.assertEqual(obj.__getattribute__(attr), None)
#    
#    def createTestees(self):
#        uri = random_uri()
#        self.uris.append(uri)
#        self.testees.append( sbol.SequenceAnnotation(self.doc, uri) )
#    
#    def testPositions(self):
#        self.assertPositionWorking(self.testees[0], 'start')
#        self.assertPositionWorking(self.testees[0], 'end')
#    
#    def testStrand(self):
#        # check that strand is initially forward
#        self.assertEquals(self.testees[0].strand, '+')
#        # check that it can only be set to valid symbols
#        valid_polarities = ('+', '*', '-')
#        for symbol in random_string():
#            if symbol in valid_polarities:
#                self.testees[0].strand = symbol
#                self.assertEquals(self.testees[0].strand, symbol)
#            else:
#                self.assertRaises(sbol.StrandError,
#                                  self.testees[0].__setattr__,
#                                  'strand',
#                                  symbol)
#
#def testSubcomponent(self):
#    self.assertEquals(self.testees[0].subcomponent, None)
#        uri = random_uri()
#        self.uris.append(uri)
#        com = sbol.DNAComponent(self.doc, uri)
#        self.testees[0].subcomponent = com
#        self.assertEquals(self.testees[0].subcomponent, com)
#    
#    def testPrecedes(self):
#        for n in range(NUM_SLOW_TESTS):
#            self.assertEqual(len(self.testees[0].precedes), n)
#            uri = random_uri()
#            self.uris.append(uri)
#            ann = sbol.SequenceAnnotation(self.doc, uri)
#            self.assertFalse(ann in self.testees[0].precedes)
#            self.testees[0].precedes += ann
#            self.assertTrue(ann in self.testees[0].precedes)
#
class TestSequences(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def testAddSeqence(self):
        test_seq = Sequence("R0010", "ggctgca")
        doc = Document()
        doc.addSequence(test_seq)
        seq = doc.sequences.get("R0010").elements.get()
        
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
        doc.read(os.path.join(TEST_LOC_SBOL2, str(TEST_FILES_SBOL2[72])))

        # List of displayIds        
        listseq = ['CRP_b_seq', 'CRa_U6_seq', 'gRNA_b_seq', 'mKate_seq']
        
        for seq in doc.sequences:
            listseq_read.append(seq.displayId.get())
            
        self.assertItemsEqual(listseq_read, listseq)
            
    def testSequenceElement(self):
        doc = Document()
        doc.read(os.path.join(TEST_LOC_SBOL2, str(TEST_FILES_SBOL2[72])))
        # Sequence to test against
        seq = ('GCTCCGAATTTCTCGACAGATCTCATGTGATTACGCCAAGCTACGGGCGGAGTACTGTCCTC'
               'CGAGCGGAGTACTGTCCTCCGAGCGGAGTACTGTCCTCCGAGCGGAGTACTGTCCTCCGAGC'
               'GGAGTTCTGTCCTCCGAGCGGAGACTCTAGATACCTCATCAGGAACATGTTGGAATTCTAGG'
               'CGTGTACGGTGGGAGGCCTATATAAGCAGAGCTCGTTTAGTGAACCGTCAGATCGCCTCGAG'
               'TACCTCATCAGGAACATGTTGGATCCAATTCGACC')
               
        seq_read = doc.getSequence('CRP_b_seq').elements.get()
        self.assertEquals(seq_read, seq)

#class TestPythonMethods(unittest.TestCase):

    
#    def testAnnotations(self):
#        for n in range(NUM_SLOW_TESTS):
#            self.assertEqual(len(self.testees[0].annotations), n)
#            uri = random_uri()
#            self.uris.append(uri)
#            ann = sbol.SequenceAnnotation(self.doc, uri)
#            self.assertFalse(ann in self.testees[0].annotations)
#            self.testees[0].annotations += ann
#            self.assertTrue(ann in self.testees[0].annotations)
#
#class TestCollection(TestSBOLCompoundObject):
#    def createTestees(self):
#        uri = random_uri()
#        self.uris.append(uri)
#        self.testees.append( sbol.Collection(self.doc, uri) )
#    
#    def testComponents(self):
#        col = self.testees[0]
#        for n in range(NUM_SLOW_TESTS):
#            self.assertEqual(len(col.components), n)
#            uri = random_uri()
#            self.uris.append(uri)
#            com = sbol.DNAComponent(self.doc, uri)
#            self.assertFalse(com in col.components)
#            col.components += com
#            self.assertTrue(com in col.components)
#            self.assertEqual(len(col.components), n+1)

# List of tests
test_list = [TestRoundTripSBOL2, TestComponentDefinitions, TestSequences]

def runTests():
    print("Setting up")
    suite_list = []
    loader = unittest.TestLoader()
    for test_class in test_list:
        suite = loader.loadTestsFromTestCase(test_class)
        suite_list.append(suite)
   
    full_test_suite = unittest.TestSuite(suite_list)
    unittest.TextTestRunner(verbosity=2,stream=sys.stderr).run(full_test_suite)

if __name__ == '__main__':
    unittest.main()

