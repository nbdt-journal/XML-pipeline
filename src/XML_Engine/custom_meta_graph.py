import networkx as nx 

import node
from node import Node 
from element import Element 

from meta_name_graph import meta_name_node
from meta_value_graph import meta_value_node

''' Building a graph for Custom Meta ''' 
# Defining Elements
custom_meta = Element('custom-meta')
# Defining the graph 
G_custom_meta = nx.DiGraph()
# creating the first and last node
first_node = node.get_first_node()
last_node = node.get_last_node()
# adding the first-node
G_custom_meta.add_node(first_node)
# adding the element nodes
G_custom_meta.add_node(meta_name_node)
G_custom_meta.add_node(meta_value_node)
# adding the last node
G_custom_meta.add_node(last_node)
# adding the edges
G_custom_meta.add_edge(first_node, meta_name_node)
G_custom_meta.add_edge(meta_name_node, meta_value_node)
G_custom_meta.add_edge(meta_value_node, last_node)
# defining the custom-meta node
custom_meta_node = Node(element=custom_meta, graph=G_custom_meta)

if __name__ == '__main__':
    import xml.etree.ElementTree as ET
    tree = ET.parse('test_samples/custom_meta.xml')
    root = tree.getroot()
    print(custom_meta_node.check(root))