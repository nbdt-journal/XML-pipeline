import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Series Title ''' 
# Defining Elements
series_title = Element('series-title')
# Creating the Nodes
series_title_node = Node(element=series_title, graph=node.get_leaf_graph())