import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for media ''' 
# Defining Elements
media = Element('media')
# Creating the Nodes
media_node = Node(element=media, graph=node.get_leaf_graph())