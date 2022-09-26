import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for response ''' 
# Defining Elements
response = Element('response')
# Creating the Nodes
response_node = Node(element=response, graph=node.get_leaf_graph())
