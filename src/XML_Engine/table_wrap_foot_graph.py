import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for table-wrap-foot ''' 
# Defining Elements
table_wrap_foot = Element('table-wrap-foot')
# Creating the Nodes
table_wrap_foot_node = Node(element=table_wrap_foot, graph=node.get_leaf_graph())
