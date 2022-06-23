import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Element Citation ''' 
# Defining Elements
element_citation = Element('element-citation')
# Creating the Nodes
element_citation_node = Node(element=element_citation, graph=node.get_leaf_graph())
