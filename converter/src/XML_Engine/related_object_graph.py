import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for related-object ''' 
# Defining Elements
related_object = Element('related-object')
# Creating the Nodes
related_object_node = Node(element=related_object, graph=node.get_leaf_graph())