import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Volume ''' 
# Defining Elements
volume = Element('volume')
# Creating the Nodes
volume_node = Node(element=volume, graph=node.get_leaf_graph())