import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Issue ID ''' 
# Defining Elements
issue_id = Element('issue-id')
# Creating the Nodes
issue_id_node = Node(element=issue_id, graph=node.get_leaf_graph())