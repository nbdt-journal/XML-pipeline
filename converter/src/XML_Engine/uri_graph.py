import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for uri ''' 
# Defining Elements
uri = Element('uri')
# Creating the Nodes
uri_node = Node(element=uri, graph=node.get_leaf_graph())