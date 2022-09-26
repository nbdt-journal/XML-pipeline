import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for history ''' 
# Defining Elements
history = Element('history')

G_history = nx.DiGraph()
first_node = node.get_first_node()
last_node = node.get_last_node()
G_history.add_nodes_from([first_node, last_node, date_node])
G_history.add_edge(first_node, date_node)
G_history.add_edge(date_node, date_node)
G_history.add_edge(date_node, last_node)
# Creating the Nodes
history_node = Node(element=history, graph=G_history)