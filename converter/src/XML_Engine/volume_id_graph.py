import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Volume ''' 
# Defining Elements
volume_id = Element('volume-id')
# Creating the Nodes
volume_id_node = Node(element=volume_id, graph=node.get_leaf_graph())