import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for etal ''' 
# Defining Elements
etal = Element('etal')
# Creating the Nodes
etal_node = Node(element=etal, graph=node.get_leaf_graph())