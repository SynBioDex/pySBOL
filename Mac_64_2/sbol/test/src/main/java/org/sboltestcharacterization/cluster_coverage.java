package org.sboltestcharacterization;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class cluster_coverage {

	private static HashSet<HashSet<String>> clusters = null;

	public static void main(String[] args) throws FileNotFoundException {

		File clusterClassGroups = new File("./Cluster_Class_Data.txt");
		File combosFile = new File("./ClassCombinations.txt");

		Scanner scan_clusters = new Scanner(new BufferedReader(new FileReader(clusterClassGroups)));
		Scanner scan_combos = new Scanner(new BufferedReader(new FileReader(combosFile)));

		clusters = new HashSet<HashSet<String>>();
		HashSet<HashSet<String>> combos = new HashSet<HashSet<String>>();

		// while(scan_combos.hasNextLine())
		// {
		// String line = scan_combos.nextLine();
		// line = line.trim();
		// String[] types = line.split(",");
		// HashSet<String> c = new HashSet<String>();
		// for(String type : types)
		// c.add(type);
		// combos.add(c);
		// }
		//
		while (scan_clusters.hasNextLine()) {
			String line = scan_clusters.nextLine();
			String[] types = line.split(",");
			HashSet<String> c = new HashSet<String>();
			for (String type : types)
				c.add(type);
			clusters.add(c);
		}

		HashSet<String> types = cluster_types(clusters);
		SBOL2_coverage_stats(types);
		//
		// for(HashSet<String> c : combos)
		// {
		// for(String s : c)
		// System.out.print(s + ",");
		// System.out.print("\n");
		// }
		//
		 int count = 0;
		 for(HashSet<String> combo : combos)
		 {
		 if(!clusters.contains(combo))
		 {
		 for(String s : combo)
		 System.out.print(s + ",");
		 System.out.println("\n");
		 count++;
		 }
		 }
		
		 System.out.println("Total combos: " + combos.size());
		 System.out.println("Total clusters: " + clusters.size());
		 System.out.println("Current Coverage: " + count);
		 System.out.println("Uncovered combos: " + (float)count/combos.size());
		
		scan_clusters.close();
		scan_combos.close();

	}

	public static void SBOL2_coverage_stats(HashSet<String> sbolTypes) throws FileNotFoundException {
		System.out.println("SBOL2 Coverage Statistics");
		File sbol2classes = new File("./SBOL2_Classes.txt");
		Scanner scan_classes = new Scanner(new BufferedReader(new FileReader(sbol2classes)));

		HashSet<String> classes = new HashSet<String>();

		while (scan_classes.hasNextLine()) {
			String line = scan_classes.nextLine();
			line = line.trim();
			String[] types = line.split("\n");
			for (String type : types) {
				classes.add(type);
			}
		}

		scan_classes.close();

		int count = 0;
		for (String s : classes) {
			if (!classes.contains(s)) {
				System.out.print(s + ",");
				System.out.println("\n");
				count++;
			}
		}

		File sbol2Files = new File("./Cluster_File_Data.txt");
		Scanner scan_clus_files = new Scanner(new BufferedReader(new FileReader(sbol2Files)));
		int structural = 0;
		int functional = 0;
		int auxillary = 0;
		int sAndF = 0;
		while (scan_clus_files.hasNextLine()) {
			String line = scan_clus_files.nextLine();
			line = line.trim();
			String[] types = line.split("\n");
			String[] t = types[0].split(":");
			String clusterType = t[0];
			int fileCount = Integer.parseInt(t[1]);

			if (clusterType.equals("green"))
				functional += fileCount;
			else if (clusterType.equals("yellow"))
				structural += fileCount;
			else if (clusterType.equals("royalblue"))
				auxillary += fileCount;
			else if (clusterType.equals("salmon"))
				sAndF += fileCount;
		}

		int totalFileCount = structural + functional + auxillary + sAndF;
		scan_classes.close();
		scan_clus_files.close();

		System.out.println("# of clusters: " + clusters.size());
		System.out.println("# of SBOL classes: " + classes.size());
		System.out.println("missing types: " + count);
		System.out.println("# of total examples: " + totalFileCount);

		System.out.println("# of structural examples: " + structural);
		System.out.println("# of functional examples: " + functional);
		System.out.println("# of auxillary examples: " + auxillary);
		System.out.println("# of s&f examples: " + sAndF);
		type_stats();

	}

	public static void combos_stats() {

	}

	public static HashSet<String> cluster_types(HashSet<HashSet<String>> clusters) {
		HashSet<String> types = new HashSet<String>();
		for (HashSet<String> c : clusters) {
			for (String s : c)
				if (!types.contains(s)) {
					types.add(s);
				}
		}
		return types;
	}

	private static void type_stats() {

		int structuralClusters = 0;
		int functionalClusters = 0;
		int auxillaryClusters = 0;
		int sAndf = 0;
		int sAnda = 0;
		int fAnda = 0;
		int all = 0;
		int none = 0; 
		for (HashSet<String> cluster : clusters) {

			// structural
			if ((!cluster.contains("ModuleDefinition") && !cluster.contains("Model")) && !cluster.contains("Collection")
					&& !cluster.contains("GenericTopLevel") && !cluster.contains("Activity")
					&& !cluster.contains("Attachment") && !cluster.contains("Plan") && !cluster.contains("Agent"))
				structuralClusters++;

			// functional
			if ((!cluster.contains("Sequence") && !cluster.contains("ComponentDefinition"))
					&& !cluster.contains("Collection") && !cluster.contains("GenericTopLevel")
					&& !cluster.contains("Activity") && !cluster.contains("Attachment") && !cluster.contains("Plan")
					&& !cluster.contains("Agent") && !cluster.contains("Implementation")
					&& !cluster.contains("CombinatorialDerivation"))
				functionalClusters++;

			// auxiliary classes only
			if ((cluster.contains("Collection") || cluster.contains("GenericTopLevel")
					|| cluster.contains("Activity") || cluster.contains("Attachment")
					|| cluster.contains("Plan") || cluster.contains("Agent"))
					&& (!cluster.contains("Sequence") && !cluster.contains("ComponentDefinition")
							&& !cluster.contains("Implementation") && !cluster.contains("CombinatorialDerivation")
							&& !cluster.contains("ModuleDefinition") && !cluster.contains("Model"))) {
				auxillaryClusters++;
			}
			// structural && functional
			if ((cluster.contains("ModuleDefinition") || cluster.contains("Model"))
					&& (cluster.contains("Sequence") || cluster.contains("ComponentDefinition")
							|| cluster.contains("Implementation") || cluster.contains("CombinatorialDerivation"))
					&& (!cluster.contains("Collection") && !cluster.contains("GenericTopLevel")
							&& !cluster.contains("Activity") && !cluster.contains("Attachment")
							&& !cluster.contains("Plan") && !cluster.contains("Agent")))
				sAndf++;

			// aux & structural
			if ((cluster.contains("Collection") || cluster.contains("GenericTopLevel") || cluster.contains("Activity")
					|| cluster.contains("Attachment") || cluster.contains("Plan") || cluster.contains("Agent"))
					&& (cluster.contains("Sequence") || cluster.contains("ComponentDefinition")
							|| cluster.contains("Implementation") || cluster.contains("CombinatorialDerivation"))
					&& (!cluster.contains("ModuleDefinition") && !cluster.contains("Model"))) {
				sAnda++;
			}

			// aux & functional
			if ((cluster.contains("Collection") || cluster.contains("GenericTopLevel") || cluster.contains("Activity")
					|| cluster.contains("Attachment") || cluster.contains("Plan") || cluster.contains("Agent"))
					&& (!cluster.contains("Sequence") && !cluster.contains("ComponentDefinition")
							&& !cluster.contains("Implementation") && !cluster.contains("CombinatorialDerivation"))
					&& (cluster.contains("ModuleDefinition") || cluster.contains("Model"))) {
				fAnda++;
			}
			// all
			if ((cluster.contains("Collection") || cluster.contains("GenericTopLevel")
					|| cluster.contains("Activity") || cluster.contains("Attachment")
					|| cluster.contains("Plan") || cluster.contains("Agent"))
					&& (cluster.contains("Sequence") || cluster.contains("ComponentDefinition")
							|| cluster.contains("Implementation") || cluster.contains("CombinatorialDerivation")
							|| cluster.contains("ModuleDefinition") || cluster.contains("Model"))) {
				all++;
			}
			
			// none
			if ((!cluster.contains("Collection") && !cluster.contains("GenericTopLevel")
					&& !cluster.contains("Activity") && !cluster.contains("Attachment")
					&& !cluster.contains("Plan") && !cluster.contains("Agent"))
					&& !cluster.contains("Sequence") && !cluster.contains("ComponentDefinition")
					&& !cluster.contains("Implementation") && !cluster.contains("CombinatorialDerivation")
					&& !cluster.contains("ModuleDefinition") && !cluster.contains("Model")) {
				none++;
			}
			
			if(cluster.size() == 0)
				none++;

		}

		System.out.println("# of structural clusters: " + structuralClusters);
		System.out.println("# of functional clusters: " + functionalClusters);
		System.out.println("# of auxillary clusters: " + auxillaryClusters);
		System.out.println("# of s&f clusters: " + sAndf);
		System.out.println("# of s&a clusters: " + sAnda);
		System.out.println("# of f&a clusters: " + fAnda);
		System.out.println("# of allTypes clusters: " + all);
		System.out.println("# of noTypes clusters: " + none);


	}
}
