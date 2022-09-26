import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for on-behalf-of ''' 
# Defining Elements
on_behalf_of = Element('on-behalf-of')
# Creating the Nodes
on_behalf_of_node = Node(element=on_behalf_of, graph=node.get_leaf_graph())