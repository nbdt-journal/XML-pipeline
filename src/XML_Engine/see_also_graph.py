import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for see-also ''' 
# Defining Elements
see_also = Element('see-also')
# Creating the Nodes
see_also_node = Node(element=see_also, graph=node.get_leaf_graph())
