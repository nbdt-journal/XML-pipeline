import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for fpage ''' 
# Defining Elements
fpage = Element('fpage')
# Creating the Nodes
fpage_node = Node(element=fpage, graph=node.get_leaf_graph())