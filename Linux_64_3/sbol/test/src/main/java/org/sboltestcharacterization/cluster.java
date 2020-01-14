package org.sboltestcharacterization;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class cluster {


	private int cluster_name;
	private List<cluster> connections;
	private Set<String> data_types;
	private HashSet<String> files;
	private boolean isSource; 
	
	public cluster(int _id, Set<String> _data, HashSet<String> file_list) {
		cluster_name = _id;
		connections = new ArrayList<cluster>(); 
		data_types = _data;
		files = file_list;
		isSource = false; 
	}
	
	public boolean get_source()
	{
		
		return this.isSource; 
	}
	
	public void set_source(boolean _isSource)
	{
		this.isSource = _isSource; 
	}

	public int get_cluster_id() {
		return this.cluster_name;
	}

	public Set<String> get_data_types() {
		return data_types;
	}

	public Set<String> get_files() {
		return files;
	}
	
	public List<cluster> get_connections() {
		return this.connections;
	}
	
	public void add_connections (cluster _connection)
	{
		this.connections.add(_connection); 
	}
	
	public void set_connections (ArrayList<cluster> _connections)
	{
		this.connections = _connections; 
	}


}
