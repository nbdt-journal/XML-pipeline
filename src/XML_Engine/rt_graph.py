import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for rt ''' 
# Defining Elements
rt = Element('rt')
# Creating the Nodes
rt_node = Node(element=rt, graph=node.get_leaf_graph())
