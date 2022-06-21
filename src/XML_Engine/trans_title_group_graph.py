import networkx as nx 

import node
from node import Node 
from element import Element 

from trans_title_graph import trans_title_node
from trans_subtitle_graph import trans_subtitle_node

''' Building a graph for Trans Title Group ''' 
# Defining Elements
trans_title_group = Element('trans-title-group')
# Defining the Graph
G_trans_title_group = nx.DiGraph()
# creating the first and last node
first_node = node.get_first_node()
last_node = node.get_last_node()
# adding the first node
G_trans_title_group.add_node(first_node)
# adding the elements
G_trans_title_group.add_node(trans_title_node)
G_trans_title_group.add_node(trans_subtitle_node)
# adding the last node
G_trans_title_group.add_node(last_node)
# adding the edges
G_trans_title_group.add_edge(first_node, trans_title_node)
G_trans_title_group.add_edge(trans_title_node, trans_subtitle_node)
G_trans_title_group.add_edge(trans_title_node, last_node)
G_trans_title_group.add_edge(trans_subtitle_node, trans_subtitle_node)
G_trans_title_group.add_edge(trans_subtitle_node, last_node)
# Defining the trans-title-group node
trans_title_group_node = Node(element=trans_title_group, graph=G_trans_title_group)

if __name__ == '__main__':
    import xml.etree.ElementTree as ET
    tree = ET.parse('test_samples/trans_title_group.xml')
    root = tree.getroot()
    print(trans_title_group_node.check(root))