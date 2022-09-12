import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for def-item ''' 
# Defining Elements
def_item = Element('def-item')
G_def_item = nx.DiGraph()
first_node = node.get_first_node()
last_node = node.get_last_node()
G_def_item.add_nodes_from([first_node, last_node, term_node, def_node])
G_def_item.add_edge(first_node, term_node)
G_def_item.add_edge(term_node, def_node)
G_def_item.add_edge(term_node, last_node)
G_def_item.add_edge(def_node, def_node)
G_def_item.add_edge(def_node, last_node)
# Creating the Nodes
def_item_node = Node(element=def_item, graph=G_def_item)