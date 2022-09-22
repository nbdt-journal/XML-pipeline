import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for sig-block ''' 
# Defining Elements
sig_block = Element('sig-block')
# Creating the Nodes
sig_block_node = Node(element=sig_block, graph=node.get_leaf_graph())
