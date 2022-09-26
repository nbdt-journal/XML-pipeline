import networkx as nx 

import node
from node import Node 
from element import Element 

from compound_subject_part_graph import compound_subject_part_node

''' Building a graph for Compound Subject ''' 
# Defining Elements
compound_subject = Element('compound-subject')
# Creating the Nodes
first_node = node.get_first_node()
last_node = node.get_last_node()
# Creating the graph
G_compound_subject = nx.DiGraph()
# adding the nodes
G_compound_subject.add_node(first_node)
G_compound_subject.add_node(compound_subject_part_node)
G_compound_subject.add_node(last_node)
# adding the edges
G_compound_subject.add_edge(first_node, compound_subject_part_node)
G_compound_subject.add_edge(compound_subject_part_node, compound_subject_part_node)
G_compound_subject.add_edge(compound_subject_part_node, last_node)
# making the node
compound_subject_node = Node(element=compound_subject, graph=G_compound_subject)

if __name__ == '__main__':
    import xml.etree.ElementTree as ET
    tree = ET.parse('test_samples/compound_subject.xml')
    root = tree.getroot()
    print(compound_subject_node.check(root))