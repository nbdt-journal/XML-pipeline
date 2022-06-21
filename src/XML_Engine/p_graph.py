import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for p ''' 
# Defining Elements
p = Element('p')
# Creating the Nodes
p_node = Node(element=p, graph=node.get_leaf_graph())