import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for table-wrap-group ''' 
# Defining Elements
table_wrap_group = Element('table-wrap-group')
# Creating the Nodes
table_wrap_group_node = Node(element=table_wrap_group, graph=node.get_leaf_graph())
