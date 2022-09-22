import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for event ''' 
# Defining Elements
event = Element('event')
# Creating the Nodes
event_node = Node(element=event, graph=node.get_leaf_graph())