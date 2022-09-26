import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for glyph-data ''' 
# Defining Elements
glyph_data = Element('glyph-data')
# Creating the Nodes
glyph_data_node = Node(element=glyph_data, graph=node.get_leaf_graph())