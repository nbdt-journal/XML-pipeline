import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for counts ''' 
# Defining Elements
counts = Element('counts')
# Creating the Nodes
counts_node = Node(element=counts, graph=node.get_leaf_graph())