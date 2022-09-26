import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Table Row ''' 
# Defining Elements
tr = Element('tr')
# Creating the Nodes
tr_node = Node(element=tr, graph=node.get_leaf_graph())
