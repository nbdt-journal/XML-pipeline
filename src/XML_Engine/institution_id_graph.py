import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for institution-id ''' 
# Defining Elements
institution_id = Element('institution-id')
# Creating the Nodes
institution_id_node = Node(element=institution_id, graph=node.get_leaf_graph())