import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Copyright Year ''' 
# Defining Elements
copyright_year = Element('copyright-year')
# Creating the Nodes
copyright_year_node = Node(element=copyright_year, graph=node.get_leaf_graph())
