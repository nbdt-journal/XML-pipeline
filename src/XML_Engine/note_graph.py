import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for note ''' 
# Defining Elements
note = Element('note')
# Creating the Nodes
note_node = Node(element=note, graph=node.get_leaf_graph())