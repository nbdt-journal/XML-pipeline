import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for target ''' 
# Defining Elements
target = Element('target')
# Creating the Nodes
target_node = Node(element=target, graph=node.get_leaf_graph())
