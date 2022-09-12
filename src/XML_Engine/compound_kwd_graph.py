import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for compound-kwd ''' 
# Defining Elements
compound_kwd = Element('compound-kwd')
# Creating the Nodes
G_compound_kwd = nx.DiGraph()
first_node = node.get_first_node()
last_node = node.get_last_node()
G_compound_kwd.add_nodes_from([first_node,  last_node, compound_kwd_part_node])
G_compound_kwd.add_edge(first_node, compound_kwd_part_node)
G_compound_kwd.add_edge(compound_kwd_part_node, compound_kwd_part_node)
G_compound_kwd.add_edge(compound_kwd_part_node, last_node)