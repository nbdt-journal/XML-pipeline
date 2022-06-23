import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Boxed Text ''' 
# Defining Elements
boxed_text = Element('boxed-text')
# Creating the Nodes
boxed_text_node = Node(element=boxed_text, graph=node.get_leaf_graph())
