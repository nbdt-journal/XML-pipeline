import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Subject ''' 
# Defining Elements
subject = Element('subject')
# Creating the Nodes
subject_node = Node(element=subject, graph=node.get_leaf_graph())