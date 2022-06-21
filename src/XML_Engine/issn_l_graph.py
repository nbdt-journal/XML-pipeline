import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Issn-l ''' 
# Defining Elements
issn_l = Element('issn-l')
# Creating the Nodes
issn_l_node = Node(element=issn_l, graph=node.get_leaf_graph())