import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for open-access ''' 
# Defining Elements
open_access = Element('open-access')
# Creating the Nodes
open_access_node = Node(element=open_access, graph=node.get_leaf_graph())