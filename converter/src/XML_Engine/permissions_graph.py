import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for permissions ''' 
# Defining Elements
permissions = Element('permissions')
# Creating the Nodes
permissions_node = Node(element=permissions, graph=node.get_leaf_graph())