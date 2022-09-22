import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Subscript ''' 
# Defining Elements
sub = Element('sub')
# Creating the Nodes
sub_node = Node(element=sub, graph=node.get_leaf_graph())
