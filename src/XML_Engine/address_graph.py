import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Address ''' 
# Defining Elements
address = Element('address')
# Creating the Nodes
address_node = Node(element=address, graph=node.get_leaf_graph())