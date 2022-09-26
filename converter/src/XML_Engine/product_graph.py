import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for product ''' 
# Defining Elements
product = Element('product')
# Creating the Nodes
product_node = Node(element=product, graph=node.get_leaf_graph())