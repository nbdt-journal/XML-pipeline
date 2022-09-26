import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for page-count ''' 
# Defining Elements
page_count = Element('page-count')
# Creating the Nodes
page_count_node = Node(element=page_count, graph=node.get_leaf_graph())