import unittest
from .libsbol import *
import random
import string
import os, sys
import tempfile, shutil
import inspect
from urllib3.exceptions import HTTPError


############################################
# Utility functions for generating test data
############################################

URIS_USED = set()
RANDOM_CHARS = string.ascii_letters

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


#################################################
# Commandline parameters for Synbiohub test instance
#################################################

# username = None
# password = None
# resource = None
# spoofed_resource = None
# if 'TestPartShop.RESOURCE' in os.environ:
#     TestPartShop.RESOURCE = os.environ['TestPartShop.RESOURCE']
# else:
#     raise ValueError('Must specify TestPartShop.RESOURCE environment variable with the URL for the repository')
if 'SBH_USER' in os.environ:
    SBH_USER = os.environ['SBH_USER']
else:
    SBH_USER = None
if 'SBH_PASSWORD' in os.environ:
    SBH_PASSWORD = os.environ['SBH_PASSWORD']
else:
    SBH_PASSWORD = None
# else:
#     raise ValueError('Must specify PASS environment variable with the user password')
# if 'SPOOF' in os.environ:
#     SPOOF_TestPartShop.RESOURCE = os.environ['SPOOF']


#####################
# Paths to test files
#####################

MODULE_LOCATION = os.path.dirname(os.path.abspath(__file__))
TEST_LOCATION = os.path.join(MODULE_LOCATION, 'test')
TEST_LOC_SBOL2 = os.path.join(TEST_LOCATION, 'SBOL2')
TEST_LOC_SBOL2_bp = os.path.join(TEST_LOCATION, 'SBOL2_bp')
TEST_LOC_SBOL2_ic = os.path.join(TEST_LOCATION, 'SBOL2_ic')
TEST_LOC_SBOL2_nc = os.path.join(TEST_LOCATION, 'SBOL2_nc')

#TEST_LOC_SBOL1 = os.path.join(TEST_LOCATION, 'SBOL1')
#TEST_LOC_RDF = os.path.join(TEST_LOCATION, 'RDF')
#TEST_LOC_Invalid = os.path.join(TEST_LOCATION, 'InvalidFiles')
#TEST_LOC_GB = os.path.join(TEST_LOCATION, 'GenBank')

##############
# Unit tests
##############

#class TestParse(unittest.TestCase):

#class TestWrite(unittest.TestCase):

class TestRoundTripSBOL2(unittest.TestCase):
    '''
    Test SBOL files that are compliant, complete, and adhere to best practices.
    '''
    def setUp(self):
        # Create temp directory
        self.temp_out_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove directory after the test
        shutil.rmtree(self.temp_out_dir)

class TestRoundTripSBOL2BestPractices(unittest.TestCase):
    '''
    Test SBOL files that are compliant and complete, but do not follow best practices
    '''
    def setUp(self):
        # Create temp directory
        self.temp_out_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove directory after the test
        shutil.rmtree(self.temp_out_dir)

class TestRoundTripSBOL2IncompleteDocuments(unittest.TestCase):
    '''
    Test SBOL files that are incomplete, but are compliant
    '''
    def setUp(self):
        # Create temp directory
        self.temp_out_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove directory after the test
        shutil.rmtree(self.temp_out_dir)


class TestRoundTripSBOL2NoncompliantURIs(unittest.TestCase):
    '''
    Test SBOL files that are not compliant
    '''
    def setUp(self):
        # Create temp directory
        self.temp_out_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove directory after the test
        shutil.rmtree(self.temp_out_dir)


def test_generator(test_file):
    def run_round_trip(self):
        print(str(test_file))
        split_path = os.path.splitext(test_file)
        self.doc = Document()   # Document for read and write
        # self.doc.read(os.path.join(TEST_LOC_SBOL2, split_path[0] + split_path[1]))
        self.doc.read(test_file)
        self.doc.write(os.path.join(self.temp_out_dir, split_path[0] + '_out' + split_path[1]))
        
        self.doc2 = Document()  # Document to compare for equality
        self.doc2.read(os.path.join(self.temp_out_dir, split_path[0] + '_out' + split_path[1]))
        self.assertEqual(self.doc.compare(self.doc2), 1)
    return run_round_trip

# Dynamically generate test cases
i_f = 0
for f in os.listdir(TEST_LOC_SBOL2):
    if f == '.' or f == '..' or f == 'manifest':
        continue
    if f == 'pICH42211.xml' or f == 'pICH42222.xml':
        continue
    f = os.path.join(TEST_LOC_SBOL2, f)
    test_name = 'testRoundTripSBOL2_{:03d}'.format(i_f)
    test = test_generator(f)
    setattr(TestRoundTripSBOL2, test_name, test)
    i_f += 1


i_f = 0
for f in os.listdir(TEST_LOC_SBOL2_bp):
    if f == '.' or f == '..' or f == 'manifest':
        continue
    f = os.path.join(TEST_LOC_SBOL2_bp, f)
    test_name = 'testRoundTripBestPractices_{:03d}'.format(i_f)
    test = test_generator(f)
    setattr(TestRoundTripSBOL2BestPractices, test_name, test)
    i_f += 1

i_f = 0
for f in os.listdir(TEST_LOC_SBOL2_ic):
    if f == '.' or f == '..' or f == 'manifest':
        continue
    f = os.path.join(TEST_LOC_SBOL2_ic, f)
    test_name = 'testRoundTripSBOL2IncompleteDocuments_{:03d}'.format(i_f)
    test = test_generator(f)
    setattr(TestRoundTripSBOL2IncompleteDocuments, test_name, test)
    i_f += 1

i_f = 0
for f in os.listdir(TEST_LOC_SBOL2_nc):
    if f == '.' or f == '..' or f == 'manifest':
        continue
    f = os.path.join(TEST_LOC_SBOL2_nc, f)
    test_name = 'testRoundTripSBOL2NoncompliantURIs_{:03d}'.format(i_f)
    test = test_generator(f)
    setattr(TestRoundTripSBOL2NoncompliantURIs, test_name, test)
    i_f += 1


class TestRoundTripFailSBOL2(unittest.TestCase):
    def setUp(self):
        # Create temp directory
        self.temp_out_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove directory after the test
        shutil.rmtree(self.temp_out_dir)

    def run_round_trip_assert_fail(self, test_file):
        split_path = os.path.splitext(test_file)
        self.doc = Document()   # Document for read and write
        self.doc.read(os.path.join(TEST_LOC_SBOL2, split_path[0] + split_path[1]))
        self.doc.write(os.path.join(self.temp_out_dir, split_path[0] + '_out' + split_path[1]))

        self.doc2 = Document()  # Document to compare for equality
        self.doc2.read(os.path.join(self.temp_out_dir, split_path[0] + '_out' + split_path[1]))
        # Expected to fail
        self.assertRaises(AssertionError, lambda: self.assertEqual(self.doc.compare(self.doc2), 1))

class TestComponentDefinitions(unittest.TestCase):

    def setUp(self):
        pass

    def testAddComponentDefinition(self):
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
        self.assertRaises(RuntimeError, lambda: doc.componentDefinitions.get("BB0001"))

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

        self.assertListEqual(listCD_read, listCD)

    def testPrimaryStructureIteration(self):
        listCD = []
        listCD_true = ["R0010", "B0032", "E0040", "B0012"]
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

        self.assertListEqual(listCD, listCD_true)

class TestAssemblyRoutines(unittest.TestCase):

    def setUp(self):
        pass

    def testAssemble(self):
        doc = Document()
        gene = ComponentDefinition("BB0001")
        promoter = ComponentDefinition("R0010")
        RBS = ComponentDefinition("B0032")
        CDS = ComponentDefinition("E0040")
        terminator = ComponentDefinition("B0012")

        promoter.sequence = Sequence('R0010')
        RBS.sequence = Sequence('B0032')
        CDS.sequence = Sequence('E0040')
        terminator.sequence = Sequence('B0012')

        promoter.sequence.elements = 'a'
        RBS.sequence.elements = 't'
        CDS.sequence.elements = 'c'
        terminator.sequence.elements = 'g'

        promoter.roles = SO_PROMOTER
        RBS.roles = SO_RBS
        CDS.roles = SO_CDS
        terminator.roles = SO_TERMINATOR

        doc.addComponentDefinition([ gene, promoter, RBS, CDS, terminator ])
        gene.assemblePrimaryStructure([ 'R0010', 'B0032', 'E0040', 'B0012' ])
        primary_structure = gene.getPrimaryStructure()
        primary_structure = [c.identity for c in primary_structure]

        self.assertListEqual(primary_structure, [promoter.identity, RBS.identity, CDS.identity, terminator.identity])

    def testCompileSequence(self):
        doc = Document()
        Config.setOption('sbol_typed_uris', True)
        gene = ComponentDefinition("BB0001")
        promoter = ComponentDefinition("R0010")
        CDS = ComponentDefinition("B0032")
        RBS = ComponentDefinition("E0040")
        terminator = ComponentDefinition("B0012")
        scar = ComponentDefinition('scar')

        promoter.sequence = Sequence('R0010')
        RBS.sequence = Sequence('B0032')
        CDS.sequence = Sequence('E0040')
        terminator.sequence = Sequence('B0012')
        scar.sequence = Sequence('scar')

        promoter.sequence.elements = 'aaa'
        RBS.sequence.elements = 'aaa'
        CDS.sequence.elements = 'aaa'
        terminator.sequence.elements = 'aaa'
        scar.sequence.elements = 'ttt'

        doc.addComponentDefinition(gene)
        gene.assemblePrimaryStructure([ promoter, scar, RBS, scar, CDS, scar, terminator ])
        target_seq = gene.compile()

        self.assertEquals(target_seq, 'aaatttaaatttaaatttaaa')
        self.assertEquals(target_seq, gene.sequence.elements)

    def testRecursiveCompile(self):
        doc = Document()
        cd1 = ComponentDefinition('cd1')
        cd2 = ComponentDefinition('cd2')
        cd3 = ComponentDefinition('cd3')
        cd4 = ComponentDefinition('cd4')
        cd5 = ComponentDefinition('cd5')
        cd1.sequence = Sequence('cd1')
        cd2.sequence = Sequence('cd2')
        cd3.sequence = Sequence('cd3')
        cd4.sequence = Sequence('cd4')
        cd5.sequence = Sequence('cd5')
        cd1.sequence.elements = 'tt'
        cd2.sequence.elements = 'gg'
        cd3.sequence.elements = 'n'
        cd4.sequence.elements = 'aa'
        cd5.sequence.elements = 'n'
        doc.addComponentDefinition([cd1, cd2, cd3, cd4, cd5])
        cd3.assemblePrimaryStructure([cd1, cd2])
        cd5.assemblePrimaryStructure([cd4, cd3])
        cd5.compile()
        self.assertEquals(cd3.sequence.elements, 'ttgg')
        self.assertEquals(cd5.sequence.elements, 'aattgg')
        r1 = cd3.sequenceAnnotations['cd1_annotation_0'].locations['cd1_annotation_0_range']
        r2 = cd3.sequenceAnnotations['cd2_annotation_0'].locations['cd2_annotation_0_range']
        r4 = cd5.sequenceAnnotations['cd4_annotation_0'].locations['cd4_annotation_0_range']
        self.assertEquals(r1.start, 3)
        self.assertEquals(r1.end, 4)
        self.assertEquals(r2.start, 5)
        self.assertEquals(r2.end, 6)
        self.assertEquals(r4.start, 1)
        self.assertEquals(r4.end, 2)

    def testStandardAssembly(self):
        doc = Document()
        gene = ComponentDefinition("BB0001")
        promoter = ComponentDefinition("R0010")
        RBS = ComponentDefinition("B0032")
        CDS = ComponentDefinition("E0040")
        terminator = ComponentDefinition("B0012")

        promoter.sequence = Sequence('R0010')
        RBS.sequence = Sequence('B0032')
        CDS.sequence = Sequence('E0040')
        terminator.sequence = Sequence('B0012')

        promoter.sequence.elements = 'a'
        RBS.sequence.elements = 't'
        CDS.sequence.elements = 'c'
        terminator.sequence.elements = 'g'

        promoter.roles = SO_PROMOTER
        RBS.roles = SO_RBS
        CDS.roles = SO_CDS
        terminator.roles = SO_TERMINATOR

        doc.addComponentDefinition(gene)
        gene.assemblePrimaryStructure([ promoter, RBS, CDS, terminator ], IGEM_STANDARD_ASSEMBLY)
        target_seq = gene.compile()

        self.assertEquals(target_seq, 'atactagagttactagctactagagg')

    def testAssembleWithDisplayIds(self):
        Config.setOption('sbol_typed_uris', True)

        doc = Document()
        gene = ComponentDefinition("BB0001")
        promoter = ComponentDefinition("R0010")
        RBS = ComponentDefinition("B0032")
        CDS = ComponentDefinition("E0040")
        terminator = ComponentDefinition("B0012")

        promoter.sequence = Sequence('R0010')
        RBS.sequence = Sequence('B0032')
        CDS.sequence = Sequence('E0040')
        terminator.sequence = Sequence('B0012')

        promoter.sequence.elements = 'a'
        RBS.sequence.elements = 't'
        CDS.sequence.elements = 'c'
        terminator.sequence.elements = 'g'

        promoter.roles = SO_PROMOTER
        RBS.roles = SO_RBS
        CDS.roles = SO_CDS
        terminator.roles = SO_TERMINATOR

        doc.addComponentDefinition([ gene, promoter, RBS, CDS, terminator ])
        gene.assemblePrimaryStructure([ 'R0010', 'B0032', 'E0040', 'B0012' ])
        primary_structure = gene.getPrimaryStructure()
        primary_structure = [c.identity for c in primary_structure]
        self.assertListEqual(primary_structure, [promoter.identity, RBS.identity, CDS.identity, terminator.identity])

        target_seq = gene.compile()
        self.assertEquals(target_seq, 'atcg')

    def testApplyCallbackRecursively(self):
        # Assemble module hierarchy
        doc = Document()
        root = ModuleDefinition('root')
        sub = ModuleDefinition('sub')
        leaf = ModuleDefinition('leaf')
        doc.addModuleDefinition([root, sub, leaf])
        root.assemble([sub])
        sub.assemble([leaf])

        # Define callback which performs an operation on the given ModuleDefinition
        def callback(md, params):
            level = params[0]
            level += 1
            params[0] = level

        # Apply callback
        level = 0
        params = [ level ]
        flattened_module_tree = root.applyToModuleHierarchy(callback, params)
        level = params[0]
        flattened_module_tree = [md.identity for md in flattened_module_tree]
        expected_module_tree = [md.identity for md in [root, sub, leaf]]
        self.assertSequenceEqual(flattened_module_tree, expected_module_tree)
        self.assertEquals(level, 3)

    def testDeleteUpstream(self):
        doc = Document()
        gene = ComponentDefinition("BB0001")
        promoter = ComponentDefinition("R0010")
        rbs = ComponentDefinition("B0032")
        cds = ComponentDefinition("E0040")
        terminator = ComponentDefinition("B0012")

        doc.addComponentDefinition([ gene, promoter, rbs, cds, terminator ])
        gene.assemblePrimaryStructure([promoter, rbs, cds, terminator])
        primary_structure_components = gene.getPrimaryStructureComponents()
        c_promoter = primary_structure_components[0]
        c_rbs = primary_structure_components[1]
        c_cds = primary_structure_components[2]
        c_terminator = primary_structure_components[3]

        gene.deleteUpstreamComponent(c_cds)
        primary_structure = gene.getPrimaryStructure()
        primary_structure = [cd.identity for cd in primary_structure]
        valid_primary_structure = [promoter.identity, cds.identity, terminator.identity]
        self.assertListEqual(primary_structure, valid_primary_structure)

        # Test deletion when the target Component is the first Component
        gene.deleteUpstreamComponent(c_cds)
        primary_structure = gene.getPrimaryStructure()
        primary_structure = [cd.identity for cd in primary_structure]
        valid_primary_structure = [cds.identity, terminator.identity]
        self.assertListEqual(primary_structure, valid_primary_structure)

        # Test failure when user tries to delete a Component upstream of the first Component
        with self.assertRaises(ValueError):
            gene.deleteUpstreamComponent(c_promoter)
        # Test failure when the user supplies a Component that isn't part of the primary structure
        with self.assertRaises(ValueError):
            gene.deleteUpstreamComponent(Component())

    def testDeleteDownstream(self):
        doc = Document()
        gene = ComponentDefinition("BB0001")
        promoter = ComponentDefinition("R0010")
        rbs = ComponentDefinition("B0032")
        cds = ComponentDefinition("E0040")
        terminator = ComponentDefinition("B0012")

        doc.addComponentDefinition([ gene, promoter, rbs, cds, terminator ])
        gene.assemblePrimaryStructure([promoter, rbs, cds, terminator])
        primary_structure_components = gene.getPrimaryStructureComponents()
        c_promoter = primary_structure_components[0]
        c_rbs = primary_structure_components[1]
        c_cds = primary_structure_components[2]
        c_terminator = primary_structure_components[3]

        gene.deleteDownstreamComponent(c_rbs)
        primary_structure = gene.getPrimaryStructure()
        primary_structure = [cd.identity for cd in primary_structure]
        valid_primary_structure = [promoter.identity, rbs.identity, terminator.identity]
        self.assertListEqual(primary_structure, valid_primary_structure)

        # Test deletion when the target Component is the last Component
        gene.deleteDownstreamComponent(c_rbs)
        primary_structure = gene.getPrimaryStructure()
        primary_structure = [cd.identity for cd in primary_structure]
        valid_primary_structure = [promoter.identity, rbs.identity]
        self.assertListEqual(primary_structure, valid_primary_structure)

        # Test failure when user tries to delete Component upstream of the first Component
        with self.assertRaises(ValueError):
            gene.deleteDownstreamComponent(c_cds)
        # Test failure when the user supplies a Component that isn't part of the primary structure
        with self.assertRaises(ValueError):
            gene.deleteDownstreamComponent(Component())

    def testInsertDownstream(self):
        doc = Document()
        gene = ComponentDefinition("BB0001")
        promoter = ComponentDefinition("R0010")
        rbs = ComponentDefinition("B0032")
        cds = ComponentDefinition("E0040")
        terminator = ComponentDefinition("B0012")

        doc.addComponentDefinition([ gene, promoter, rbs, cds, terminator])
        gene.assemblePrimaryStructure([promoter, rbs, cds])
        primary_structure_components = gene.getPrimaryStructureComponents()
        c_promoter = primary_structure_components[0]
        c_rbs = primary_structure_components[1]
        c_cds = primary_structure_components[2]
        gene.insertDownstreamComponent(c_cds, terminator)
        primary_structure = gene.getPrimaryStructure()
        primary_structure = [cd.identity for cd in primary_structure]
        valid_primary_structure = [promoter.identity, rbs.identity, cds.identity, terminator.identity]
        self.assertListEqual(primary_structure, valid_primary_structure)


    def testInsertUpstream(self):
        doc = Document()
        gene = ComponentDefinition("BB0001")
        promoter = ComponentDefinition("R0010")
        rbs = ComponentDefinition("B0032")
        cds = ComponentDefinition("E0040")
        terminator = ComponentDefinition("B0012")

        doc.addComponentDefinition([ gene, promoter, rbs, cds, terminator])
        gene.assemblePrimaryStructure([rbs, cds, terminator])
        primary_structure_components = gene.getPrimaryStructureComponents()
        c_rbs = primary_structure_components[0]
        c_cds = primary_structure_components[1]
        c_terminator = primary_structure_components[2]
        gene.insertUpstreamComponent(c_rbs, promoter)
        primary_structure = gene.getPrimaryStructure()
        primary_structure = [cd.identity for cd in primary_structure]
        valid_primary_structure = [promoter.identity, rbs.identity, cds.identity, terminator.identity]
        self.assertListEqual(primary_structure, valid_primary_structure)

class TestSequences(unittest.TestCase):

    def setUp(self):
        pass

    def testAddSeqence(self):
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

        self.assertListEqual(listseq_read, listseq)

    def testSequenceElement(self):
        setHomespace('http://sbols.org/CRISPR_Example')
        Config.setOption('sbol_typed_uris', False)
        doc = Document()
        doc.read(os.path.join(MODULE_LOCATION, 'crispr_example.xml'))
        # Sequence to test against
        seq = ('GCTCCGAATTTCTCGACAGATCTCATGTGATTACGCCAAGCTACGGGCGGAGTACTGTCCTC'
               'CGAGCGGAGTACTGTCCTCCGAGCGGAGTACTGTCCTCCGAGCGGAGTACTGTCCTCCGAGC'
               'GGAGTTCTGTCCTCCGAGCGGAGACTCTAGATACCTCATCAGGAACATGTTGGAATTCTAGG'
               'CGTGTACGGTGGGAGGCCTATATAAGCAGAGCTCGTTTAGTGAACCGTCAGATCGCCTCGAG'
               'TACCTCATCAGGAACATGTTGGATCCAATTCGACC')

        seq_read = doc.sequences.get('CRP_b_seq').elements
        self.assertEquals(seq_read, seq)

class TestMemory(unittest.TestCase):

    def setUp(self):
        pass

    def testDiscard(self):
        doc = Document()
        cd = ComponentDefinition()
        bool1 = cd.thisown
        doc.addComponentDefinition(cd)
        bool2 = cd.thisown
        self.assertNotEquals(bool1, bool2)

class TestExtensionClass(unittest.TestCase):

    def testExtensionClass(self):
        class ModuleDefinitionExtension(ModuleDefinition):
            def __init__(self, id = 'example'):
                ModuleDefinition.__init__(self, id)
                self.x_coordinate = TextProperty(self.this, 'http://dnaplotlib.org#xCoordinate', '0', '1', '10')  # Initialize property value to 10
                self.y_coordinate = IntProperty(self.this, 'http://dnaplotlib.org#yCoordinate', '0', '1', 10)  # Initialize property value to 10

        doc = Document()
        doc.addNamespace('http://dnaplotlib.org#', 'dnaplotlib')
        md = ModuleDefinitionExtension('md_example')
        md_id = md.identity
        md.y_coordinate = 5
        self.assertEquals(md.x_coordinate, '10')
        self.assertEquals(md.y_coordinate, 5)
        doc.addExtensionObject(md)
        doc.readString(doc.writeString())
        md = doc.getExtensionObject(md_id)
        self.assertEquals(md.x_coordinate, '10')
        self.assertEquals(md.y_coordinate, 5)

class TestIterators(unittest.TestCase):

    def setUp(self):
        pass

    def testDocumentIterator(self):
        doc = Document()
        cds = []
        for i_cd in range(0, 10):
            cd = doc.componentDefinitions.create('cd%d' %i_cd)
            cds.append(cd.identity)
            self.assertEquals(cd.displayId, 'cd%d' %i_cd)  # Verify TopLevel properties are accessible
        i_cd = 0
        for obj in doc:
            cds.remove(obj.identity)
        self.assertEquals([], cds)

    def testOwnedObjectIterator(self):
        cd = ComponentDefinition()
        sa1 = cd.sequenceAnnotations.create('sa1').this
        sa2 = cd.sequenceAnnotations.create('sa2').this
        annotations = []
        for sa in cd.sequenceAnnotations:
            annotations.append(sa.this)
        self.assertEquals(annotations, [sa1, sa2])

class TestCast(unittest.TestCase):

    def testDowncast(self):
        obj = SBOLObject()
        cd = obj.cast(ComponentDefinition)
        self.assertEquals(cd.type, 'http://sbols.org/v2#ComponentDefinition')

    def testUpcast(self):
        cd = ComponentDefinition()
        obj = cd.cast(SBOLObject)
        self.assertEquals(obj.type, 'http://sbols.org/v2#Undefined')

class TestCopy(unittest.TestCase):

    def setUp(self):
        pass

    def testCloneObject(self):
        cd = ComponentDefinition()
        cd_copy = cd.copy()
        self.assertEquals(cd.compare(cd_copy), 1)

    def testCopyAndIncrementVersion(self):
        Config.setOption('sbol_typed_uris', False)
        doc = Document()
        comp = ComponentDefinition('foo', BIOPAX_DNA, '1.0.0')
        doc.addComponentDefinition(comp)

        # Copy an object within a single Document, the version should be automatically incrememented
        comp_copy = comp.copy()
        self.assertEquals(comp.version, '1.0.0')
        self.assertEquals(comp_copy.version, '2.0.0')
        self.assertEquals(comp_copy.identity, comp.persistentIdentity + '/2.0.0')
        self.assertEquals(comp_copy.wasDerivedFrom[0], comp.identity)
        self.assertEquals(comp_copy.types[0], BIOPAX_DNA)

    def testCopyToNewDocument(self):
        Config.setOption('sbol_typed_uris', False)
        doc = Document()
        comp1 = doc.componentDefinitions.create('cd1')
        comp2 = doc.componentDefinitions.create('cd2')
        comp2.wasDerivedFrom = comp1.identity

        # Clone the object to another Document, the wasDerivedFrom should not be a circular reference
        doc2 = Document()
        comp3 = comp2.copy(doc2)
        self.assertEquals(comp3.identity, comp2.identity)
        self.assertEquals(comp3.wasDerivedFrom[0], comp1.identity)
        self.assertNotEqual(comp3.wasDerivedFrom[0], comp2.identity)

    def testImportObjectIntoNewNamespace(self):
        Config.setOption('sbol_typed_uris', False)
        doc = Document()
        doc2 = Document()
        comp = doc.componentDefinitions.create('hi')
        comp.version = '3'

        # Import the object into a new namespace and retain the same version
        homespace = getHomespace()
        setHomespace('https://hub.sd2e.org/user/sd2e/test')
        comp_copy = comp.copy(doc2, homespace)  # Import from old homespace into new homespace
        self.assertEquals(comp_copy.identity, 'https://hub.sd2e.org/user/sd2e/test/hi/3')

        # Import the object into a new namespace and set the version
        comp_copy = comp.copy(doc2, homespace, '2')  # Import from old homespace into new homespace
        self.assertEquals(comp_copy.identity, 'https://hub.sd2e.org/user/sd2e/test/hi/2')
        setHomespace('http://examples.org')

    def testExtensionObjects(self):
        class GenericTopLevel(TopLevel):
            def __init__(self, id = 'example'):
                TopLevel.__init__(self, 'http://extension_namespace.com#GenericTopLevel', id, '1.0.0')

        tl1 = GenericTopLevel()
        doc = Document()
        doc.addExtensionObject(tl1)
        tl2 = doc.getExtensionObject(tl1.identity)
        self.assertEquals(tl1.this, tl2.this)

    def testCopyExtensionObjects(self):
        class GenericTopLevel(TopLevel):
            def __init__(self, id = 'example'):
                TopLevel.__init__(self, 'http://extension_namespace.com#GenericTopLevel', id, '1.0.0')

        tl = GenericTopLevel()
        doc = Document()
        doc.addExtensionObject(tl)
        doc2 = doc.copy(getHomespace())
        tl = doc2.getExtensionObject(tl.identity)
        self.assertEquals(tl.thisown, False)

    def testUpdateComponentProperty(self):
        # See issue #89
        Config.setOption('sbol_compliant_uris', True)
        Config.setOption('sbol_typed_uris', False)
        setHomespace('http://examples.org')

        doc = Document()

        lacZ = ComponentDefinition('lacZ_cassette', BIOPAX_DNA, '1')
        doc.addComponentDefinition(lacZ)

        pLac = ComponentDefinition('pLac', BIOPAX_DNA, '1')
        doc.addComponentDefinition(pLac)

        pLac_comp = lacZ.components.create('pLac_comp')
        pLac_comp.definition = pLac.identity

        pLac_anno = lacZ.sequenceAnnotations.create('pLac_anno')
        l = pLac_anno.locations.createGenericLocation('pLac_loc')
        pLac_anno.component = pLac_comp.identity
        self.assertEquals(pLac_anno.identity, 'http://examples.org/lacZ_cassette/pLac_anno/1')
        self.assertEquals(pLac_comp.identity, 'http://examples.org/lacZ_cassette/pLac_comp/1')
        self.assertEquals(pLac_anno.component, 'http://examples.org/lacZ_cassette/pLac_comp/1')
        self.assertEquals(l.identity, 'http://examples.org/lacZ_cassette/pLac_anno/pLac_loc/1')

        setHomespace('http://testing.org')

        lacZ_copy = lacZ.copy(doc, 'http://examples.org')
        self.assertEquals(lacZ_copy.identity, 'http://testing.org/lacZ_cassette/' + VERSION_STRING)
        self.assertEquals(lacZ_copy.sequenceAnnotations[0].identity, 'http://testing.org/lacZ_cassette/pLac_anno/' + VERSION_STRING)
        self.assertEquals(lacZ_copy.components[0].identity, 'http://testing.org/lacZ_cassette/pLac_comp/' + VERSION_STRING)
        self.assertEquals(lacZ_copy.sequenceAnnotations[0].component, 'http://testing.org/lacZ_cassette/pLac_comp/' + VERSION_STRING)
        self.assertEquals(lacZ_copy.sequenceAnnotations[0].locations[0].identity, 'http://testing.org/lacZ_cassette/pLac_anno/pLac_loc/' + VERSION_STRING)
        
        setHomespace('http://examples.org')
        Config.setOption('sbol_compliant_uris', True)
        Config.setOption('sbol_typed_uris', True)

    def testUpdateComponentPropertyTypedURI(self):
        # See issue #89
        Config.setOption('sbol_compliant_uris', True)
        Config.setOption('sbol_typed_uris', True)
        setHomespace('http://examples.org')
        doc = Document()

        lacZ = ComponentDefinition('lacZ_cassette', BIOPAX_DNA, '1')
        doc.addComponentDefinition(lacZ)

        pLac = ComponentDefinition('pLac', BIOPAX_DNA, '1')
        doc.addComponentDefinition(pLac)

        pLac_comp = lacZ.components.create('pLac_comp')
        pLac_comp.definition = pLac.identity

        pLac_anno = lacZ.sequenceAnnotations.create('pLac_anno')
        l = pLac_anno.locations.createGenericLocation('pLac_loc')
        pLac_anno.component = pLac_comp.identity
        self.assertEquals(pLac_anno.identity, 'http://examples.org/ComponentDefinition/lacZ_cassette/pLac_anno/1')
        self.assertEquals(pLac_comp.identity, 'http://examples.org/ComponentDefinition/lacZ_cassette/pLac_comp/1')
        self.assertEquals(pLac_anno.component, 'http://examples.org/ComponentDefinition/lacZ_cassette/pLac_comp/1')
        self.assertEquals(l.identity, 'http://examples.org/ComponentDefinition/lacZ_cassette/pLac_anno/pLac_loc/1')

        setHomespace('http://testing.org')
        lacZ_copy = lacZ.copy(doc, 'http://examples.org')
        self.assertEquals(lacZ_copy.identity, 'http://testing.org/ComponentDefinition/lacZ_cassette/' + VERSION_STRING)
        self.assertEquals(lacZ_copy.sequenceAnnotations[0].identity, 'http://testing.org/ComponentDefinition/lacZ_cassette/pLac_anno/' + VERSION_STRING)
        self.assertEquals(lacZ_copy.components[0].identity, 'http://testing.org/ComponentDefinition/lacZ_cassette/pLac_comp/' + VERSION_STRING)
        self.assertEquals(lacZ_copy.sequenceAnnotations[0].component, 'http://testing.org/ComponentDefinition/lacZ_cassette/pLac_comp/' + VERSION_STRING)
        self.assertEquals(lacZ_copy.sequenceAnnotations[0].locations[0].identity, 'http://testing.org/ComponentDefinition/lacZ_cassette/pLac_anno/pLac_loc/' + VERSION_STRING)
        setHomespace('http://examples.org')

    def testCopyIntoNewConfig(self):
        '''
        Copy a typed compliant URI to a non-typed compliant URI
        Copy a non-typed compliant URI to a typed URI
        '''
        pass

class TestDBTL(unittest.TestCase):

    def setUp(self):
        pass

    def testDBTL(self):
        setHomespace("http://examples.org")

        doc = Document()
        workflow_step_1 = Activity('build_1')
        workflow_step_2 = Activity('build_2')
        workflow_step_3 = Activity('build_3')
        workflow_step_4 = Activity('build_4')
        workflow_step_5 = Activity('build_5')
        workflow_step_6 = Activity('test_1')
        workflow_step_7 = Activity('analysis_1')

        workflow_step_1.plan = Plan('PCR_protocol_part1')
        workflow_step_2.plan = Plan('PCR_protocol_part2')
        workflow_step_3.plan = Plan('PCR_protocol_part3')
        workflow_step_4.plan = Plan('gibson_assembly')
        workflow_step_5.plan = Plan('transformation')
        workflow_step_6.plan = Plan('promoter_characterization')
        workflow_step_7.plan = Plan('parameter_optimization')

        setHomespace('')
        Config.setOption('sbol_compliant_uris', False)  # Temporarily disable auto-construction of URIs

        workflow_step_1.agent = Agent('mailto:jdoe@sbols.org')
        workflow_step_2.agent = workflow_step_1.agent
        workflow_step_3.agent = workflow_step_1.agent
        workflow_step_4.agent = workflow_step_1.agent
        workflow_step_5.agent = workflow_step_1.agent
        workflow_step_6.agent = Agent('http://sys-bio.org/plate_reader_1')
        workflow_step_7.agent = Agent('http://tellurium.analogmachine.org')

        Config.setOption('sbol_compliant_uris', True)
        setHomespace("http://examples.org")

        doc.addActivity([workflow_step_1, workflow_step_2, workflow_step_3, workflow_step_4, workflow_step_5, workflow_step_6, workflow_step_7])

        doc.componentDefinitions.create('cd')
        target = Design('target')
        part1 = workflow_step_1.generateBuild('part1', target)
        part2 = workflow_step_2.generateBuild('part2', target)
        part3 = workflow_step_3.generateBuild('part3', target)
        gibson_mix = workflow_step_4.generateBuild('gibson_mix', target, [part1, part2, part3])
        clones = workflow_step_5.generateBuild(['clone1', 'clone2', 'clone3'], target, gibson_mix)
        experiment1 = workflow_step_6.generateTest('experiment1', clones)
        analysis1 = workflow_step_7.generateAnalysis('analysis1', experiment1)
        doc.readString(doc.writeString())

        activity = doc.activities['build_1']
        self.assertEquals(activity.agent.identity, activity.associations[0].agent)
        self.assertEquals(activity.plan.identity, activity.associations[0].plan)

class TestURIAutoConstruction(unittest.TestCase):
    def setUp(self):
        pass

    def testCompliantURIWithVersion(self):
        Config.setOption('sbol_compliant_uris', True)
        Config.setOption('sbol_typed_uris', True)
        tl = TopLevel(SBOL_TOP_LEVEL, 'test', '1b')
        self.assertEquals(tl.identity, getHomespace() + '/TopLevel/test/1b')
        identified = Identified(SBOL_IDENTIFIED, 'test', '1b')
        self.assertEquals(identified.identity, getHomespace() + '/Identified/test/1b')
        
        Config.setOption('sbol_typed_uris', False)
        tl = TopLevel(SBOL_TOP_LEVEL, 'test', '1b')
        self.assertEquals(tl.identity, getHomespace() + '/test/1b')
        identified = Identified(SBOL_IDENTIFIED, 'test', '1b')
        self.assertEquals(identified.identity, getHomespace() + '/test/1b')

    def testCompliantURINoVersion(self):
        Config.setOption('sbol_compliant_uris', True)
        Config.setOption('sbol_typed_uris', True)
        tl = TopLevel(SBOL_TOP_LEVEL, 'test', '')
        self.assertEquals(tl.identity, getHomespace() + '/TopLevel/test')
        identified = Identified(SBOL_IDENTIFIED, 'test', '')
        self.assertEquals(identified.identity, getHomespace() + '/Identified/test')
        
        Config.setOption('sbol_typed_uris', False)
        tl = TopLevel(SBOL_TOP_LEVEL, 'test', '')
        self.assertEquals(tl.identity, getHomespace() + '/test')
        identified = Identified(SBOL_IDENTIFIED, 'test', '')
        self.assertEquals(identified.identity, getHomespace() + '/test')

    def testCreateMethods(self):
        # If the parent Document does not have a version specified, child objects should
        # be initialized with default version string
        Config.setOption('sbol_compliant_uris', True)
        Config.setOption('sbol_typed_uris', True)
        doc = Document()
        self.assertEquals(doc.version, VERSION_STRING)

        doc.version = ''
        cd0 = doc.componentDefinitions.create('cd0')
        self.assertEquals(cd0.version, VERSION_STRING)
        self.assertEquals(cd0.identity, getHomespace() + '/ComponentDefinition/cd0/' + VERSION_STRING)

        sa0 = cd0.sequenceAnnotations.create('ann0')
        self.assertEquals(sa0.version, VERSION_STRING)
        self.assertEquals(sa0.identity, getHomespace() + '/ComponentDefinition/cd0/ann0/' + VERSION_STRING)
        
        # If the parent Document does have a version specified, child objects should
        # inherit that version
        doc = Document()
        doc.version = '2'
        cd0 = doc.componentDefinitions.create('cd0')
        self.assertEquals(cd0.version, '2')
        self.assertEquals(cd0.identity, getHomespace() + '/ComponentDefinition/cd0/2')

        sa0 = cd0.sequenceAnnotations.create('ann0')
        self.assertEquals(sa0.version, '2')
        self.assertEquals(sa0.identity, getHomespace() + '/ComponentDefinition/cd0/ann0/2')

    def testAddChildObjects(self):
        Config.setOption('sbol_compliant_uris', True)
        Config.setOption('sbol_typed_uris', True)
        cd = ComponentDefinition('cd')
        sa = SequenceAnnotation('sa')
        self.assertEquals(sa.identity, getHomespace() + '/SequenceAnnotation/sa/' + VERSION_STRING)
        cd.sequenceAnnotations.add(sa)
        self.assertEquals(sa.identity, getHomespace() + '/ComponentDefinition/cd/sa/' + VERSION_STRING)

    def tearDown(self):
        Config.setOption('sbol_compliant_uris', True)
        Config.setOption('sbol_typed_uris', True)

class TestIntegrate(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        setHomespace('https://example.com') 

    def setUp(self):
        self.doc = Document()
        self.wt_cd = ComponentDefinition('wt_cd')
        self.wt_cd.sequence = Sequence('wt_seq')
        self.insert_cd = ComponentDefinition('insert_cd')
        self.insert_cd.sequence = Sequence('insert_seq')
        self.integrated_cd = ComponentDefinition('integrated_cd')
        self.doc.addComponentDefinition([self.integrated_cd, self.insert_cd, self.wt_cd])

    def testSourceLocation(self):
        # Test insertion splits the targt ComponentDefinition
        # into 2 Components each with a SourceLocation
        self.wt_cd.sequence.elements = 'atcg'
        self.insert_cd.sequence.elements = 'gg'
        self.integrated_cd.integrateAtBaseCoordinate(self.wt_cd, self.insert_cd, 3)
        components = [c for c in self.integrated_cd.components if c.definition == self.wt_cd.identity]
        self.assertEqual(len(components), 2)
        self.assertEqual(len(components[0].sourceLocations), 1)
        self.assertEqual(len(components[1].sourceLocations), 1)
        l0 = components[0].sourceLocations.getRange()
        l1 = components[1].sourceLocations.getRange()
        self.assertEqual(l0.start, 1)
        self.assertEqual(l0.end, 2)
        self.assertEqual(l1.start, 3)
        self.assertEqual(l1.end, 4)

    def testIntegrationPrimaryStructure(self):
        self.wt_cd.sequence.elements = 'atcg'
        self.insert_cd.sequence.elements = 'gg'
        self.integrated_cd.integrateAtBaseCoordinate(self.wt_cd, self.insert_cd, 3)
        primary_structure = self.integrated_cd.getPrimaryStructure()
        primary_structure = [c.identity for c in primary_structure]
        self.assertListEqual(primary_structure, [self.wt_cd.identity, self.insert_cd.identity, self.wt_cd.identity])        

    def testIntegrationNegative(self):
        # An exception should be raised if user tries to insert
        # at a negative base coordinate 
        with self.assertRaises(ValueError):
            self.wt_cd.sequence.elements = 'atcg'
            self.insert_cd.sequence.elements = 'gg'
            self.integrated_cd.integrateAtBaseCoordinate(self.wt_cd, self.insert_cd, -3)

    def testIntegrationPositive(self):
        # An exception should be raised if the user attempts to
        # appending at a location beyond the end of the initial
        # sequence.
        with self.assertRaises(ValueError):
            self.wt_cd.sequence.elements = 'atcg'
            self.insert_cd.sequence.elements = 'gg'
            self.integrated_cd.integrateAtBaseCoordinate(self.wt_cd, self.insert_cd, 8)

    def testIntegration0(self):
        # An exception should be raised if user tries to insert
        # at 0 base coordinate. Base coordinates are indexed from 1
        with self.assertRaises(ValueError):
            self.wt_cd.sequence.elements = 'atcg'
            self.insert_cd.sequence.elements = 'gg'
            self.integrated_cd.integrateAtBaseCoordinate(self.wt_cd, self.insert_cd, 0)

    def testIntegration1(self):
        # Test inserting at the beginning of the sequence. Prepending.
        self.wt_cd.sequence.elements = 'atcg'
        self.insert_cd.sequence.elements = 'gg'
        self.integrated_cd.integrateAtBaseCoordinate(self.wt_cd, self.insert_cd, 1)
        self.integrated_cd.compile()
        self.assertEqual(self.integrated_cd.sequence.elements, 'ggatcg')

    def testIntegration2(self):
        # Test inserting within the sequence.
        self.wt_cd.sequence.elements = 'atcg'
        self.insert_cd.sequence.elements = 'gg'
        self.integrated_cd.integrateAtBaseCoordinate(self.wt_cd, self.insert_cd, 2)
        self.integrated_cd.compile()
        self.assertEqual(self.integrated_cd.sequence.elements, 'aggtcg')

    def testIntegration3(self):
        # Test inserting within the sequence.
        self.wt_cd.sequence.elements = 'atcg'
        self.insert_cd.sequence.elements = 'gg'
        self.integrated_cd.integrateAtBaseCoordinate(self.wt_cd, self.insert_cd, 3)
        self.integrated_cd.compile()
        self.assertEqual(self.integrated_cd.sequence.elements, 'atggcg')

    def testIntegration4(self):
        # Test inserting one base before the end of the sequence.
        self.wt_cd.sequence.elements = 'atcg'
        self.insert_cd.sequence.elements = 'gg'
        self.integrated_cd.integrateAtBaseCoordinate(self.wt_cd, self.insert_cd, 4)
        self.integrated_cd.compile()
        self.assertEqual(self.integrated_cd.sequence.elements, 'atcggg')

    def testIntegrationN(self):
        # Test appending at the end of the initial sequence.
        self.wt_cd.sequence.elements = 'atcg'
        self.insert_cd.sequence.elements = 'gg'
        self.integrated_cd.integrateAtBaseCoordinate(self.wt_cd, self.insert_cd, 5)
        self.integrated_cd.compile()
        self.assertEqual(self.integrated_cd.sequence.elements, 'atcggg')

    def testMissingDocument(self):
        # Test that compile fails with a raised exception when
        # this CD or the insert is not associated with a Document
        self.wt_cd.sequence.elements = 'atcg'
        self.insert_cd.sequence.elements = 'gg'
        self.wt_cd = self.doc.componentDefinitions.remove(self.wt_cd.identity)
        with self.assertRaises(ValueError):
            self.integrated_cd.integrateAtBaseCoordinate(self.wt_cd, self.insert_cd, 4)
        self.doc.componentDefinitions.add(self.wt_cd)
        self.insert_cd = self.doc.componentDefinitions.remove(self.insert_cd.identity)
        with self.assertRaises(ValueError):
            self.integrated_cd.integrateAtBaseCoordinate(self.wt_cd, self.insert_cd, 4)

    def testDifferentDocuments(self):
        # Currently this causes a double-deletion error when the routine exits
        pass
        # Test that compile fails with a raised exception when
        # this CD and the insert belong to different Documents

        # new_doc = Document()
        # self.insert_cd.sequence.elements = 'gg'
        # self.wt_cd.sequence.elements = 'atcg'
        # self.wt_cd = self.doc.componentDefinitions.remove(self.wt_cd.identity)
        # new_doc.componentDefinitions.add(self.wt_cd)
        # with self.assertRaises(ValueError):
        #     self.integrated_cd.integrateAtBaseCoordinate(self.wt_cd, self.insert_cd, 4)


# class TestIntegrate(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls):
#         setHomespace('https://example.com')      

#     def makeIntegration(self, dst_seq, insert_seq, insert_loc):
#         doc = Document()
#         cd0 = ComponentDefinition('wt_cd')
#         cd0.sequence = Sequence('wt_seq', dst_seq)
#         doc.addComponentDefinition(cd0)

#         insert_cd = ComponentDefinition('insert_cd')
#         insert_cd.sequence = Sequence('insert_seq', insert_seq)
#         doc.addComponentDefinition(insert_cd)

#         cd = cd0.integrate(insert_cd, insert_loc, 'new_cd')

#         # Return the doc and URI because we get a Segmentation Fault
#         # if we return the cd itself and then try to reference it in
#         # any way.
#         return doc, cd.identity

#     def testSourceLocation(self):
#         # Test insertion splits the targt ComponentDefinition
#         # into 2 Components each with a SourceLocation
#         doc = Document()
#         cd0 = ComponentDefinition('wt_cd')
#         cd0.sequence = Sequence('wt_seq', 'atcg')
#         doc.addComponentDefinition(cd0)

#         insert_cd = ComponentDefinition('insert_cd')
#         insert_cd.sequence = Sequence('insert_seq', 'gg')
#         doc.addComponentDefinition(insert_cd)

#         cd = cd0.integrate(insert_cd, 3, 'new_cd')
#         components = [c for c in cd.components if c.definition == cd0.identity]
#         self.assertEqual(len(components), 2)
#         self.assertEqual(len(components[0].sourceLocations), 1)
#         self.assertEqual(len(components[1].sourceLocations), 1)
#         l0 = components[0].sourceLocations.getRange()
#         l1 = components[1].sourceLocations.getRange()
#         self.assertEqual(l0.start, 1)
#         self.assertEqual(l0.end, 2)
#         self.assertEqual(l1.start, 3)
#         self.assertEqual(l1.end, 4)

#     def testIntegrationPrimaryStructure(self):
#         doc = Document()
#         cd0 = ComponentDefinition('wt_cd')
#         cd0.sequence = Sequence('wt_seq', 'atcg')
#         doc.addComponentDefinition(cd0)

#         insert_cd = ComponentDefinition('insert_cd')
#         insert_cd.sequence = Sequence('insert_seq', 'gg')
#         doc.addComponentDefinition(insert_cd)

#         cd = cd0.integrate(insert_cd, 3, 'new_cd')
#         primary_structure = cd.getPrimaryStructure()
#         primary_structure = [c.identity for c in primary_structure]
 
#         self.assertListEqual(primary_structure, [cd0.identity, insert_cd.identity, cd0.identity])        

#     def testIntegrationNegative(self):
#         # An exception should be raised if user tries to insert
#         # at a negative base coordinate 
#         with self.assertRaises(ValueError):
#             doc, uri = self.makeIntegration('atcg', 'gg', -3)

#     def testIntegration0(self):
#         # An exception should be raised if user tries to insert
#         # at 0 base coordinate. Base coordinates are indexed from 1
#         with self.assertRaises(ValueError):
#             doc, uri = self.makeIntegration('atcg', 'gg', 0)

#     def testIntegration1(self):
#         # Test inserting at the beginning of the sequence. Prepending.
#         doc, uri = self.makeIntegration('atcg', 'gg', 1)
#         cd = doc.getComponentDefinition(uri)
#         cd.compile()
#         self.assertEqual(cd.sequence.elements, 'ggatcg')

#     def testIntegration2(self):
#         # Test inserting within the sequence.
#         doc, uri = self.makeIntegration('atcg', 'gg', 2)
#         cd = doc.getComponentDefinition(uri)
#         cd.compile()
#         self.assertEqual(cd.sequence.elements, 'aggtcg')

#     def testIntegration3(self):
#         # Test inserting within the sequence.
#         doc, uri = self.makeIntegration('atcg', 'aa', 3)
#         cd = doc.getComponentDefinition(uri)
#         cd.compile()
#         self.assertEqual(cd.sequence.elements, 'ataacg')

#     def testIntegration4(self):
#         # Test inserting one base before the end of the sequence.
#         doc, uri = self.makeIntegration('atcg', 'aa', 4)
#         cd = doc.getComponentDefinition(uri)
#         cd.compile()
#         self.assertEqual(cd.sequence.elements, 'atcaag')

#     def testIntegrationN(self):
#         # Test appending at the end of the initial sequence.
#         doc, uri = self.makeIntegration('atcg', 'gg', 5)
#         cd = doc.getComponentDefinition(uri)
#         cd.compile()
#         self.assertEqual(cd.sequence.elements, 'atcggg')

#     def testIntegrationPositive(self):
#         # An exception should be raised if the user attempts to
#         # appending at a location beyond the end of the initial
#         # sequence.
#         with self.assertRaises(ValueError):
#             doc, uri = self.makeIntegration('atcg', 'gg', 8)

#     def testMissingDocument(self):
#         # Test that compile fails with a raised exception when
#         # this CD or the insert is not associated with a Document
#         doc = Document()
#         cd = ComponentDefinition('cd')
#         insert_cd = doc.componentDefinitions.create('insert_cd')
#         with self.assertRaises(ValueError):
#             cd = cd.integrate(insert_cd, 4, 'new_cd')
#         doc = Document()
#         cd = doc.componentDefinitions.create('cd')
#         insert_cd = ComponentDefinition('insert_cd')
#         with self.assertRaises(ValueError):
#             cd = cd.integrate(insert_cd, 4, 'new_cd')

#     def testDifferentDocuments(self):
#         # Test that compile fails with a raised exception when
#         # this CD and the insert belong to different Documents
#         doc0 = Document()
#         doc1 = Document()
#         cd = doc0.componentDefinitions.create('cd')
#         insert_cd = doc1.componentDefinitions.create('insert_cd')
#         with self.assertRaises(ValueError):
#             cd = cd.integrate(insert_cd, 4, 'new_cd')

#     def testCDwithoutSequence(self):
#         # Test that compile fails with a raised exception when
#         # the CD doesn't have a Sequence
#         doc = Document()
#         cd = doc.componentDefinitions.create('cd')
#         insert_cd = doc.componentDefinitions.create('insert_cd')
#         with self.assertRaises(ValueError):
#             cd = cd.integrate(insert_cd, 4, 'new_cd')

#     def testCDwithoutSequenceElements(self):
#         # Test that compile fails with a raised exception when
#         # the Sequence doesn't have valid elements
#         doc = Document()
#         cd = doc.componentDefinitions.create('cd')
#         cd.sequence = Sequence('cd_seq')
#         insert_cd = doc.componentDefinitions.create('insert_cd')
#         with self.assertRaises(ValueError):
#             cd = cd.integrate(insert_cd, 4, 'new_cd')

#     def testIntegrationwithoutSequence(self):
#         # Test that compile fails with a raised exception when
#         # the insert CD doesn't have a Sequence
#         doc = Document()
#         cd = doc.componentDefinitions.create('cd')
#         cd.sequence = Sequence('cd_seq', 'tttttt')
#         insert_cd = doc.componentDefinitions.create('insert_cd')
#         with self.assertRaises(ValueError):
#             cd = cd.integrate(insert_cd, 4, 'new_cd')

#     def testIntegrationwithoutSequenceElements(self):
#         # Test that compile fails with a raised exception when
#         # the insert Sequence doesn't have valid elements
#         doc = Document()
#         cd = doc.componentDefinitions.create('cd')
#         cd.sequence = Sequence('cd_seq', 'tttttt')
#         insert_cd = doc.componentDefinitions.create('insert_cd')
#         insert_cd.sequence = Sequence('insert_seq')
#         with self.assertRaises(ValueError):
#             cd = cd.integrate(insert_cd, 4, 'new_cd')


#     def testDoubleInsertion(self):
#         # 
#         doc, uri = self.makeIntegration('atcg', 'aa', 3)
#         cd = doc.getComponentDefinition(uri)
#         cd.compile()
#         insert_cd = ComponentDefinition('insert2_cd')
#         insert_cd.sequence = Sequence('insert2_seq', 'gcta')
#         doc.addComponentDefinition(insert_cd)
#         cd = cd.integrate(insert_cd, 4, 'new_new_cd')
#         cd.compile()
#         self.assertEqual(cd.sequence.elements, 'atagctaacg')
#         ranges = []
#         for sa in cd.sequenceAnnotations:
#             r = sa.locations.getRange()
#             ranges.append((r.start, r.end))
#         ranges.sort()
#         self.assertEqual(len(ranges), 3)
#         self.assertEqual(ranges[0], (1, 3))
#         self.assertEqual(ranges[1], (4, 7))
#         self.assertEqual(ranges[2], (8, 10))

class TestCombinatorial(unittest.TestCase):

    def testCombinatorial(self):
        doc = Document()

        # Create template
        pathway_template = doc.componentDefinitions.create('pathway_template')
        pathway_genes = []
        for i_gene in range(3):
            gene = pathway_template.components.create('gene_%d' %i_gene)
            gene.definition = ComponentDefinition('gene_%d' %i_gene)
            pathway_genes.append(gene)

        vioA = doc.componentDefinitions.create('vioA')
        vioB = doc.componentDefinitions.create('vioB')
        vioC = doc.componentDefinitions.create('vioC')

        # Create combinatorial design
        combinatorial_pathway = doc.combinatorialDerivations.create('combinatorial_pathway')
        combinatorial_pathway.masterTemplate = pathway_template
        for i_gene in range(3):
            variable_component = combinatorial_pathway.variableComponents.create('variable_component_%d' %i_gene)
            variable_component.variable = pathway_genes[i_gene]
            variable_component.variants = [vioA, vioB, vioC]
            variable_component.variantCollections = Collection('c')
            variable_component.repeat = 'http://sbols.org/v2#one'

class TestPartShop(unittest.TestCase):

    # These parameters for the Synbiohub test instance are set externally by the test runner
    USER = None
    PASSWORD = None
    RESOURCE = None
    SPOOFED_RESOURCE = None

    @classmethod
    def setUpClass(cls):
        TestPartShop.PART_SHOP = PartShop(TestPartShop.RESOURCE)
        TestPartShop.TEST_COLLECTION_URI = TestPartShop.RESOURCE
        if TestPartShop.SPOOFED_RESOURCE:
            TestPartShop.PART_SHOP.spoof(TestPartShop.SPOOFED_RESOURCE)
            TestPartShop.TEST_COLLECTION_URI = TestPartShop.SPOOFED_RESOURCE
        TestPartShop.TEST_COLLECTION = 'pySBOL_test'
        TestPartShop.TEST_COLLECTION_URI += '/user/' + TestPartShop.USER + '/' + TestPartShop.TEST_COLLECTION + '/' + TestPartShop.TEST_COLLECTION + '_collection/1'
        Config.setOption('sbol_typed_uris', False)

    def testLoginFailure(self):
        with self.assertRaises(Exception):
            TestPartShop.PART_SHOP.login('foo', 'bar')

    def testLogin(self):
        response = TestPartShop.PART_SHOP.login(TestPartShop.USER, TestPartShop.PASSWORD)
        self.assertEqual(response, None)  # None is returned if the login succeeded

    def testSubmit(self):
        '''
        '0' prevent, '1' overwrite, '2' merge and prevent, '3' merge and overwrite
        '''
        doc = Document()
        doc.displayId = TestPartShop.TEST_COLLECTION
        doc.name = 'pySBOL test'
        doc.description = 'A temporary collection used for running pySBOL integration tests'
        doc.componentDefinitions.create('foo')
        TestPartShop.PART_SHOP.submit(doc)
        self.assertTrue(TestPartShop.PART_SHOP.exists(TestPartShop.TEST_COLLECTION_URI))
        self.assertTrue(TestPartShop.PART_SHOP.exists(TestPartShop.RESOURCE + '/user/' + TestPartShop.USER + \
            '/' + TestPartShop.TEST_COLLECTION + '/foo/1'))

    def testPull(self):
        doc = Document()
        TestPartShop.PART_SHOP.pull(TestPartShop.TEST_COLLECTION_URI, doc)
        self.assertTrue(len(doc.componentDefinitions) == 1)

    def testSubmitPrevent(self):
        doc = Document()
        doc.displayId = TestPartShop.TEST_COLLECTION
        doc.name = 'pySBOL test'
        doc.description = 'A temporary collection used for running pySBOL integration tests'
        doc.componentDefinitions.create('foo')
        with self.assertRaises(HTTPError):
            TestPartShop.PART_SHOP.submit(doc, TestPartShop.TEST_COLLECTION_URI, 0)

    def testSubmitOverwrite(self):
        doc = Document()
        doc.displayId = TestPartShop.TEST_COLLECTION
        doc.name = 'pySBOL test'
        doc.description = 'A temporary collection used for running pySBOL integration tests'
        bar = doc.componentDefinitions.create('bar')
        bar.roles = SO_PROMOTER
        TestPartShop.PART_SHOP.submit(doc, TestPartShop.TEST_COLLECTION_URI, 1)
        
        # Check that foo object created in test_submit has been deleted and replaced with bar
        self.assertFalse(TestPartShop.PART_SHOP.exists(TestPartShop.RESOURCE + '/user/' + TestPartShop.USER + \
            '/' + TestPartShop.TEST_COLLECTION + '/foo/1'))
        self.assertTrue(TestPartShop.PART_SHOP.exists(TestPartShop.RESOURCE + '/user/' + TestPartShop.USER + \
            '/' + TestPartShop.TEST_COLLECTION + '/bar/1'))

    def testSubmitMergeAndPrevent(self):
        doc = Document()
        doc.displayId = TestPartShop.TEST_COLLECTION
        doc.name = 'pySBOL test'
        doc.description = 'A temporary collection used for running pySBOL integration tests'
        bar = doc.componentDefinitions.create('bar')

        # Change bar's roles field from what it was set to in test_submit_overwrite
        bar.roles = SO_CDS
        with self.assertRaises(HTTPError):
            TestPartShop.PART_SHOP.submit(doc, TestPartShop.TEST_COLLECTION_URI, 2)
        
    def testSubmitMergeAndOverwrite(self):
        doc = Document()
        doc.displayId = TestPartShop.TEST_COLLECTION
        doc.name = 'pySBOL test'
        doc.description = 'A temporary collection used for running pySBOL integration tests'
        bar = doc.componentDefinitions.create('bar')

        # Change bar's roles field from what it was set to in test_submit_overwrite
        bar.roles = SO_CDS
        TestPartShop.PART_SHOP.submit(doc, TestPartShop.TEST_COLLECTION_URI, 3)            

    def testPreventDuplicateCollections(self):
        # Synbiohub is janky when trying to merge a Collection that already exists
        # on Synbiohub and also exists in the submission Document. This can result
        # in a duplicate Collection.
        DUPLICATE_COLLECTION_URI = TestPartShop.RESOURCE + '/user/' + TestPartShop.USER + '/' + \
                                   TestPartShop.TEST_COLLECTION + '/user_' + TestPartShop.USER + '_' + \
                                   TestPartShop.TEST_COLLECTION + '_' + TestPartShop.TEST_COLLECTION + '_collection/1'

        doc = Document()
        TestPartShop.PART_SHOP.pull(TestPartShop.TEST_COLLECTION_URI, doc)
        for c in doc.collections:
            print(c)
        print(TestPartShop.TEST_COLLECTION_URI)
        self.assertTrue(TestPartShop.TEST_COLLECTION_URI in doc.collections)
        TestPartShop.PART_SHOP.submit(doc, TestPartShop.TEST_COLLECTION_URI, 3)    
        self.assertTrue(TestPartShop.TEST_COLLECTION_URI in doc.collections)
        self.assertFalse(TestPartShop.PART_SHOP.exists(DUPLICATE_COLLECTION_URI))

    def testPullAndMerge(self):
        # Synbiohub is janky when trying to merge Documents that are already
        # populated with objects in the PartShop's namespace. Therefore,
        # a succesful merge operation requires this workaround
        DUPLICATE_COLLECTION_URI = TestPartShop.RESOURCE + '/user/' + TestPartShop.USER + '/' + \
                                   TestPartShop.TEST_COLLECTION + '/user_' + TestPartShop.USER + '_' + \
                                   TestPartShop.TEST_COLLECTION + '_' + TestPartShop.TEST_COLLECTION + '_collection/1'

        doc = Document()
        TestPartShop.PART_SHOP.pull(TestPartShop.TEST_COLLECTION_URI, doc)
        doc = doc.copy(TestPartShop.RESOURCE + '/user/' + TestPartShop.USER)
        for obj in doc:
            obj.wasDerivedFrom = None
        foo = doc.componentDefinitions.create('foo')
        TestPartShop.PART_SHOP.submit(doc, TestPartShop.TEST_COLLECTION_URI, 3)    

        # Check that foo object created in test_submit has been deleted and replaced with bar
        self.assertTrue(TestPartShop.PART_SHOP.exists(TestPartShop.RESOURCE + '/user/' + TestPartShop.USER + \
            '/' + TestPartShop.TEST_COLLECTION + '/foo/1'))
        self.assertTrue(TestPartShop.PART_SHOP.exists(TestPartShop.RESOURCE + '/user/' + TestPartShop.USER + \
            '/' + TestPartShop.TEST_COLLECTION + '/bar/1'))
        self.assertFalse(TestPartShop.PART_SHOP.exists(DUPLICATE_COLLECTION_URI))

    def testRemove(self):
        TestPartShop.PART_SHOP.remove(TestPartShop.TEST_COLLECTION_URI)
        self.assertFalse(TestPartShop.PART_SHOP.exists(TestPartShop.TEST_COLLECTION_URI))

##############
# Test runners
##############

def runTests(test_list = [TestComponentDefinitions, TestSequences, TestMemory, TestIterators, TestCast, TestCopy, TestDBTL, TestAssemblyRoutines, TestExtensionClass, TestURIAutoConstruction, TestIntegrate, TestCombinatorial], username = SBH_USER, password = SBH_PASSWORD, resource = None, spoofed_resource = None):
    
    # Test methods will be executed in the order in which they are declared in this file
    # (Necessary for testing HTTP interface with Synbiohub which relies on database state)

    def get_decl_line_no(method_name, method_map):
        '''
        Get line number on which a method is declared
        '''
        try:
            method = method_map[method_name]
        except:
            print(__name__)
            print(method_map.keys())
        return inspect.getsourcelines(method)[1]

    def compare_method_line_nos(m, n, method_map):
        '''
        Callback used to sort methods by order they appear in this file
        '''
        if get_decl_line_no(m, method_map) < get_decl_line_no(n, method_map):
            return -1
        else:
            return 1

    # Map callable methods from each Test class to their respective method name
    method_map = {}
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj) and obj.__module__ == __name__:
            for fx_name, fx in inspect.getmembers(obj, inspect.isroutine):
                if fx.__name__ in obj.__dict__:
                    method_map[fx_name] = fx

    if username and password and resource:
        test_list.append(TestPartShop)
        TestPartShop.USER = username
        TestPartShop.PASSWORD = password
        TestPartShop.RESOURCE = resource
        if spoofed_resource:
            TestPartShop.SPOOFED_RESOURCE = spoofed_resource
    elif username or password or resource:
        raise ValueError('Cannot run PartShop tests. A username, password, and resource must be specified as keyword arguments.')

    VALIDATE = Config.getOption('validate')
    Config.setOption('validate', False)

    test_suite = []
    loader = unittest.TestLoader()
    loader.sortTestMethodsUsing = lambda m, n: compare_method_line_nos(m, n, method_map)  # Sort test methods based on declaration line in this file 

    for test_class in test_list:
        test_suite.append(loader.loadTestsFromTestCase(test_class))
    testResult = unittest.TextTestRunner(verbosity=2,stream=sys.stderr).run(unittest.TestSuite(test_suite))
    # restore the validate config option
    Config.setOption('validate', VALIDATE)
    return testResult.wasSuccessful()


def runRoundTripTests(test_list = [TestRoundTripSBOL2, TestRoundTripSBOL2BestPractices, TestRoundTripSBOL2IncompleteDocuments, TestRoundTripSBOL2NoncompliantURIs
, TestRoundTripFailSBOL2]):
    VALIDATE = Config.getOption('validate')
    Config.setOption('validate', False)

    test_suite = []
    loader = unittest.TestLoader()
    for test_class in test_list:
        test_suite.append(loader.loadTestsFromTestCase(test_class))
    testResult = unittest.TextTestRunner(verbosity=2,stream=sys.stderr).run(unittest.TestSuite(test_suite))
    # restore the validate config option
    Config.setOption('validate', VALIDATE)
    return testResult.wasSuccessful()


def travisRunTests(**kwargs):
    """This is a convenience function to execute runTests in
    TravisCI. This function accepts any keyword args and passes them
    along to `runTests()`. Then this function causes the interpreter
    to exit with a status of 0 if tests were successful and 1
    otherwise.

    """
    sys.exit(not runTests(**kwargs))


def travisRunRoundTripTests(**kwargs):
    """This is a convenience function to execute runRoundTripTests in
    TravisCI. This function accepts any keyword args and passes them
    along to `runRoundTripTests()`. Then this function causes the interpreter
    to exit with a status of 0 if tests were successful and 1
    otherwise.

    """
    sys.exit(not runRoundTripTests(**kwargs))


if __name__ == '__main__':
    runTests()
