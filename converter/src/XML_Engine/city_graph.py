import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for city ''' 
# Defining Elements
city = Element('city')
# Creating the Nodes
city_node = Node(element=city, graph=node.get_leaf_graph())
