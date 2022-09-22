import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for verse-line ''' 
# Defining Elements
verse_line = Element('verse-line')
# Creating the Nodes
verse_line_node = Node(element=verse_line, graph=node.get_leaf_graph())