import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Access-Date ''' 
# Defining Elements
access_date = Element('access-date')
# Creating the Nodes
access_date_node = Node(element=access_date, graph=node.get_leaf_graph())
