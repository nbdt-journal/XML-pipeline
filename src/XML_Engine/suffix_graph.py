import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Suffix ''' 
# Defining Elements
suffix = Element('suffix')
# Creating the Nodes
suffix_node = Node(element=suffix, graph=node.get_leaf_graph())
