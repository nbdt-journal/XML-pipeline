import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Published Name ''' 
# Defining Elements
publisher_name = Element('publisher-name')
# Creating the Nodes
publisher_name_node = Node(element=publisher_name, graph=node.get_leaf_graph())