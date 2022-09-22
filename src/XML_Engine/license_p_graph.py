import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for license-p ''' 
# Defining Elements
license_p = Element('license-p')
# Creating the Nodes
license_p_node = Node(element=license_p, graph=node.get_leaf_graph())