import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Issue Subtitle ''' 
# Defining Elements
issue_subtitle = Element('issue-subtitle')
# Creating the Nodes
issue_subtitle_node = Node(element=issue_subtitle, graph=node.get_leaf_graph())