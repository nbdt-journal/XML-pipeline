import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Body ''' 
# Defining Elements
body = Element('body')
# Creating the Nodes
body_node = Node(element=body, graph=node.get_leaf_graph())
