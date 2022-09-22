import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Superscript ''' 
# Defining Elements
sup = Element('sup')
# Creating the Nodes
sup_node = Node(element=sup, graph=node.get_leaf_graph())
