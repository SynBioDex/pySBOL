package org.ValidationTesting;

import static org.junit.Assert.*;

import java.io.File;
import java.io.IOException;
import java.net.URISyntaxException;
import java.util.HashSet;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.sbolstandard.core2.SBOLConversionException;
import org.sbolstandard.core2.SBOLDocument;
import org.sbolstandard.core2.SBOLReader;
import org.sbolstandard.core2.SBOLValidate;
import org.sbolstandard.core2.SBOLValidationException;

@RunWith(Parameterized.class)
public class SBOL1ValidationTest {
	private File file;

	/**
	 * @param file
	 *            - file to test
	 */
	public SBOL1ValidationTest(File file) {
		this.file = file;
	}

	/**
	 * @return a set of files to test
	 */
	@Parameterized.Parameters
	public static java.util.Collection<File> files() {
		File file_base = null;
		java.util.Collection<File> col = new HashSet<File>();

		try {
			file_base = new File(SBOL2ValidationTest.class.getResource("/SBOL1/").toURI());
		} catch (URISyntaxException e1) {
			e1.printStackTrace();
		}
		for (File f : file_base.listFiles()) {
			if (f.getName().equals("pIKE_pTAK_cassettes.xml")) continue;
			if (f.getName().equals("BBa_T9002.xml")) continue;
			if (f.getName().equals("pIKE_pTAK_left_right_cassettes.xml")) continue;
			if (f.getName().equals("pIKE_pTAK_cassettes_2.xml")) continue;
			if (f.getName().equals("pACPc_invF.xml")) continue;
			if (f.getName().equals(".gitignore")) continue;
			if (f.getName().equals("manifest")) continue;
			col.add(f);
		}

		return col;
	}

	/**
	 * Run each xml/XML file under the "Validation" sub-directory to test SBOL
	 * validation exceptions.
	 * 
	 * @throws IOException
	 *             see {@link IOException}
	 * @throws SBOLConversionException
	 *             see {@link SBOLConversionException}
	 * @throws SBOLValidationException
	 *             see {@link SBOLValidationException}
	 */
	@Test
	public void runValidation()
			throws IOException, SBOLConversionException, SBOLValidationException {
		SBOLReader.setKeepGoing(true);
		SBOLDocument doc = SBOLReader.read(file);
		SBOLValidate.validateSBOL(doc, false, false, false);

		if (SBOLReader.getNumErrors() > 0 || SBOLValidate.getNumErrors() > 0) {
			System.out.println("Testing " + file.getName() + ": ");
			// String fileName = dir + "/" + file.getName();
			// SBOLWriter.write(doc, fileName);
			// String errorFileName = dir + "/" + file.getName().replace(".xml", "") +
			// "_errors.txt";
			// BufferedWriter bw = new BufferedWriter(new FileWriter(new
			// File(errorFileName)));

			for (String error : SBOLReader.getErrors()) {
				System.out.println(error);
				// bw.write(error);
				// bw.write("\n");
			}


			for (String error : SBOLValidate.getErrors()) {
				System.out.println(error);

				// bw.write(error);
				// bw.write("\n");
			}

			// bw.close();
			fail();
		}
	}

}
