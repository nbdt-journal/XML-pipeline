import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for support-source ''' 
# Defining Elements
support_source = Element('support-source')
# Creating the Nodes
support_source_node = Node(element=support_source, graph=node.get_leaf_graph())