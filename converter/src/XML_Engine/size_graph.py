import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for size ''' 
# Defining Elements
size = Element('size')
# Creating the Nodes
size_node = Node(element=size, graph=node.get_leaf_graph())
