import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for kwd-group ''' 
# Defining Elements
kwd_group = Element('kwd-group')
# Creating the Nodes
kwd_group_node = Node(element=kwd_group, graph=node.get_leaf_graph())