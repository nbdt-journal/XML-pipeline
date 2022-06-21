import networkx as nx 

import node
from node import Node 
from element import Element 

from custom_meta_graph import custom_meta_node 

''' Building a graph for Custom Meta Group ''' 
# Defining Elements
custom_meta_group = Element('custom-meta-group')
# Defining the Graph 
G_custom_meta_group = nx.DiGraph()
# creating the first and last node 
first_node = node.get_first_node()
last_node = node.get_last_node()
# adding the first node
G_custom_meta_group.add_node(first_node)
# adding the elements
G_custom_meta_group.add_node(custom_meta_node)
# adding the last node
G_custom_meta_group.add_node(last_node)
# adding the edges
G_custom_meta_group.add_edge(first_node, custom_meta_node)
G_custom_meta_group.add_edge(custom_meta_node, custom_meta_node)
G_custom_meta_group.add_edge(custom_meta_node, last_node)
# Defining the custom-meta-group node
custom_meta_group_node = Node(element=custom_meta_group, graph=G_custom_meta_group)
    
if __name__ == '__main__':
    import xml.etree.ElementTree as ET
    tree = ET.parse('test_samples/custom_meta_group.xml')
    root = tree.getroot()
    print(custom_meta_group_node.check(root))