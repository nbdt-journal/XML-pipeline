import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Name ''' 
# Defining Elements
name = Element('name')
# Creating the Nodes
name_node = Node(element=name, graph=node.get_leaf_graph())
