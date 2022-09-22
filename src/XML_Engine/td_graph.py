import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Table Data Cell ''' 
# Defining Elements
td = Element('td')
# Creating the Nodes
td_node = Node(element=td, graph=node.get_leaf_graph())
