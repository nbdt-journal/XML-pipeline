import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for prefix ''' 
# Defining Elements
prefix = Element('prefix')
# Creating the Nodes
prefix_node = Node(element=prefix, graph=node.get_leaf_graph())
