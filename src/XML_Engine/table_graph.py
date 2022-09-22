import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for table ''' 
# Defining Elements
table = Element('table')
# Creating the Nodes
table_node = Node(element=table, graph=node.get_leaf_graph())
