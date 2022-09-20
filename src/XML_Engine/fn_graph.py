import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for FN ''' 
# Defining Elements
fn = Element('fn')
# Creating the Nodes
G_fn = nx.DiGraph()
first_node = node.get_first_node()
last_node = node.get_last_node()
G_fn.add_nodes_from([first_node, last_node, label_node, p_node])
G_fn.add_edge(first_node, label_node)
G_fn.add_edge(first_node, p_node)
G_fn.add_edge(label_node, p_node)
G_fn.add_edge(p_node, p_node)
G_fn.add_edge(p_node, last_node)

fn_node = Node(element=fn, graph=G_fn)