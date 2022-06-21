import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Trans Subtitle ''' 
# Defining Elements
trans_subtitle = Element('trans-subtitle')
# Creating the Nodes
trans_subtitle_node = Node(element=trans_subtitle, graph=node.get_leaf_graph())
