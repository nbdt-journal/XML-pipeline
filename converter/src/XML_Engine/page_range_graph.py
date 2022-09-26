import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for page-range ''' 
# Defining Elements
page_range = Element('page-range')
# Creating the Nodes
page_range_node = Node(element=page_range, graph=node.get_leaf_graph())