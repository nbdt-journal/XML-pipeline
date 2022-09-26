import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for question-preamble ''' 
# Defining Elements
question_preamble = Element('question-preamble')
# Creating the Nodes
question_preamble_node = Node(element=question_preamble, graph=node.get_leaf_graph())
