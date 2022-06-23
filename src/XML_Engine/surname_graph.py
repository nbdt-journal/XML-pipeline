import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Surname ''' 
# Defining Elements
surname = Element('surname')
# Creating the Nodes
surname_node = Node(element=surname, graph=node.get_leaf_graph())
