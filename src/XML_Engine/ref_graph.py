import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Reference ''' 
# Defining Elements
ref = Element('ref')
# Creating the Nodes
ref_node = Node(element=ref, graph=node.get_leaf_graph())
