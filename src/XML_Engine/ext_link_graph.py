import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for ext-link ''' 
# Defining Elements
ext_link = Element('ext-link')
# Creating the Nodes
ext_link_node = Node(element=ext_link, graph=node.get_leaf_graph())