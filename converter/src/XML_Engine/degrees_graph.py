import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for degrees ''' 
# Defining Elements
degrees = Element('degrees')
# Creating the Nodes
degrees_node = Node(element=degrees, graph=node.get_leaf_graph())
