import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for thead ''' 
# Defining Elements
thead = Element('thead')
G_thead = nx.DiGraph()
first_node = node.get_first_node()
last_node = node.get_last_node()
G_thead.add_nodes_from([first_node, last_node, tr_node])
G_thead.add_edge(first_node, tr_node)
G_thead.add_edge(tr_node, tr_node)
G_thead.add_edge(tr_node, last_node)
# Creating the Nodes
thead_node = Node(element=thead, graph=G_thead)
