import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for postal-code ''' 
# Defining Elements
postal_code = Element('postal-code')
# Creating the Nodes
postal_code_node = Node(element=postal_code, graph=node.get_leaf_graph())
