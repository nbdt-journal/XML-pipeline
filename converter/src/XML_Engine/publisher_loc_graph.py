import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Published Loc ''' 
# Defining Elements
publisher_loc = Element('publisher-loc')
# Creating the Nodes
publisher_loc_node = Node(element=publisher_loc, graph=node.get_leaf_graph())