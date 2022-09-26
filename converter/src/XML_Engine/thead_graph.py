import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Table Header ''' 
# Defining Elements
thead = Element('thead')
# Creating the Nodes
thead_node = Node(element=thead, graph=node.get_leaf_graph())
