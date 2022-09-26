import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for license ''' 
# Defining Elements
license_ = Element('license')
# Creating the Nodes
license_node = Node(element=license_, graph=node.get_leaf_graph())