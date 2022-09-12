import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for colgroup ''' 
# Defining Elements
col_group = Element('colgroup')
# Creating the Nodes
G_col_group = nx.DiGraph()
col_group_node = Node(element=col_group, graph=G_col_group)

first_node = node.get_first_node()
last_node = node.get_last_node()

G_col_group.add_edge(first_node, last_node)
G_col_group.add_edge(first_node, col_node)
G_col_group.add_edge(col_node, col_node)
G_col_group.add_edge(col_node, last_node)