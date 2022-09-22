import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Signature ''' 
# Defining Elements
sig = Element('sig')
# Creating the Nodes
sig_node = Node(element=sig, graph=node.get_leaf_graph())
