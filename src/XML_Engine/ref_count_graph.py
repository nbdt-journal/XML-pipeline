import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for reference count ''' 
# Defining Elements
ref_count = Element('ref-count')
# Creating the Nodes
ref_count_node = Node(element=ref_count, graph=node.get_leaf_graph())
