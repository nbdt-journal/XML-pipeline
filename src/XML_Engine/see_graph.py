import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for see ''' 
# Defining Elements
see = Element('see')
# Creating the Nodes
see_node = Node(element=see, graph=node.get_leaf_graph())
