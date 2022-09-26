import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for table-count ''' 
# Defining Elements
table_count = Element('table-count')
# Creating the Nodes
table_count_node = Node(element=table_count, graph=node.get_leaf_graph())
