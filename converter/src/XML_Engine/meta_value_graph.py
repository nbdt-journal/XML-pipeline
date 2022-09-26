import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Meta Value ''' 
# Defining Elements
meta_value = Element('meta-value')
# Creating the Nodes
meta_value_node = Node(element=meta_value, graph=node.get_leaf_graph())