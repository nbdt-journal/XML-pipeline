import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Label ''' 
# Defining Elements
label = Element('label')
# Creating the Nodes
label_node = Node(element=label, graph=node.get_leaf_graph())
