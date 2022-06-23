import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Date ''' 
# Defining Elements
date = Element('date')
# Creating the Nodes
date_node = Node(element=date, graph=node.get_leaf_graph())
