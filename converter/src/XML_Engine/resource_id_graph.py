import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for resource-id ''' 
# Defining Elements
resource_id = Element('resource-id')
# Creating the Nodes
resource_id_node = Node(element=resource_id, graph=node.get_leaf_graph())
