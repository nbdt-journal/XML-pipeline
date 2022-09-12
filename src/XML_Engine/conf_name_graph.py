import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for conf-name ''' 
# Defining Elements
conf_name = Element('conf-name')
# Creating the Nodes
conf_name_node = Node(element=conf_name, graph=node.get_leaf_graph())