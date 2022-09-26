import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Issue ''' 
# Defining Elements
issue = Element('issue')
# Creating the Nodes
issue_node = Node(element=issue, graph=node.get_leaf_graph())