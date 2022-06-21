import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for lpage ''' 
# Defining Elements
lpage = Element('lpage')
# Creating the Nodes
lpage_node = Node(element=lpage, graph=node.get_leaf_graph())