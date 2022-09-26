import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for milestone-end ''' 
# Defining Elements
milestone_end = Element('milestone-end')
# Creating the Nodes
milestone_end_node = Node(element=milestone_end, graph=node.get_leaf_graph())