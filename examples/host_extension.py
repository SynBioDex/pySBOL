# -*- coding: utf-8 -*-

"""
The following example script demonstrates pySBOL extension classes. PySBOL extensions allow users to create their own classes of data and serialize it into SBOL files as RDF/XML.

A Host is a ComponentDefinition that represents a cell. To indicate that the ComponentDefinition is a cell, as opposed to DNA, RNA, or other type of ComponentDefinition, the Gene Ontology term for cell is used as the value for the types field. 
The Genome, Plasmid, and Mutation classes are all ComponentDefinitions representing DNA molecules. They are initialized with the corresponding SequenceOntology term in the roles field. 

A Host may be defined using a taxonomic term that indicates its strain or species.  Its genotype may also be specified in terms of genetic nomenclature. The extract_marker method then converts each of these into a Marker object.
"""

from sbol import *
import re

# Define XML namespace for custom extension data. Namespaces should end in a delimiter such as / or #
EXTENSION_NAMESPACE = 'http://sys-bio.org#'

# Ontology terms
GENE_ONTOLOGY_CELL = 'http://purl.obolibrary.org/obo/GO_0005623'
NCBI_TAXONOMY = 'https://www.ncbi.nlm.nih.gov/Taxonomy/'

class Host(ComponentDefinition):

    def __init__(self, id = 'my_strain', plasmids = []):
        ComponentDefinition.__init__(self, SBOL_COMPONENT_DEFINITION, id, GENE_ONTOLOGY_CELL, '1.0.0')

        # Validate plasmid arguments
        for p in plasmids:
            if p.type != SBOL_COMPONENT_DEFINITION:
                raise SBOLError('Failed to instantiate host. An invalid plasmid component was specified.')

        # Initialize object properties
        self.taxonomy = URIProperty(self, EXTENSION_NAMESPACE + 'taxonomy', '0', '1')
        self.genotype = TextProperty(self, EXTENSION_NAMESPACE + 'genotype', '0', '1')
        self.genome = Genome(id + '_genome')
        self.origin = Origin(id + '_origin_of_replication')

        # Associate these objects with an SBOL Document for file I/O
        self.document = Document()
        self.document.addComponentDefinition(self)
        self.document.addComponentDefinition(self.genome)
        self.document.addComponentDefinition(self.origin)
        self.document.addComponentDefinition(plasmids)
        
        # Create an abstraction hierarchy
        self.assemble([Genome] + [Origin] + plasmids)

    def set_genotype(self, genotype):
        # Replace Unicode characters with Ascii
        self.genotype = re.sub(r'[^a-zA-Z0-9 ]', '_', genotype)

    def parse_genotype(self):
        markers = self.genotype.split(' ')
        markers = [ m for m in markers if m != ""]
        markers = list(set(markers))  # Remove duplicates
        markers = [ re.sub(r'[^a-zA-Z0-9 ]', '_', m) for m in markers ]  # Convert to alphanumeric and underscores
        return markers

    def extract_markers(self):
        markers = self.parse_genotype()
        marker_components = []
        for m in markers:
            marker_component = Marker(m)
            self.document.addComponentDefinition(marker_component)
            marker_components.append(marker_component)

        # Add markers to the base genome
        self.genome.assemble(marker_components) 

    def write(self, file_name):
        self.document.write(file_name)

class Genome(ComponentDefinition):
    def __init__(self, id = 'genome'):
        ComponentDefinition.__init__(self, SBOL_COMPONENT_DEFINITION, id, BIOPAX_DNA, '1.0.0')
        self.roles = SO + '0001026'  # Set 

class Origin(ComponentDefinition):
    def __init__(self, id = 'oriR'):
        ComponentDefinition.__init__(self, SBOL_COMPONENT_DEFINITION, id, BIOPAX_DNA, '1.0.0')
        self.roles = SO + '0000296'

class Plasmid(ComponentDefinition):
    def __init__(self, id = 'plasmid'):
        ComponentDefinition.__init__(self, SBOL_COMPONENT_DEFINITION, id, BIOPAX_DNA, '1.0.0')
        self.roles = SO + '0000155'

class Marker(ComponentDefinition):
    def __init__(self, id = 'test'):
        ComponentDefinition.__init__(self, SBOL_COMPONENT_DEFINITION, id, BIOPAX_DNA, '1.0.0')
        self.notes = TextProperty(self, EXTENSION_NAMESPACE + "note", '0', '*')

circuit = Plasmid('circuit')
host = Host('DH5alpha', [circuit])
host.taxonomy = NCBI_TAXONOMY + '668369'  # Taxonomic ID for DH5alpha strain
print host.taxonomy
host.set_genotype('F– endA1 glnV44 thi-1 recA1 relA1 gyrA96 deoR nupG purB20 φ80dlacZΔM15 Δ(lacZYA-argF)U169, hsdR17(rK–mK+), λ–')
host.extract_markers()
Config.setOption('validate', False)
host.write('DH5alpha.xml')
