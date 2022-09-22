import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for tr ''' 
# Defining Elements
tr = Element('tr')
G_tr = nx.DiGraph()
first_node = node.get_first_node()
last_node = node.get_last_node()
G_tr.add_nodes_from([first_node, last_node, th_node, td_node])
G_tr.add_edge(first_node, th_node)
G_tr.add_edge(first_node, td_node)
G_tr.add_edge(th_node, th_node)
G_tr.add_edge(th_node, td_node)
G_tr.add_edge(th_node, last)
G_tr.add_edge(td_node, th_node)
G_tr.add_edge(td_node, td_node)
G_tr.add_edge(td_node, last)
# Creating the Nodes
tr_node = Node(element=tr, graph=G_tr)