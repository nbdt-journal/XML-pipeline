import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Volume Issue Group ''' 
# Defining Elements
volume_issue_group = Element('volume-issue-group')
# Creating the Nodes
volume_issue_group_node = Node(element=volume_issue_group, graph=node.get_leaf_graph())