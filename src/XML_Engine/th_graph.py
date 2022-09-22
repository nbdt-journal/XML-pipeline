import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Table Header Cell''' 
# Defining Elements
th = Element('th')
# Creating the Nodes
th_node = Node(element=th, graph=node.get_leaf_graph())
