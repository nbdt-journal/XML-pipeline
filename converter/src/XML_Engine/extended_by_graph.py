import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for extended-by ''' 
# Defining Elements
extended_by = Element('extended-by')
# Creating the Nodes
extended_by_node = Node(element=extended_by, graph=node.get_leaf_graph())