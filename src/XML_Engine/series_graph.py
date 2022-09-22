import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for series ''' 
# Defining Elements
series = Element('series')
# Creating the Nodes
series_node = Node(element=series, graph=node.get_leaf_graph())
