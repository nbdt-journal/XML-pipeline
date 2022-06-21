import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for restricted-by ''' 
# Defining Elements
restricted_by = Element('restricted-by')
# Creating the Nodes
restricted_by_node = Node(element=restricted_by, graph=node.get_leaf_graph())