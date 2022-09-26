import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for country ''' 
# Defining Elements
country = Element('country')
# Creating the Nodes
country_node = Node(element=country, graph=node.get_leaf_graph())