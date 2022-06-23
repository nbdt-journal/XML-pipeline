import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Mixed Citation ''' 
# Defining Elements
mixed_citation = Element('mixed-citation')
# Creating the Nodes
mixed_citation_node = Node(element=mixed_citation, graph=node.get_leaf_graph())
