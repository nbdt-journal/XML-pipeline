import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for question-wrap-group ''' 
# Defining Elements
question_wrap_group = Element('question-wrap-group')
# Creating the Nodes
question_wrap_group_node = Node(element=question_wrap_group, graph=node.get_leaf_graph())
