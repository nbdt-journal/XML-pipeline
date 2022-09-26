import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Meta Name ''' 
# Defining Elements
meta_name = Element('meta-name')
# Creating the Nodes
meta_name_node = Node(element=meta_name, graph=node.get_leaf_graph())