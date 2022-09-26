import networkx as nx 

import node
from node import Node 
from element import Element 

from aff_graph import aff_node

''' Building a graph for Aff Alternatives ''' 
# Defining Elements
aff_alternatives = Element('aff-alternatives')
# Creating the Nodes
G_aff_alternatives = nx.DiGraph()
first_node = node.get_first_node()
last_node = node.get_last_node()
# adding the nodes
G_aff_alternatives.add_node(first_node)
G_aff_alternatives.add_node(aff_node)
G_aff_alternatives.add_node(last_node)
# adding the edges
G_aff_alternatives.add_edge(first_node, aff_node)
G_aff_alternatives.add_edge(aff_node, aff_node)
G_aff_alternatives.add_edge(aff_node, last_node)
# Defining the node
aff_alternatives_node = Node(element=aff_alternatives, graph=G_aff_alternatives)