import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Issue Title ''' 
# Defining Elements
issue_title = Element('issue-title')
# Creating the Nodes
issue_title_node = Node(element=issue_title, graph=node.get_leaf_graph())