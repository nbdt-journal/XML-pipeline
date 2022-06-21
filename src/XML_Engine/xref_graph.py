import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for xref ''' 
# Defining Elements
xref = Element('xref')
# Creating the Nodes
xref_node = Node(element=xref, graph=node.get_leaf_graph())