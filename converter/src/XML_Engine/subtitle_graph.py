import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Subtitle ''' 
# Defining Elements
subtitle = Element('subtitle')
# Creating the Nodes
subtitle_node = Node(element=subtitle, graph=node.get_leaf_graph())