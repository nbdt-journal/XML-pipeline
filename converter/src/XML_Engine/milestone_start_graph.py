import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for milestone-start ''' 
# Defining Elements
milestone_start = Element('milestone-start')
# Creating the Nodes
milestone_start_node = Node(element=milestone_start, graph=node.get_leaf_graph())