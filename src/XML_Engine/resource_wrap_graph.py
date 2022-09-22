import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for resource-wrap ''' 
# Defining Elements
resource_wrap = Element('resource-wrap')
# Creating the Nodes
resource_wrap_node = Node(element=resource_wrap, graph=node.get_leaf_graph())
