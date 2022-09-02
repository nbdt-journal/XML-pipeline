import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for alt-text ''' 
# Defining Elements
alt_text = Element('alt-text')
alt_text_node = Node(element=alt_text, graph=node.get_leaf_graph())