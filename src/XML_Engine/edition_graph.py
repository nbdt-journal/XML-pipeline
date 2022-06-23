import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Edition ''' 
# Defining Elements
edition = Element('edition')
# Creating the Nodes
edition_node = Node(element=edition, graph=node.get_leaf_graph())
