import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Aff ''' 
# Defining Elements
aff = Element('aff')
# Creating the Nodes
aff_node = Node(element=aff, graph=node.get_leaf_graph())