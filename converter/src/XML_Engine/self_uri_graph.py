import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Self URI ''' 
# Defining Elements
self_uri = Element('self-uri')
# Creating the Nodes
self_uri_node = Node(element=self_uri, graph=node.get_leaf_graph())