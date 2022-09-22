import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for textual-form ''' 
# Defining Elements
textual_form = Element('textual-form')
# Creating the Nodes
textual_form_node = Node(element=textual_form, graph=node.get_leaf_graph())
