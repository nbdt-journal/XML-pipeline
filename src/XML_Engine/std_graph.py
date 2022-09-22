import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Standard, Cited ''' 
# Defining Elements
std = Element('std')
# Creating the Nodes
std_node = Node(element=std, graph=node.get_leaf_graph())
