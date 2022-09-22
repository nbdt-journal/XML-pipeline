import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for support-description ''' 
# Defining Elements
support_description = Element('support-description')
# Creating the Nodes
support_description_node = Node(element=support_description, graph=node.get_leaf_graph())
