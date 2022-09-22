import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for term-head ''' 
# Defining Elements
term_head = Element('term-head')
# Creating the Nodes
term_head_node = Node(element=term_head, graph=node.get_leaf_graph())
