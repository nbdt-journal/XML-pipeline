import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for State ''' 
# Defining Elements
state = Element('state')
# Creating the Nodes
state_node = Node(element=state, graph=node.get_leaf_graph())
