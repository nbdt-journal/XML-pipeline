import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for string-date ''' 
# Defining Elements
string_date = Element('string-date')
# Creating the Nodes
string_date_node = Node(element=string_date, graph=node.get_leaf_graph())
