import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for col ''' 
# Defining Elements
col = Element('col')
# Creating the Nodes
col_node = Node(element=col, graph=node.get_leaf_graph())
