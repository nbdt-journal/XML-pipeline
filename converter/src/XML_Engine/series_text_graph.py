import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Series Text ''' 
# Defining Elements
series_text = Element('series-text')
# Creating the Nodes
series_text_node = Node(element=series_text, graph=node.get_leaf_graph())