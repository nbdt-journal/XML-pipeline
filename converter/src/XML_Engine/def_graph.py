import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for def ''' 
# Defining Elements
_def = Element('def')
G_def = nx.DiGraph()
first_node = node.get_first_node()
last_node = node.get_last_node()
G_def.add_nodes_from([first_node, last_node, p_node])
G_def.add_edge(first_node, p_node)
G_def.add_edge(p_node, p_node)
G_def.add_edge(p_node, last_node)
# Creating the Nodes
def_node = Node(element=_def, graph=G_def)