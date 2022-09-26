import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for X ''' 
# Defining Elements
x = Element('x')
# Creating the Nodes
x_node = Node(element=x, graph=node.get_leaf_graph())