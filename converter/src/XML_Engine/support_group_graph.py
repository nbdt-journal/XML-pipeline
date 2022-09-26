import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for support-group ''' 
# Defining Elements
support_group = Element('support-group')
# Creating the Nodes
support_group_node = Node(element=support_group, graph=node.get_leaf_graph())