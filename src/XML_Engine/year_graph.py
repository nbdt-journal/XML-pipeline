import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Year ''' 
# Defining Elements
year = Element('year')
# Creating the Nodes
year_node = Node(element=year, graph=node.get_leaf_graph())
