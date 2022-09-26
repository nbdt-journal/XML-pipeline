import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for question ''' 
# Defining Elements
question = Element('question')
# Creating the Nodes
question_node = Node(element=question, graph=node.get_leaf_graph())
