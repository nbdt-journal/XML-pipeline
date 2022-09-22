import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for trans-source ''' 
# Defining Elements
trans_source = Element('trans-source')
# Creating the Nodes
trans_source_node = Node(element=trans_source, graph=node.get_leaf_graph())