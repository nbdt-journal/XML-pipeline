import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for object-id ''' 
# Defining Elements
object_id = Element('object-id')
# Creating the Nodes
object_id_node = Node(element=object_id, graph=node.get_leaf_graph())