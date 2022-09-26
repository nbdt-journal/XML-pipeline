import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Reference List ''' 
# Defining Elements
ref_list = Element('ref-list')
# Creating the Nodes
ref_list_node = Node(element=ref_list, graph=node.get_leaf_graph())
