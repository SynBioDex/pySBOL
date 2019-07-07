import unittest
from .libsbol import *
import random
import string
import os, sys
import tempfile, shutil

#####################
# utility functions
#####################

URIS_USED = set()
RANDOM_CHARS = string.ascii_letters
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

TEST_FILES_SBOL2 = []



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

        self.assertSequenceEqual(listCD_read, listCD)
        # # Python 3 compatability
        # if sys.version_info[0] < 3:
        #   self.assertItemsEqual(listCD_read, listCD)
        # else:
        #   self.assertCountEqual(listCD_read, listCD)

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

class TestAssemblyRoutines(unittest.TestCase):

    def setUp(self):
        pass

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
        gene.assemblePrimaryStructure([ 'R0010', 'B0032', 'E0040', 'B0012' ], IGEM_STANDARD_ASSEMBLY)
        target_seq = gene.compile()

        self.assertEquals(target_seq, 'atactagagttactagctactagagg')

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

        # Python 3 compatability
        if sys.version_info[0] < 3:
            self.assertItemsEqual(listseq_read, listseq)
        else:
            self.assertCountEqual(listseq_read, listseq)

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

def runTests(test_list = [TestComponentDefinitions, TestSequences, TestMemory, TestIterators, TestCopy, TestDBTL, TestAssemblyRoutines, TestExtensionClass, TestURIAutoConstruction ]):
    VALIDATE = Config.getOption('validate')
    Config.setOption('validate', False)

    #exec(open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "CRISPR_example.py")).read())
    suite_list = []
    loader = unittest.TestLoader()
    for test_class in test_list:
        suite = loader.loadTestsFromTestCase(test_class)
        suite_list.append(suite)

    full_test_suite = unittest.TestSuite(suite_list)
    unittest.TextTestRunner(verbosity=2,stream=sys.stderr).run(full_test_suite)
    Config.setOption('validate', VALIDATE)

def runRoundTripTests(test_list = [TestRoundTripSBOL2, TestRoundTripSBOL2BestPractices, TestRoundTripSBOL2IncompleteDocuments, TestRoundTripSBOL2NoncompliantURIs
, TestRoundTripFailSBOL2]):
    runTests(test_list)

if __name__ == '__main__':
    runTests()
