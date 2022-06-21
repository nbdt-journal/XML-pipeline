import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Issue Title Group ''' 
# Defining Elements
issue_title_group = Element('issue-title-group')
# Creating the Nodes
issue_title_group_node = Node(element=issue_title_group, graph=node.get_leaf_graph())