import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for explanation ''' 
# Defining Elements
explanation = Element('explanation')
# Creating the Nodes
explanation_node = Node(element=explanation, graph=node.get_leaf_graph())