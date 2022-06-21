import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Issue Sponsor ''' 
# Defining Elements
issue_sponsor = Element('issue-sponsor')
# Creating the Nodes
issue_sponsor_node = Node(element=issue_sponsor, graph=node.get_leaf_graph())