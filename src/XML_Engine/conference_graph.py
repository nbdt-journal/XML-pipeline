import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for conference ''' 
# Defining Elements
conference = Element('conference')
# Creating the Nodes
conference_node = Node(element=conference, graph=node.get_leaf_graph())