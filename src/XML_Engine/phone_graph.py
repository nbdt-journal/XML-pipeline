import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for phone ''' 
# Defining Elements
phone = Element('phone')
# Creating the Nodes
phone_node = Node(element=phone, graph=node.get_leaf_graph())
