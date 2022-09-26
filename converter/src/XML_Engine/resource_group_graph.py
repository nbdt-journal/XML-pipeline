import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for resource-group ''' 
# Defining Elements
resource_group = Element('resource-group')
# Creating the Nodes
resource_group_node = Node(element=resource_group, graph=node.get_leaf_graph())
