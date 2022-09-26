import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Volume ''' 
# Defining Elements
volume_series = Element('volume-series')
# Creating the Nodes
volume_series_node = Node(element=volume_series, graph=node.get_leaf_graph())