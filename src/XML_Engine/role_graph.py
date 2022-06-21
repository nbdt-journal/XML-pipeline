import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Role ''' 
# Defining Elements
role = Element('role')
# Creating the Nodes
role_node = Node(element=role, graph=node.get_leaf_graph())