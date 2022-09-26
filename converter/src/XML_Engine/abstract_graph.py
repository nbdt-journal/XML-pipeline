import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for abstract ''' 
# Defining Elements
abstract = Element('abstract')
# Creating the Nodes
abstract_node = Node(element=abstract, graph=node.get_leaf_graph())