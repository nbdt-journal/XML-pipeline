import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Supplement ''' 
# Defining Elements
supplement = Element('supplement')
# Creating the Nodes
supplement_node = Node(element=supplement, graph=node.get_leaf_graph())