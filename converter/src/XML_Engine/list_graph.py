import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for List ''' 
# Defining Elements
list_element = Element('list')
# Creating the Nodes
list_element_node = Node(element=list_element, graph=node.get_leaf_graph())
