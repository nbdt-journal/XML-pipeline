import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Author Notes ''' 
# Defining Elements
author_notes = Element('author-notes')
# Creating the Nodes
author_notes_node = Node(element=author_notes, graph=node.get_leaf_graph())