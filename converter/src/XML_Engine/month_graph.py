import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Month ''' 
# Defining Elements
month = Element('month')
# Creating the Nodes
month_node = Node(element=month, graph=node.get_leaf_graph())
