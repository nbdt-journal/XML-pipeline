import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Copyright Holder ''' 
# Defining Elements
copyright_holder = Element('copyright-holder')
# Creating the Nodes
copyright_holder_node = Node(element=copyright_holder, graph=node.get_leaf_graph())
