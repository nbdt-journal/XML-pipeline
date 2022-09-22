import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Speaker ''' 
# Defining Elements
speaker = Element('speaker')
# Creating the Nodes
speaker_node = Node(element=speaker, graph=node.get_leaf_graph())
