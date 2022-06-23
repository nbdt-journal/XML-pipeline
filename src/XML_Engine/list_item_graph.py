import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for List Item ''' 
# Defining Elements
list_item = Element('list-item')
# Creating the Nodes
list_item_node = Node(element=list_item, graph=node.get_leaf_graph())
