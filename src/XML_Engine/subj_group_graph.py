import networkx as nx 

import node
from node import Node 
from element import Element 

from subject_graph import subject_node
from compound_subject_graph import compound_subject_node

''' Building a graph for Subj-Group ''' 
# Defining Elements
subj_group = Element('subj-group')
# Creating the Nodes
first_node = node.get_first_node()
last_node = node.get_last_node()
# Creating the graph
G_subj_group = nx.DiGraph()
subj_group_node = Node(element=subj_group, graph=G_subj_group)
# adding the nodes
G_subj_group.add_node(first_node)
G_subj_group.add_node(subject_node)
G_subj_group.add_node(compound_subject_node)
G_subj_group.add_node(last_node)
# adding the edges
G_subj_group.add_edge(first_node, subject_node)
G_subj_group.add_edge(first_node, compound_subject_node)
G_subj_group.add_edge(subject_node, subject_node)
G_subj_group.add_edge(subject_node, compound_subject_node)
G_subj_group.add_edge(compound_subject_node, subject_node)
G_subj_group.add_edge(compound_subject_node, compound_subject_node)
G_subj_group.add_edge(subject_node, last_node)
G_subj_group.add_edge(compound_subject_node, last_node)
G_subj_group.add_edge(subject_node, subj_group_node)
G_subj_group.add_edge(compound_subject_node, subj_group_node)
G_subj_group.add_edge(subj_group_node, subj_group_node)
G_subj_group.add_edge(subj_group_node, last_node)

if __name__ == '__main__':
    import xml.etree.ElementTree as ET
    tree = ET.parse('test_samples/subj_group.xml')
    root = tree.getroot()
    print(subj_group_node.check(root))

