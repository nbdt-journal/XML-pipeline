import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for keyword ''' 
# Defining Elements
kwd = Element('kwd')
# Creating the Nodes
kwd_node = Node(element=kwd, graph=node.get_leaf_graph())