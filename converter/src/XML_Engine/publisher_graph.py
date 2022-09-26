import networkx as nx 

import node
from node import Node 
from element import Element 

from publisher_name_graph import publisher_name_node 
from publisher_loc_graph import publisher_loc_node

''' Building a graph for Publisher ''' 
# Defining Elements
publisher = Element('publisher')
# Creating the graph
G_publisher_node = nx.DiGraph()
# Creting the first and last node
first_node = node.get_first_node()
last_node = node.get_last_node()
# adding the nodes
G_publisher_node.add_node(first_node)
G_publisher_node.add_node(publisher_name_node)
G_publisher_node.add_node(publisher_loc_node)
# adding the edges
G_publisher_node.add_edge(first_node, publisher_name_node)
G_publisher_node.add_edge(publisher_name_node, publisher_name_node)
G_publisher_node.add_edge(publisher_name_node, publisher_loc_node)
G_publisher_node.add_edge(publisher_name_node, last_node)
G_publisher_node.add_edge(publisher_loc_node, publisher_name_node)
G_publisher_node.add_edge(publisher_loc_node, last_node)
# defining the publisher node
publisher_node = Node(element=publisher, graph=G_publisher_node)

if __name__ == '__main__':
    import xml.etree.ElementTree as ET
    tree = ET.parse('test_samples/publisher.xml')
    root = tree.getroot()
    print(publisher_node.check(root))