import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for title ''' 
# Defining Elements
title = Element('title')
# Creating the Nodes
title_node = Node(element=title, graph=node.get_leaf_graph())