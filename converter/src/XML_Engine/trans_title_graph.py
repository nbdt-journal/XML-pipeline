import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Trans Title ''' 
# Defining Elements
trans_title = Element('trans-title')
# Creating the Nodes
trans_title_node = Node(element=trans_title, graph=node.get_leaf_graph())
