import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Given (First) Names ''' 
# Defining Elements
given_names = Element('given-names')
# Creating the Nodes
given_names_node = Node(element=given_names, graph=node.get_leaf_graph())
