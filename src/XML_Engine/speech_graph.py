import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Speech ''' 
# Defining Elements
speech = Element('speech')
# Creating the Nodes
speech_node = Node(element=speech, graph=node.get_leaf_graph())
