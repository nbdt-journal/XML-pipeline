import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for question-wrap ''' 
# Defining Elements
question_wrap = Element('question-wrap')
# Creating the Nodes
question_wrap_node = Node(element=question_wrap, graph=node.get_leaf_graph())
