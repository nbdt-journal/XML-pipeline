import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for index-term-range-end ''' 
# Defining Elements
index_term_range_end = Element('index-term-range-end')
# Creating the Nodes
index_term_range_end_node = Node(element=index_term_range_end, graph=node.get_leaf_graph())