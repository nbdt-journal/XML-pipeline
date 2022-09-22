import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for name-alternatives ''' 
# Defining Elements
name_alternatives = Element('name-alternatives')
# Creating the Nodes
name_alternatives_node = Node(element=name_alternatives, graph=node.get_leaf_graph())