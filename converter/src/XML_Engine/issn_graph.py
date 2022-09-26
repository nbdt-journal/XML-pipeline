import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Issn ''' 
# Defining Elements
issn = Element('issn')
# Creating the Nodes
issn_node = Node(element=issn, graph=node.get_leaf_graph())