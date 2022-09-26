import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Issue Part ''' 
# Defining Elements
issue_part = Element('issue-part')
# Creating the Nodes
issue_part_node = Node(element=issue_part, graph=node.get_leaf_graph())