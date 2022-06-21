import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Notes ''' 
# Defining Elements
notes = Element('notes')
# Creating the Nodes
notes_node = Node(element=notes, graph=node.get_leaf_graph())