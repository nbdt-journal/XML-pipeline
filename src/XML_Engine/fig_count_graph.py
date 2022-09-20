import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for fig-count ''' 
# Defining Elements
fig_count = Element('fig-count')
# Creating the Nodes
fig_count_node = Node(element=fig_count, graph=node.get_leaf_graph())