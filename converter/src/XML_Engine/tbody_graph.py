import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Table body ''' 
# Defining Elements
tbody = Element('tbody')
# Creating the Nodes
tbody_node = Node(element=tbody, graph=node.get_leaf_graph())
