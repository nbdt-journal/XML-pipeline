import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for string-name ''' 
# Defining Elements
string_name = Element('string-name')
# Creating the Nodes
string_name_node = Node(element=string_name, graph=node.get_leaf_graph())
