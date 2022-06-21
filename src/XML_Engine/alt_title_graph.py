import networkx as nx 

import node
from node import Node 
from element import Element 



''' Building a graph for Alt Title ''' 
# Defining Elements
alt_title = Element('alt-title')
# Creating the Nodes
alt_title_node = Node(element=alt_title, graph=node.get_leaf_graph())