package org.sboltestcharacterization;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class cluster_analysis {

	private static ArrayList<cluster> nodes = null;
	private static HashMap<String, HashSet<String>> pairs = null;
	private static HashSet<String> files = null;

	public cluster_analysis(ArrayList<cluster> _nodes, HashSet<String> list_of_files) throws IOException {
		nodes = _nodes;
		files = list_of_files;
		required_type_pairs();
		draw_graph();
		data();
		is_graph_complete();
	}

	private static String which_type(cluster c) {
		Set<String> data_types = c.get_data_types();

		if(data_types.size() == 0)
			return "slategrey";
		
		else if (data_types.size() > 0) {

			// structural && functional
			if ((data_types.contains("ModuleDefinition") || data_types.contains("Model"))
					&& (data_types.contains("Sequence") || data_types.contains("ComponentDefinition")
							|| data_types.contains("Implementation") || data_types.contains("CombinatorialDerivation"))
					&& (!data_types.contains("Collection") && !data_types.contains("GenericTopLevel")
							&& !data_types.contains("Activity") && !data_types.contains("Attachment")
							&& !data_types.contains("Plan") && !data_types.contains("Agent")))
				return "salmon";

//			// aux & structural
//			if ((data_types.contains("Collection") || data_types.contains("GenericTopLevel")
//					|| data_types.contains("Activity") || data_types.contains("Attachment")
//					|| data_types.contains("Plan") || data_types.contains("Agent"))
//					&& (data_types.contains("Sequence") || data_types.contains("ComponentDefinition")
//							|| data_types.contains("Implementation") || data_types.contains("CombinatorialDerivation"))
//					&& (!data_types.contains("ModuleDefinition") && !data_types.contains("Model"))) {
//				return "blueviolet";
//			}
//
//			// aux & functional
//			if ((data_types.contains("Collection") || data_types.contains("GenericTopLevel")
//					|| data_types.contains("Activity") || data_types.contains("Attachment")
//					|| data_types.contains("Plan") || data_types.contains("Agent"))
//					&& (!data_types.contains("Sequence") && !data_types.contains("ComponentDefinition")
//							&& !data_types.contains("Implementation")
//							&& !data_types.contains("CombinatorialDerivation"))
//					&& (data_types.contains("ModuleDefinition") || data_types.contains("Model"))) {
//				return "dodgerblue";
//			}
			// structural
			if ((!data_types.contains("ModuleDefinition") && !data_types.contains("Model"))
					&& !data_types.contains("Collection") && !data_types.contains("GenericTopLevel")
					&& !data_types.contains("Activity") && !data_types.contains("Attachment")
					&& !data_types.contains("Plan") && !data_types.contains("Agent"))
				return "yellow";

			// functional
			if ((!data_types.contains("Sequence") && !data_types.contains("ComponentDefinition"))
					&& !data_types.contains("Collection") && !data_types.contains("GenericTopLevel")
					&& !data_types.contains("Activity") && !data_types.contains("Attachment")
					&& !data_types.contains("Plan") && !data_types.contains("Agent")
					&& !data_types.contains("Implementation") && !data_types.contains("CombinatorialDerivation"))
				return "green";

			// auxiliary classes only
			if ((data_types.contains("Collection") || data_types.contains("GenericTopLevel")
					|| data_types.contains("Activity") || data_types.contains("Attachment")
					|| data_types.contains("Plan") || data_types.contains("Agent"))
					&& (!data_types.contains("Sequence") && !data_types.contains("ComponentDefinition")
							&& !data_types.contains("Implementation") && !data_types.contains("CombinatorialDerivation")
							&& !data_types.contains("ModuleDefinition") && !data_types.contains("Model"))) {
				return "royalblue";
			}

//			// all
			if ((data_types.contains("Sequence") || data_types.contains("ComponentDefinition")
							|| data_types.contains("Implementation") || data_types.contains("CombinatorialDerivation"))
					&& (data_types.contains("ModuleDefinition") || data_types.contains("Model"))
					|| (data_types.contains("Collection") || data_types.contains("GenericTopLevel")
							|| data_types.contains("Activity") || data_types.contains("Attachment")
							|| data_types.contains("Plan") || data_types.contains("Agent"))) {
				return "salmon";
			}
//			// none
//			if ((!data_types.contains("Collection") && !data_types.contains("GenericTopLevel")
//					&& !data_types.contains("Activity") && !data_types.contains("Attachment")
//					&& !data_types.contains("Plan") && !data_types.contains("Agent"))
//					&& !data_types.contains("Sequence") && !data_types.contains("ComponentDefinition")
//					&& !data_types.contains("Implementation") && !data_types.contains("CombinatorialDerivation")
//					&& !data_types.contains("ModuleDefinition") && !data_types.contains("Model")) {
//				return "slategrey";
//			}
		}

		return "salmon";// "violet";
		
	}

	private static void draw_graph() throws IOException {
		System.out.println("number of nodes: " + nodes.size());
		data();
		File f = new File("graph.dot");
		File data = new File("class_relation_data.txt");
		File cluster_groups = new File("Cluster_Class_Data.txt");
		File cluster_files = new File("Cluster_File_Data.txt");

		if (!f.exists() || !data.exists() || !cluster_groups.exists()) {
			f.createNewFile();
			data.createNewFile();
			cluster_groups.createNewFile();
		}

		FileWriter fw = new FileWriter(f.getAbsoluteFile());
		BufferedWriter bw = new BufferedWriter(fw);

		FileWriter fw_data = new FileWriter(data.getAbsoluteFile());
		BufferedWriter bw_data = new BufferedWriter(fw_data);

		FileWriter fw_clusters = new FileWriter(cluster_groups.getAbsoluteFile());
		BufferedWriter bw_clusters = new BufferedWriter(fw_clusters);

		FileWriter fw_cluster_files = new FileWriter(cluster_files.getAbsoluteFile());
		BufferedWriter bw_cluster_files = new BufferedWriter(fw_cluster_files);

		bw_clusters.write("number of files : " + files);
		bw.write("digraph G {\n\n");
		// bw.write(nodes.size() + 1 + " [label=root");
		// bw.write("]");
		// bw.write("\n\n");

		for (cluster c : nodes) {
			bw_cluster_files.write(which_type(c) + ":" + c.get_files().size());
			bw_cluster_files.write("\n");
		}

		for (cluster c : nodes) {
			if (c.get_data_types().size() > 0) {
				for (String dataType : c.get_data_types()) {
					bw_clusters.write(dataType + ",");
				}
			}
			bw_clusters.write("\n");
			if (c.get_data_types().size() > 0) {
				bw.write(c.get_cluster_id() + " [label = ");
				bw.write((char) 34);
				bw.write(c.get_cluster_id() + ":");
				bw.write(c.get_data_types().size() + "(" + c.get_files().size() + ")");
				bw.write((char) 34);
				String color = which_type(c);
				if (color != "")
					bw.write("color=" + color + " " + "style=filled");
				bw.write("]");
				bw.write("\n\n");
			}
		}

		// go through each relation
		for (cluster c : nodes) {
			for (cluster conn : c.get_connections()) {
				// // connect source nodes to root
				// if (c.get_source())
				// bw.write((nodes.size() + 1) + " -> " +conn.get_cluster_id() + "\n");

				// set connection relations
				bw.write(c.get_cluster_id() + " -> " + conn.get_cluster_id() + "\n");
			}
			bw.write("\n");
		}
		bw.write("}");
		bw.close();
		bw_clusters.close();
		for (cluster c : nodes) {
			bw_data.write(c.get_cluster_id() + "");
			bw_data.write("\n");
			bw_data.write("Source? : " + c.get_source() + "\n");
			bw_data.write("File count: " + c.get_files().size() + "\n");
			bw_data.write("Files: ");
			for (String file : c.get_files())
				bw_data.write(file + ", ");
			bw_data.write("\n");
			bw_data.write("Connections: ");
			for (cluster conn : c.get_connections())
				bw_data.write(conn.get_cluster_id() + ", ");
			bw_data.write("\n");
			bw_data.write("Data Types: ");
			for (String type : c.get_data_types())
				bw_data.write(type + ", ");
			bw_data.write("\n************************************\n");

		}

		bw_data.close();
		bw_cluster_files.close();
	}

	private static void data() {

		for (cluster c : nodes) {
			System.out.println(c.get_cluster_id() + "\n");
			System.out.println("Files: ");
			for (String file : c.get_files())
				System.out.println(file + ", ");
			System.out.println("Connections: ");
			for (cluster conn : c.get_connections())
				System.out.println(conn.get_cluster_id() + ", ");
			System.out.println("Data Types: ");
			for (String type : c.get_data_types())
				System.out.println(type + ", ");
			System.out.println("\n************************************\n");

		}

	}

	private static void is_graph_complete() throws IOException {
		File data = new File("graph_completeness.txt");

		if (!data.exists()) {
			data.createNewFile();
		}

		FileWriter fw = new FileWriter(data.getAbsoluteFile());
		BufferedWriter bw = new BufferedWriter(fw);

		for (cluster parent : nodes) {
			Set<String> child_dtypes = new HashSet<String>();
			if (parent.get_connections().size() != 0) {
				for (cluster child : parent.get_connections()) {
					child_dtypes.addAll(child.get_data_types());
				}
				if (child_dtypes.size() == 0) {
					bw.write("\n" + parent.get_cluster_id() + "\n");
					bw.write("children have no data types: Complete Set\n");
				} else if (isLeaf(parent)) {
					bw.write("\n" + parent.get_cluster_id() + "\n");
					bw.write("Leaf Node: Complete Set\n");
				} else if (parent.get_data_types().equals(child_dtypes)) {

					bw.write("\n" + parent.get_cluster_id() + "\n");
					bw.write("Children exist in Parent: Complete Set\n");

				} else {
					bw.write("\n" + parent.get_cluster_id() + "\n");
					bw.write("types: ");

					for (String ptype : parent.get_data_types())
						bw.write(ptype + ", ");

					bw.write("\n");

					bw.write("child types: ");
					for (String ctype : child_dtypes)
						bw.write(ctype + ", ");

					bw.write("\n");

					bw.write("Need: ");
					for (String ptype : parent.get_data_types()) {
						if (!child_dtypes.contains(ptype))
							bw.write(ptype + ", ");
					}
				}
				bw.write("\n");
			} else {
				bw.write(parent.get_cluster_id() + "\n" + "Node is leaf : Complete Set\n");
			}
		}

		bw.close();
		fw.close();
	}

	private static boolean isLeaf(cluster c) {
		if (c.get_data_types().size() == 1) {
			for (String dataType : c.get_data_types()) {
				if (dataType.equals("Collection"))
					return true;
				if (dataType.equals("ModuleDefinition"))
					return true;
				if (dataType.equals("ComponentDefinition"))
					return true;
				if (dataType.equals("Sequence"))
					return true;
				if (dataType.equals("Model"))
					return true;
				if (dataType.equals("GenericTopLevel"))
					return true;
				if (dataType.equals("Attachment"))
					return true;
				if (dataType.equals("Implementation"))
					return true;
				if (dataType.equals("CombinatorialDerivation"))
					return true;
				if (dataType.equals("Activity"))
					return true;

			}
		}

		return false;
	}

	private static void required_type_pairs() {
		pairs = new HashMap<String, HashSet<String>>();

		String[] pair = new String[] { "Agent" };
		HashSet<String> pairset = new HashSet<String>(Arrays.asList(pair));
		pairs.put("Association", pairset);

		pair = new String[] { "Location" };
		pairset = new HashSet<String>(Arrays.asList(pair));
		pairs.put("SequenceAnnotation", pairset);

		pair = new String[] { "Component" };
		pairset = new HashSet<String>(Arrays.asList(pair));
		pairs.put("SequenceConstraint", pairset);

		pair = new String[] { "ModuleDefinition" };
		pairset = new HashSet<String>(Arrays.asList(pair));
		pairs.put("Module", pairset);

		pair = new String[] { "FunctionalComponent" };
		pairset = new HashSet<String>(Arrays.asList(pair));
		pairs.put("Participation", pairset);

		pair = new String[] { "ComponentDefinition" };
		pairset = new HashSet<String>(Arrays.asList(pair));
		pairs.put("CombinatorialDerivation", pairset);

		pair = new String[] { "Component" };
		pairset = new HashSet<String>(Arrays.asList(pair));
		pairs.put("VariableComponent", pairset);

	}
}
