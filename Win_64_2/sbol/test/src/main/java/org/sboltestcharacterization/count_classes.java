package org.sboltestcharacterization;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.net.URISyntaxException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Random;
import java.util.Set;

import org.sbolstandard.core2.Activity;
import org.sbolstandard.core2.Association;
import org.sbolstandard.core2.CombinatorialDerivation;
import org.sbolstandard.core2.Component;
import org.sbolstandard.core2.ComponentDefinition;
import org.sbolstandard.core2.Cut;
import org.sbolstandard.core2.FunctionalComponent;
import org.sbolstandard.core2.GenericLocation;
import org.sbolstandard.core2.Interaction;
import org.sbolstandard.core2.Location;
import org.sbolstandard.core2.Module;
import org.sbolstandard.core2.ModuleDefinition;
import org.sbolstandard.core2.Range;
import org.sbolstandard.core2.SBOLConversionException;
import org.sbolstandard.core2.SBOLDocument;
import org.sbolstandard.core2.SBOLReader;
import org.sbolstandard.core2.SBOLValidationException;
import org.sbolstandard.core2.SequenceAnnotation;
import org.sbolstandard.core2.TopLevel;

public class count_classes {

	private static final String COMMA_DELIMITER = ",";
	private static final String NEW_LINE_SEPARATOR = "\n";
	private static String file_header = "";
	private static final String file_name = "count_classes.csv";
	private static final String classStatsFName = "class_stats.csv";
	private static ArrayList<cluster> nodes = null;
	private static FileWriter fileWriter = null;
	private static FileWriter classStatsWriter = null;
	// map class to number of times it appears in each file
	private static HashMap<String, Integer> class_counts = new HashMap<String, Integer>();
	private static HashMap<String, Integer> final_class_counts = new HashMap<String, Integer>();

	private static HashMap<String, HashMap<String, Integer>> class_counts_2d = null;
	private static HashSet<String> list_of_files = new HashSet<String>();
	private static Set<HashSet<String>> clusters = new HashSet<HashSet<String>>();
	private static HashSet<String> keys = new HashSet<String>();

	private static HashMap<String, HashMap<String, Boolean>> class_field_counts = null;
	private static HashMap<String, HashMap<String, HashMap<String, Boolean>>> class_field_counts_2d = null;

	private static cluster_analysis ca = null;

	public static void main(String[] args)
			throws SBOLValidationException, IOException, SBOLConversionException, URISyntaxException {
		initialize_classes();
		class_property_coverage();
		fileWriter = new FileWriter(file_name);
		fileWriter.append(COMMA_DELIMITER);
		file_header = "";

		classStatsWriter = new FileWriter(classStatsFName);
		//classStatsWriter.append(COMMA_DELIMITER);
		initialize_final_classes();

		String class_header = "";
		for (String data_type : class_counts.keySet()) {
			file_header += data_type + ",";
		}

		fileWriter.append(file_header.toString());
		class_counts_2d = new HashMap<String, HashMap<String, Integer>>();
		class_field_counts_2d = new HashMap<String, HashMap<String, HashMap<String, Boolean>>>();
		// for each file in the examples folder, call count_classes_test
		//./SBOLTestSuite/SBOL2/
		//C:\\Users\\Meher\\Documents\\Masters_Program\\TestSuites\\SBOLTestSuite\\SBOL2
		//C:\\Users\\Meher\\Documents\\Masters_Program\\thesis\\SBOLTestCharacterization\\SBOLTestSuite\\SBOL2
		//"/src/test/resources/SBOLTestSuite/SBOL2"
		for (File f : new File(count_classes.class.getResource("/SBOLTestSuite/SBOL2/").toURI()).listFiles()) {
			initialize_classes(); // resets the data types' count to 0
			//class_property_coverage();
			System.out.println("working on: " + f.getName());
			SBOLDocument doc = readDoc(f);
			//count_fields_test(doc, f.getName());
			count_classes_test(doc, f.getName()); // counts instances of each data type
			// associates file with the counts of each type
			class_counts_2d.put(f.getName(), class_counts);
			//class_field_counts_2d.put(f.getName(), class_field_counts);
			for (String key : class_counts.keySet()) {
				int fcc = final_class_counts.get(key);
				int cc = class_counts.get(key);
				final_class_counts.put(key, fcc + cc);
			}
			list_of_files.add(f.getName()); // list of total files

		}
		for (String data_type : final_class_counts.keySet()) {
			String percentAppears = "=" + final_class_counts.get(data_type) + "/" + list_of_files.size();
			class_header = data_type + "," + final_class_counts.get(data_type) + "," + percentAppears + "\n";
			classStatsWriter.append(class_header.toString());
			class_header = "";
		}
		try {
			fileWriter.flush();
			fileWriter.close();
			classStatsWriter.flush();
			classStatsWriter.close();
		} catch (Exception e) {
			System.out.println("Attempted to flush and close writer");
			e.printStackTrace();
		}
		create_clusters();

	}

	private static void create_clusters() throws SBOLValidationException, IOException, SBOLConversionException {
		HashMap<HashSet<String>, Set<String>> data_types_clusters = new HashMap<HashSet<String>, Set<String>>();

		while (list_of_files.size() != 0) {
			int rand = new Random().nextInt(list_of_files.size());
			String file = (String) list_of_files.toArray()[rand];
			list_of_files.remove(file);
			HashSet<String> cluster_to_add = new HashSet<String>();
			Set<String> data_types = new HashSet<String>();
			cluster_to_add.add(file);

			for (String type : class_counts_2d.get(file).keySet()) {
				if (class_counts_2d.get(file).get(type) != 0)
					data_types.add(type);
			}
			HashSet<String> files_to_remove = new HashSet<String>();
			for (String s : list_of_files) // check against every other file
			{
				// get the data for the file chosen g
				HashMap<String, Integer> set_given = class_counts_2d.get(file);
				// get the data for every other file
				HashMap<String, Integer> set_to_check = class_counts_2d.get(s);

				Boolean flag = true;
				for (String dt : set_given.keySet()) // for each data type
				{
					if (set_given.get(dt) != 0 && set_to_check.get(dt) == 0) {
						flag = false;
						break;
					} else if (set_given.get(dt) == 0 && set_to_check.get(dt) != 0) {
						flag = false;
						break;
					}
				}

				if (flag) {
					cluster_to_add.add(s);
					files_to_remove.add(s);
				}
			}
			clusters.add(cluster_to_add);
			list_of_files.removeAll(files_to_remove);
			// files and then the data_types for that group of files
			data_types_clusters.put(cluster_to_add, data_types);
		}

		// create actual cluster objects and put them in a list to make graph
		// from
		int id_count = 1;
		nodes = new ArrayList<cluster>();
		for (HashSet<String> s : data_types_clusters.keySet()) {
			nodes.add(new cluster(id_count, data_types_clusters.get(s), s));
			id_count++;
		}

		create_cluster_relations(nodes);

	}

	private static void create_cluster_relations(ArrayList<cluster> _nodes) throws IOException {
		// have all the clusters, must create connections between them
		for (int i = 0; i < _nodes.size(); i++) // parent
		{
			for (int j = 0; j < _nodes.size(); j++) // child
			{
				if (_nodes.get(i) == _nodes.get(j)) // parent == child; same
													// node
					continue;
				// child not a subset of parent so no relation
				if (!_nodes.get(i).get_data_types().containsAll(_nodes.get(j).get_data_types()))
					continue;
				boolean flag = true;
				for (int k = 0; k < _nodes.size(); k++) // rest of clusters
				{
					// rest of clusters not parent or child
					if (_nodes.get(k) == _nodes.get(j) || _nodes.get(k) == _nodes.get(i)) {
						continue;
					}
					// if other is a subset of parent
					if (_nodes.get(i).get_data_types().containsAll(_nodes.get(k).get_data_types()))
						// parent and child don't have direct relations
						if (_nodes.get(k).get_data_types().containsAll(_nodes.get(j).get_data_types())) {
							flag = false;
							break;
						}
				}
				if (flag)
					_nodes.get(i).add_connections(_nodes.get(j));
				// parent and child have a direct connection so set parent's connections to have
				// child
			}

		}
		set_source(_nodes);
		// draw_graph(_nodes);
		// data(_nodes);
		ca = new cluster_analysis(_nodes, list_of_files);
	}

	private static void set_source(ArrayList<cluster> _nodes) {
		for (cluster node : _nodes) {
			node.set_source(true);
			for (cluster conn : _nodes) {
				if (!node.equals(conn)) {
					for (cluster c : conn.get_connections()) {
						if (c.equals(node)) {
							node.set_source(false);
						}
					}

				}
			}
		}
	}

	private static SBOLDocument readDoc(File file)
			throws SBOLValidationException, IOException, SBOLConversionException {
		SBOLDocument doc = new SBOLDocument();

		// read serialized file into a document, then
		SBOLReader.setCompliant(false);
		SBOLReader.setURIPrefix("http://www.async.ece.utah.edu");
		SBOLReader.setVersion("");

		if (file.getName().contains(".xml"))
			doc = SBOLReader.read(file);

		return doc;
	}

	private static void count_classes_test(SBOLDocument doc, String fileName)
			throws SBOLValidationException, IOException, SBOLConversionException {

		// place toplevel objects
		// class_counts.put("TopLevel", doc.getTopLevels().size());
		class_counts.put("Collection", doc.getCollections().size());
		class_counts.put("ComponentDefinition", doc.getComponentDefinitions().size());
		class_counts.put("Model", doc.getModels().size());
		class_counts.put("ModuleDefinition", doc.getModuleDefinitions().size());
		class_counts.put("Sequence", doc.getSequences().size());
		class_counts.put("GenericTopLevel", doc.getGenericTopLevels().size());
		class_counts.put("Attachment", doc.getAttachments().size());
		class_counts.put("CombinatorialDerivation", doc.getCombinatorialDerivations().size());
		class_counts.put("Implementation", doc.getImplementations().size());
		class_counts.put("Activity", doc.getActivities().size());
		class_counts.put("Plan", doc.getPlans().size());
		class_counts.put("Agent", doc.getAgents().size());

		for (Activity act : doc.getActivities()) {
			class_counts.put("Association", act.getAssociations().size());
			class_counts.put("Usage", act.getUsages().size());

			for (Association assoc : act.getAssociations()) {
				if (assoc.getPlan() != null)
					class_counts.put("Plan", class_counts.get("Plan") + 1);
				if (assoc.getAgent() != null)
					class_counts.put("Agent", class_counts.get("Agent") + 1);

			}
		}
		
		for(CombinatorialDerivation combDer : doc.getCombinatorialDerivations())
		{
			int count = 0; 
			if(combDer.getVariableComponents() != null) {
				count = combDer.getVariableComponents().size();
				
			}
			class_counts.put("VariableComponent", class_counts.get("VariableComponent") + count );

		}

		for (TopLevel TL : doc.getTopLevels()) {
			class_counts.put("Annotation", class_counts.get("Annotation") + TL.getAnnotations().size());
			// for (Annotation a : TL.getAnnotations())
			// put_annotations(a);
		}

		// for (Collection c : doc.getCollections()) {
		// for (Annotation a : c.getAnnotations())
		// put_annotations(a);
		// }

		for (ComponentDefinition cd : doc.getComponentDefinitions()) {
			// for (Annotation a : cd.getAnnotations()) {
			// put_annotations(a);
			// }

			class_counts.put("Component", class_counts.get("Component") + cd.getComponents().size());
			for (Component c : cd.getComponents()) {
				// for (Annotation a : c.getAnnotations())
				// put_annotations(a);
				class_counts.put("MapsTo", class_counts.get("MapsTo") + c.getMapsTos().size());

				// class_counts.put("Component-MapsTo", class_counts.get("Component-MapsTo") +
				// c.getMapsTos().size());

				// for (MapsTo mp : c.getMapsTos())
				// for (Annotation a : mp.getAnnotations())
				// put_annotations(a);
			}

			class_counts.put("SequenceAnnotation",
					class_counts.get("SequenceAnnotation") + cd.getSequenceAnnotations().size());
			for (SequenceAnnotation sa : cd.getSequenceAnnotations()) {
				// for (Annotation a : sa.getAnnotations())
				// put_annotations(a);
				// class_counts.put("Location", class_counts.get("Location") +
				// sa.getLocations().size());

				for (Location l : sa.getLocations()) {
					// for (Annotation a : l.getAnnotations())
					// put_annotations(a);
					if (l instanceof Cut)
						class_counts.put("Cut", class_counts.get("Cut") + 1);
					if (l instanceof Range)
						class_counts.put("Range", class_counts.get("Range") + 1);
					if (l instanceof GenericLocation)
						class_counts.put("GenericLocation", class_counts.get("GenericLocation") + 1);
				}
			}
			class_counts.put("SequenceConstraint",
					class_counts.get("SequenceConstraint") + cd.getSequenceConstraints().size());
			// for (SequenceConstraint sc : cd.getSequenceConstraints())
			// for (Annotation a : sc.getAnnotations())
			// put_annotations(a);
		}

		// for (Model m : doc.getModels()) {
		// for (Annotation a : m.getAnnotations())
		// put_annotations(a);
		// }

		for (ModuleDefinition md : doc.getModuleDefinitions()) {
			class_counts.put("FunctionalComponent",
					class_counts.get("FunctionalComponent") + md.getFunctionalComponents().size());
			for (FunctionalComponent fc : md.getFunctionalComponents()) {
				//// for (Annotation a : fc.getAnnotations())
				//// put_annotations(a);
				class_counts.put("MapsTo", class_counts.get("MapsTo") + fc.getMapsTos().size());
				// class_counts.put("FC-MapsTo", class_counts.get("FC-MapsTo") +
				// fc.getMapsTos().size());
				//
				// for (MapsTo mp : fc.getMapsTos())
				// for (Annotation a : mp.getAnnotations())
				// put_annotations(a);
				//
			}

			class_counts.put("Interaction", class_counts.get("Interaction") + md.getInteractions().size());
			for (Interaction i : md.getInteractions()) {
				class_counts.put("Participation", class_counts.get("Participation") + i.getParticipations().size());
				// for (Annotation a : i.getAnnotations())
				// put_annotations(a);
			}

			class_counts.put("Model", class_counts.get("Model") + md.getModels().size());

			class_counts.put("Module", class_counts.get("Module") + md.getModules().size());
			for (Module m : md.getModules()) {
				// for (Annotation a : m.getAnnotations())
				// put_annotations(a);
				// class_counts.put("Module-MapsTo", class_counts.get("Module-MapsTo") +
				// m.getMapsTos().size());
				class_counts.put("MapsTo", class_counts.get("MapsTo") + m.getMapsTos().size());

				// for (MapsTo mp : m.getMapsTos())
				// for (Annotation a : mp.getAnnotations())
				// put_annotations(a);

			}
		}

		// GenericTopLevel's have nothing but annotations

		create_spreadsheet(fileName);

	}


	// private static void put_annotations(Annotation a) {
	// if (a.isBooleanValue()) {
	// class_counts.put("Boolean_Annotation", class_counts.get("Boolean_Annotation")
	// + 1);
	// } else if (a.isIntegerValue()) {
	// class_counts.put("Integer_Annotation", class_counts.get("Integer_Annotation")
	// + 1);
	// } else if (a.isStringValue()) {
	// class_counts.put("String_Annotation", class_counts.get("String_Annotation") +
	// 1);
	// } else if (a.isDoubleValue())// must be a double value
	// {
	// class_counts.put("Double_Annotation", class_counts.get("Double_Annotation") +
	// 1);
	// } else // must be a URI value
	// {
	// class_counts.put("URI_Annotation", class_counts.get("URI_Annotation") + 1);
	// }
	// if (a.isNestedAnnotations()) {
	// class_counts.put("Nested_Annotation", class_counts.get("Nested_Annotation") +
	// 1);
	// for (Annotation sub_annotation : a.getAnnotations()) {
	// put_annotations(sub_annotation);
	// }
	// }
	// }

	private static void create_spreadsheet(String filename) {
		try {
			fileWriter.append(NEW_LINE_SEPARATOR);
			fileWriter.append(filename);
			fileWriter.append(COMMA_DELIMITER);
			for (String data_type : class_counts.keySet()) {
				fileWriter.append(class_counts.get(data_type).toString());
				fileWriter.append(COMMA_DELIMITER);
			}

		} catch (Exception e) {
			System.out.println("Error when writing file data" + filename);

		}
	}

	private static void initialize_classes() {
		class_counts = new HashMap<String, Integer>();

		class_counts.put("Activity", 0);
		class_counts.put("Agent", 0);
		class_counts.put("Annotation", 0);
		class_counts.put("Association", 0);
		class_counts.put("Attachment", 0);
		// class_counts.put("Boolean_Annotation", 0);
		// class_counts.put("Integer_Annotation", 0);
		// class_counts.put("String_Annotation", 0);
		// class_counts.put("Nested_Annotation", 0);
		// class_counts.put("Double_Annotation", 0);
		// class_counts.put("URI_Annotation", 0);
		class_counts.put("Collection", 0);
		class_counts.put("CombinatorialDerivation", 0);
		class_counts.put("Component", 0);
		class_counts.put("ComponentDefinition", 0);
		class_counts.put("Cut", 0);
		class_counts.put("FunctionalComponent", 0);
		class_counts.put("GenericLocation", 0);
		class_counts.put("GenericTopLevel", 0);
		class_counts.put("Implementation", 0);
		class_counts.put("Interaction", 0);
		// class_counts.put("Location", 0);
		class_counts.put("MapsTo", 0);
		// class_counts.put("Component-MapsTo", 0);
		// class_counts.put("FC-MapsTo", 0);
		// class_counts.put("Module-MapsTo", 0);
		class_counts.put("Model", 0);
		class_counts.put("Module", 0);
		class_counts.put("ModuleDefinition", 0);
		class_counts.put("Participation", 0);
		class_counts.put("Plan", 0);
		class_counts.put("Range", 0);
		class_counts.put("Sequence", 0);
		class_counts.put("SequenceAnnotation", 0);
		class_counts.put("SequenceConstraint", 0);
		class_counts.put("Usage", 0);
		class_counts.put("VariableComponent", 0);

		// class_counts.put("TopLevel", 0);
		keys.addAll(class_counts.keySet());

	}

	private static void initialize_final_classes() {
		final_class_counts = new HashMap<String, Integer>();

		final_class_counts.put("Activity", 0);
		final_class_counts.put("Agent", 0);
		final_class_counts.put("Annotation", 0);
		final_class_counts.put("Association", 0);
		final_class_counts.put("Attachment", 0);
		// final_class_counts.put("Boolean_Annotation", 0);
		// final_class_counts.put("Integer_Annotation", 0);
		// final_class_counts.put("String_Annotation", 0);
		// final_class_counts.put("Nested_Annotation", 0);
		// final_class_counts.put("Double_Annotation", 0);
		// final_class_counts.put("URI_Annotation", 0);
		final_class_counts.put("Collection", 0);
		final_class_counts.put("CombinatorialDerivation", 0);
		final_class_counts.put("Component", 0);
		final_class_counts.put("ComponentDefinition", 0);
		final_class_counts.put("Cut", 0);
		final_class_counts.put("FunctionalComponent", 0);
		final_class_counts.put("GenericLocation", 0);
		final_class_counts.put("GenericTopLevel", 0);
		final_class_counts.put("Implementation", 0);
		final_class_counts.put("Interaction", 0);
		// final_class_counts.put("Location", 0);
		final_class_counts.put("MapsTo", 0);
		// final_class_counts.put("Component-MapsTo", 0);
		// final_class_counts.put("FC-MapsTo", 0);
		// final_class_counts.put("Module-MapsTo", 0);
		final_class_counts.put("Model", 0);
		final_class_counts.put("Module", 0);
		final_class_counts.put("ModuleDefinition", 0);
		final_class_counts.put("Participation", 0);
		final_class_counts.put("Plan", 0);
		final_class_counts.put("Range", 0);
		final_class_counts.put("Sequence", 0);
		final_class_counts.put("SequenceAnnotation", 0);
		final_class_counts.put("SequenceConstraint", 0);
		final_class_counts.put("Usage", 0);
		final_class_counts.put("VariableComponent", 0);
		// final_class_counts.put("TopLevel", 0);

	}

	private static void class_property_coverage() {
		class_field_counts = new HashMap<String, HashMap<String, Boolean>>();

		HashMap<String, Boolean> fields = new HashMap<String, Boolean>();
		fields.put("associations", false);
		fields.put("usages", false);
		fields.put("endedAtTime", false);
		fields.put("startedAtTime", false);
		fields.put("wasInformedBys", false);
		class_field_counts.put("Activity", fields);

		fields = new HashMap<String, Boolean>();
		fields.put("agent", false);
		fields.put("roles", false);
		fields.put("plan", false);
		class_field_counts.put("Association", fields);

		fields = new HashMap<String, Boolean>();
		fields.put("source", false);
		fields.put("format", false);
		fields.put("size", false);
		fields.put("hash", false);
		class_field_counts.put("Attachment", fields);

		fields = new HashMap<String, Boolean>();
		fields.put("members", false);
		class_field_counts.put("Collection", fields);

		fields = new HashMap<String, Boolean>();
		fields.put("template", false);
		fields.put("variableComponents", false);
		fields.put("strategy", false);
		class_field_counts.put("CombinatorialDerivation", fields);

		fields = new HashMap<String, Boolean>();
		fields.put("roles", false);
		fields.put("roleIntegration", false);
		class_field_counts.put("Component", fields);

		fields = new HashMap<String, Boolean>();
		fields.put("types", false);
		fields.put("roles", false);
		fields.put("sequences", false);
		fields.put("components", false);
		fields.put("sequenceAnnotations", false);
		fields.put("sequenceConstraints", false);
		class_field_counts.put("ComponentDefinition", fields);

		fields = new HashMap<String, Boolean>();
		fields.put("orientation", false);
		fields.put("at", false);
		class_field_counts.put("Cut", fields);

		fields = new HashMap<String, Boolean>();
		fields.put("direction", false);
		class_field_counts.put("FunctionalComponent", fields);

		fields = new HashMap<String, Boolean>();
		fields.put("orientation", false);
		class_field_counts.put("GenericLocation", fields);

		fields = new HashMap<String, Boolean>();
		fields.put("rdfType", false);
		class_field_counts.put("GenericTopLevel", fields);

		fields = new HashMap<String, Boolean>();
		fields.put("built", false);
		class_field_counts.put("Implementation", fields);

		fields = new HashMap<String, Boolean>();
		fields.put("types", false);
		fields.put("participations", false);
		class_field_counts.put("Interaction", fields);

		fields = new HashMap<String, Boolean>();
		fields.put("local", false);
		fields.put("remote", false);
		fields.put("refinement", false);
		class_field_counts.put("MapsTo", fields);

		fields = new HashMap<String, Boolean>();
		fields.put("subject", false);
		fields.put("object", false);
		fields.put("restriction", false);
		class_field_counts.put("Model", fields);

		fields = new HashMap<String, Boolean>();
		fields.put("definition", false);
		fields.put("mapsTo", false);
		class_field_counts.put("Module", fields);

		fields = new HashMap<String, Boolean>();
		fields.put("roles", false);
		fields.put("modules", false);
		fields.put("functionalComponents", false);
		fields.put("interactions", false);
		fields.put("models", false);
		class_field_counts.put("ModuleDefinition", fields);

		fields = new HashMap<String, Boolean>();
		fields.put("roles", false);
		fields.put("participant", false);
		class_field_counts.put("Participation", fields);

		fields = new HashMap<String, Boolean>();
		fields.put("orientation", false);
		fields.put("start", false);
		fields.put("end", false);
		class_field_counts.put("Range", fields);

		fields = new HashMap<String, Boolean>();
		fields.put("elements", false);
		fields.put("encoding", false);
		class_field_counts.put("Sequence", fields);

		fields = new HashMap<String, Boolean>();
		fields.put("locations", false);
		fields.put("component", false);
		fields.put("roles", false);
		class_field_counts.put("SequenceAnnotation", fields);

		fields = new HashMap<String, Boolean>();
		fields.put("subject", false);
		fields.put("object", false);
		fields.put("restriction", false);
		class_field_counts.put("SequenceConstraint", fields);

		fields = new HashMap<String, Boolean>();
		fields.put("entity", false);
		fields.put("roles", false);
		class_field_counts.put("Usage", fields);

		// final_class_counts.put("Annotation", 0);
		// final_class_counts.put("Boolean_Annotation", 0);
		// final_class_counts.put("Integer_Annotation", 0);
		// final_class_counts.put("String_Annotation", 0);
		// final_class_counts.put("Nested_Annotation", 0);
		// final_class_counts.put("Double_Annotation", 0);
		// final_class_counts.put("URI_Annotation", 0);

		// final_class_counts.put("Location", 0);
		// final_class_counts.put("Component-MapsTo", 0);
		// final_class_counts.put("FC-MapsTo", 0);
		// final_class_counts.put("Module-MapsTo", 0);
		// final_class_counts.put("TopLevel", 0);

	}

}

