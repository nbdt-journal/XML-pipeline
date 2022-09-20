import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for glyph-ref ''' 
# Defining Elements
glyph_ref = Element('glyph-ref')
# Creating the Nodes
glyph_ref_node = Node(element=glyph_ref, graph=node.get_leaf_graph())