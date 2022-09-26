import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for table-wrap ''' 
# Defining Elements
table_wrap = Element('table-wrap')
# Creating the Nodes
table_wrap_node = Node(element=table_wrap, graph=node.get_leaf_graph())
