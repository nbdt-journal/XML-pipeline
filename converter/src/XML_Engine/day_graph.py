import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Day ''' 
# Defining Elements
day = Element('day')
# Creating the Nodes
day_node = Node(element=day, graph=node.get_leaf_graph())
