import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for principal-investigator ''' 
# Defining Elements
principal_investigator = Element('principal-investigator')
# Creating the Nodes
principal_investigator_node = Node(element=principal_investigator, graph=node.get_leaf_graph())
