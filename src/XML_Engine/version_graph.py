import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for version ''' 
# Defining Elements
version = Element('version')
# Creating the Nodes
version_node = Node(element=version, graph=node.get_leaf_graph())