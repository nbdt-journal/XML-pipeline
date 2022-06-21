import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Contrib ''' 
# Defining Elements
contrib = Element('contrib')
# Creating the Nodes
contrib_node = Node(element=contrib, graph=node.get_leaf_graph())