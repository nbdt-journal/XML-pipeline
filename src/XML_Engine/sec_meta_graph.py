import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for sec-meta ''' 
# Defining Elements
sec_meta = Element('sec-meta')
# Creating the Nodes
sec_meta_node = Node(element=sec_meta, graph=node.get_leaf_graph())
