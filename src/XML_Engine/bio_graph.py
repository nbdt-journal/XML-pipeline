import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for bio ''' 
# Defining Elements
bio = Element('bio')
# Creating the Nodes
bio_node = Node(element=bio, graph=node.get_leaf_graph())