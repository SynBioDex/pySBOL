package org.ValidationTesting;

import java.io.File;
import java.io.IOException;
import java.net.URISyntaxException;
import java.util.HashSet;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.experimental.runners.Enclosed;

import org.sbolstandard.core2.SBOLConversionException;
import org.sbolstandard.core2.SBOLDocument;
import org.sbolstandard.core2.SBOLReader;
import org.sbolstandard.core2.SBOLValidate;
import org.sbolstandard.core2.SBOLValidationException;

import static org.junit.Assert.*;

/**
 * Checks a set of SBOL files in which each should fail a particular validation
 * rule.
 * 
 * @author Meher Samineni
 * @author Chris Myers
 *
 */
@RunWith(Enclosed.class)
public class SBOL2ValidationTest {

	@RunWith(Parameterized.class)
	public static class SBOL2 {
		private File file;

		/**
		 * @param file
		 *            - file to test
		 */
		public SBOL2(File file) {
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
				file_base = new File(SBOL2ValidationTest.class.getResource("/SBOL2/").toURI());
			} catch (URISyntaxException e1) {
				e1.printStackTrace();
			}
			for (File f : file_base.listFiles()) {
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
			SBOLValidate.validateSBOL(doc, true, true, true);

			if (SBOLReader.getNumErrors() > 0 || SBOLValidate.getNumErrors() > 0) {
				System.out.println("Test Fail for SBOL2 : " + file.getName());
				// String fileName = dir + "/" + file.getName();
				// SBOLWriter.write(doc, fileName);
				// String errorFileName = dir + "/" + file.getName().replace(".xml", "") +
				// "_errors.txt";
				// BufferedWriter bw = new BufferedWriter(new FileWriter(new
				// File(errorFileName)));

				//for (String error : SBOLReader.getErrors()) {
					//System.out.println(error);
					// bw.write(error);
					// bw.write("\n");
				//}


				//for (String error : SBOLValidate.getErrors()) {
					//System.out.println(error);

					// bw.write(error);
					// bw.write("\n");
				//}

				// bw.close();
				fail();
			}
			
			
		}

	}

	@RunWith(Parameterized.class)
	public static class SBOL2IC {
		private File file;

		/**
		 * @param file
		 *            - file to test
		 */
		public SBOL2IC(File file) {
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
				file_base = new File(SBOL2ValidationTest.class.getResource("/SBOL2_ic/").toURI());
			} catch (URISyntaxException e1) {
				e1.printStackTrace();
			}

			for (File f : file_base.listFiles()) {
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
			SBOLValidate.validateSBOL(doc, false, true, false);

			if (SBOLReader.getNumErrors() > 0 || SBOLValidate.getNumErrors() > 0) {
				System.out.println("Test Fail for SBOL2_ic " + file.getName());
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

	@RunWith(Parameterized.class)
	public static class SBOL2NC {
		private File file;

		/**
		 * @param file
		 *            - file to test
		 */
		public SBOL2NC(File file) {
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
				file_base = new File(SBOL2ValidationTest.class.getResource("/SBOL2_nc/").toURI());
			} catch (URISyntaxException e1) {
				e1.printStackTrace();
			}
			for (File f : file_base.listFiles()) {
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
				System.out.println("Test Fail for SBOL2_nc " + file.getName());
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

	@RunWith(Parameterized.class)
	public static class SBOL2BP {
		private File file;

		/**
		 * @param file
		 *            - file to test
		 */
		public SBOL2BP(File file) {
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
				file_base = new File(SBOL2ValidationTest.class.getResource("/SBOL2_bp/").toURI());
			} catch (URISyntaxException e1) {
				e1.printStackTrace();
			}
			for (File f : file_base.listFiles()) {
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
			SBOLValidate.validateSBOL(doc, true, true, false);

			if (SBOLReader.getNumErrors() > 0 || SBOLValidate.getNumErrors() > 0) {
				System.out.println("Test Fail for SBOL2_bp " + file.getName());
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

}
