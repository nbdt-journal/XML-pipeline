import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for nested-kwd ''' 
# Defining Elements
nested_kwd = Element('nested-kwd')
# Creating the Nodes
nested_kwd_node = Node(element=nested_kwd, graph=node.get_leaf_graph())