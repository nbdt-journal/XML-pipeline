import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for long-desc ''' 
# Defining Elements
long_desc = Element('long-desc')
# Creating the Nodes
long_desc_node = Node(element=long_desc, graph=node.get_leaf_graph())