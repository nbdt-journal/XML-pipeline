import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for count ''' 
# Defining Elements
count = Element('count')
# Creating the Nodes
count_node = Node(element=count, graph=node.get_leaf_graph())