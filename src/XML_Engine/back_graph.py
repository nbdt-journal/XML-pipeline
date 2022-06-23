import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Back ''' 
# Defining Elements
back = Element('back')
# Creating the Nodes
back_node = Node(element=back, graph=node.get_leaf_graph())
