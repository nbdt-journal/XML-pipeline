import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Section ''' 
# Defining Elements
sec = Element('sec')
# Creating the Nodes
sec_node = Node(element=sec, graph=node.get_leaf_graph())
