import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for history ''' 
# Defining Elements
history = Element('history')
# Creating the Nodes
history_node = Node(element=history, graph=node.get_leaf_graph())