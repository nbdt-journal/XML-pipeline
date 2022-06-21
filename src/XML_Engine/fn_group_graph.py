import networkx as nx 

import node
from node import Node 
from element import Element 

from fn_graph import fn_node 
from x_graph import x_node 

''' Building a graph for FN-Group ''' 
# Defining Elements
fn_group = Element('fn-group')
# Creating the Graph
G_fn_group = nx.DiGraph()
fn_group_node = Node(element=fn_group, graph=G_fn_group)
# adding the nodes
first_node = node.get_first_node()
last_node = node.get_last_node()
G_fn_group.add_node(first_node)
G_fn_group.add_node(fn_node)
G_fn_group.add_node(x_node)
G_fn_group.add_node(last_node)
# adding the edges
G_fn_group.add_edge(first_node, fn_node)
G_fn_group.add_edge(first_node, x_node)
G_fn_group.add_edge(fn_node, fn_node)
G_fn_group.add_edge(fn_node, x_node)
G_fn_group.add_edge(x_node, fn_node)
G_fn_group.add_edge(x_node, x_node)
G_fn_group.add_edge(fn_node, last_node)
G_fn_group.add_edge(x_node, last_node)

if __name__ == '__main__':
    import xml.etree.ElementTree as ET
    tree = ET.parse('test_samples/fn_group.xml')
    root = tree.getroot()
    print(fn_group_node.check(root))