import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for option ''' 
# Defining Elements
option = Element('option')
# Creating the Nodes
option_node = Node(element=option, graph=node.get_leaf_graph())