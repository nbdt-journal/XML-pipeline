import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for conf-data ''' 
# Defining Elements
conf_data = Element('conf-data')
# Creating the Nodes
conf_data_node = Node(element=conf_data, graph=node.get_leaf_graph())