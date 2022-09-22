import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for event-desc ''' 
# Defining Elements
event_desc = Element('event-desc')
# Creating the Nodes
event_desc_node = Node(element=event_desc, graph=node.get_leaf_graph())