import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Table Footer ''' 
# Defining Elements
tfoot = Element('tfoot')
# Creating the Nodes
tfoot_node = Node(element=tfoot, graph=node.get_leaf_graph())
