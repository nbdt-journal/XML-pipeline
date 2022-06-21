import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for pub-history ''' 
# Defining Elements
pub_history = Element('pub-history')
# Creating the Nodes
pub_history_node = Node(element=pub_history, graph=node.get_leaf_graph())