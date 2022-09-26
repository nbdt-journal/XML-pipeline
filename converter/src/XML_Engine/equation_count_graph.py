import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for equation-count ''' 
# Defining Elements
equation_count = Element('equation-count')
# Creating the Nodes
equation_count_node = Node(element=equation_count, graph=node.get_leaf_graph())