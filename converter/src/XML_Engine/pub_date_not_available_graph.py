import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Pub Date Not Available''' 
# Defining Elements
pub_date_not_available = Element('pub-date-not-available')
# Creating the Nodes
pub_date_not_available_node = Node(element=pub_date_not_available, graph=node.get_leaf_graph())