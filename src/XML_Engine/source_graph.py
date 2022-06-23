import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Source ''' 
# Defining Elements
source = Element('source')
# Creating the Nodes
source_node = Node(element=source, graph=node.get_leaf_graph())
