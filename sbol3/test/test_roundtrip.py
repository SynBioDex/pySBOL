import unittest
import tempfile, shutil
import sys
from document import *

MODULE_LOCATION = os.path.dirname(os.path.abspath(__file__))
TEST_LOC_SBOL2 = os.path.join(MODULE_LOCATION, 'SBOLTestSuite', 'SBOL2')
FILES_SBOL2 = os.listdir(TEST_LOC_SBOL2)
FILES_SBOL2.sort()
TEST_FILES_SBOL2 = []
for i in FILES_SBOL2:
    if i.endswith('rdf'):
        TEST_FILES_SBOL2.append(i)
    if i.endswith('xml'):
        TEST_FILES_SBOL2.append(i)


class TestRoundTripSBOL2(unittest.TestCase):
    def setUp(self):
        # Create temp directory
        self.temp_out_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove directory after the test
        shutil.rmtree(self.temp_out_dir)

    def run_round_trip(self, test_file):
        print(str(test_file))
        split_path = os.path.splitext(test_file)
        self.doc = Document()   # Document for read and write
        self.doc.read(os.path.join(TEST_LOC_SBOL2, split_path[0] + split_path[1]))
        self.doc.write(os.path.join(self.temp_out_dir, split_path[0] + '_out' + split_path[1]))

        self.doc2 = Document()  # Document to compare for equality
        self.doc2.read(os.path.join(self.temp_out_dir, split_path[0] + '_out' + split_path[1]))
        self.assertTrue(self.doc.compare(self.doc2))

    def test_case000(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[0]))

    def test_case001(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[1]))

    def test_case002(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[2]))

    def test_case003(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[3]))

    def test_case004(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[4]))

    def test_case005(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[5]))

    def test_case006(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[6]))

    def test_case007(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[7]))

    def test_case008(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[8]))

    def test_case009(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[9]))

    def test_case010(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[10]))

    def test_case011(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[11]))

    def test_case012(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[12]))

    def test_case013(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[13]))

    def test_case014(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[14]))

    def test_case015(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[15]))

    def test_case016(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[16]))

    def test_case017(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[17]))

    def test_case018(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[18]))

    def test_case019(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[19]))

    def test_case020(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[20]))

    def test_case021(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[21]))

    def test_case022(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[22]))

    def test_case023(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[23]))

    def test_case024(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[24]))

    def test_case025(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[25]))

    def test_case026(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[26]))

    def test_case027(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[27]))

    def test_case028(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[28]))

    def test_case029(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[29]))

    def test_case030(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[30]))

    def test_case031(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[31]))

    def test_case032(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[32]))

    def test_case033(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[33]))

    def test_case034(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[34]))

    def test_case035(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[35]))

    def test_case036(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[36]))

    def test_case037(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[37]))

    def test_case038(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[38]))

    def test_case039(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[39]))

    def test_case040(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[40]))

    def test_case041(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[41]))

    def test_case042(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[42]))

    def test_case043(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[43]))

    def test_case044(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[44]))

    def test_case045(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[45]))

    def test_case046(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[46]))

    def test_case047(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[47]))

    def test_case048(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[48]))

    def test_case049(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[49]))

    def test_case050(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[50]))

    def test_case051(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[51]))

    def test_case052(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[52]))

    def test_case053(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[53]))

    def test_case054(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[54]))

    def test_case055(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[55]))

    def test_case056(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[56]))

    def test_case057(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[57]))

    def test_case058(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[58]))

    def test_case059(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[59]))

    def test_case060(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[60]))

    def test_case061(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[61]))

    def test_case062(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[62]))

    def test_case063(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[63]))

    def test_case064(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[64]))

    def test_case065(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[65]))

    def test_case066(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[66]))

    def test_case067(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[67]))

    def test_case068(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[68]))

    def test_case069(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[69]))

    def test_case070(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[70]))

    def test_case071(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[71]))

    def test_case072(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[72]))

    def test_case073(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[73]))

    def test_case074(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[74]))

    def test_case075(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[75]))

    def test_case076(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[76]))

    def test_case077(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[77]))

    def test_case078(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[78]))

    def test_case079(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[79]))

    def test_case080(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[80]))

    def test_case081(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[81]))

    def test_case082(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[82]))

    def test_case083(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[83]))

    def test_case084(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[84]))

    def test_case085(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[85]))

    def test_case086(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[86]))

    def test_case087(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[87]))

    def test_case088(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[88]))

    def test_case089(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[89]))

    def test_case090(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[90]))

    def test_case091(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[91]))

    def test_case092(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[92]))

    def test_case093(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[93]))

    def test_case094(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[94]))

    def test_case095(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[95]))

    def test_case096(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[96]))

    def test_case097(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[97]))

    def test_case098(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[98]))

    def test_case099(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[99]))

    def test_case100(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[100]))

    def test_case101(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[101]))

    def test_case102(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[102]))

    def test_case103(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[103]))

    def test_case104(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[104]))

    def test_case105(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[105]))

    def test_case106(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[106]))

    def test_case107(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[107]))

    def test_case108(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[108]))

    def test_case109(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[109]))

    def test_case110(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[110]))

    def test_case111(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[111]))

    def test_case112(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[112]))

    def test_case113(self):
        self.run_round_trip(str(TEST_FILES_SBOL2[113]))


class TestRoundTripFailSBOL2(unittest.TestCase):
    def setUp(self):
        # Create temp directory
        self.temp_out_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove directory after the test
        shutil.rmtree(self.temp_out_dir)

    def run_round_trip_assert_fail(self, test_file):
        print(str(test_file))
        split_path = os.path.splitext(test_file)
        self.doc = Document()   # Document for read and write
        self.doc.read(os.path.join(TEST_LOC_SBOL2, split_path[0] + split_path[1]))
        self.doc.write(os.path.join(self.temp_out_dir, split_path[0] + '_out' + split_path[1]))

        self.doc2 = Document()  # Document to compare for equality
        self.doc2.read(os.path.join(self.temp_out_dir, split_path[0] + '_out' + split_path[1]))
        # Expected to fail
        self.assertRaises(AssertionError, lambda: self.assertEqual(self.doc.compare(self.doc2), 1))


class SimpleTest(unittest.TestCase):
    def test_read(self):
        test_file = str(TEST_FILES_SBOL2[0])
        print(str(test_file))
        split_path = os.path.splitext(test_file)
        self.doc = Document()   # Document for read and write
        self.doc.read(os.path.join(TEST_LOC_SBOL2, split_path[0] + split_path[1]))


def runTests(test_list):
    #exec(open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "CRISPR_example.py")).read())
    if test_list is None or test_list == []:
        return
    suite_list = []
    loader = unittest.TestLoader()
    for test_class in test_list:
        suite = loader.loadTestsFromTestCase(test_class)
        suite_list.append(suite)

    full_test_suite = unittest.TestSuite(suite_list)

    unittest.TextTestRunner(verbosity=2,stream=sys.stderr).run(full_test_suite)


def runRoundTripTests():
    runTests([TestRoundTripSBOL2, TestRoundTripFailSBOL2])


if __name__ == '__main__':
    runRoundTripTests()
