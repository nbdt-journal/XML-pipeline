import networkx as nx 

import node
from node import Node 
from element import Element 

from custom_meta_group_graph import custom_meta_group_node
from restricted_by_graph import restricted_by_node
from extended_by_graph import extended_by_node

''' Building a graph for Procesing Metadata '''
# Defining Elements
processing_meta = Element('processing-meta')
# Defining the Graph
G_processing_meta = nx.DiGraph()
# creating the first and last node
first_node = node.get_first_node()
last_node = node.get_last_node()
# adding the first node
G_processing_meta.add_node(first_node)
# adding the elements
G_processing_meta.add_node(restricted_by_node)
G_processing_meta.add_node(extended_by_node)
G_processing_meta.add_node(custom_meta_group_node)
# adding the last node 
G_processing_meta.add_node(last_node)
# adding the edges
G_processing_meta.add_edge(first_node, restricted_by_node)
G_processing_meta.add_edge(first_node, extended_by_node)
G_processing_meta.add_edge(first_node, custom_meta_group_node)
G_processing_meta.add_edge(first_node, last_node)
G_processing_meta.add_edge(restricted_by_node, restricted_by_node)
G_processing_meta.add_edge(restricted_by_node, extended_by_node)
G_processing_meta.add_edge(restricted_by_node, custom_meta_group_node)
G_processing_meta.add_edge(restricted_by_node, last_node)
G_processing_meta.add_edge(extended_by_node, extended_by_node)
G_processing_meta.add_edge(extended_by_node, custom_meta_group_node)
G_processing_meta.add_edge(extended_by_node, last_node)
G_processing_meta.add_edge(custom_meta_group_node, custom_meta_group_node)
G_processing_meta.add_edge(custom_meta_group_node, last_node)
# Defining the processing-meta node
processing_meta_node = Node(element=processing_meta, graph=G_processing_meta)

if __name__ == '__main__':
    import xml.etree.ElementTree as ET
    tree = ET.parse('test_samples/processing_meta.xml')
    root = tree.getroot()
    print(processing_meta_node.check(root))