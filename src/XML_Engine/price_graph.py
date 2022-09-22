import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for price ''' 
# Defining Elements
price = Element('price')
# Creating the Nodes
price_node = Node(element=price, graph=node.get_leaf_graph())
