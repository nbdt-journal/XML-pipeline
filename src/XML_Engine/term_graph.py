import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for term ''' 
# Defining Elements
term = Element('term')
# Creating the Nodes
term_node = Node(element=term, graph=node.get_leaf_graph())
