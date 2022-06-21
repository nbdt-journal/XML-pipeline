import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Elocation-ID ''' 
# Defining Elements
elocation_id = Element('elocation_id')
# Creating the Nodes
elocation_id_node = Node(element=elocation_id, graph=node.get_leaf_graph())