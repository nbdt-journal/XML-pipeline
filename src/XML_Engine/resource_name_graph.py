import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for resource-name ''' 
# Defining Elements
resource_name = Element('resource-name')
# Creating the Nodes
resource_name_node = Node(element=resource_name, graph=node.get_leaf_graph())
