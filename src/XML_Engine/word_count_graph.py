import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for word-count ''' 
# Defining Elements
word_count = Element('word-count')
# Creating the Nodes
word_count_node = Node(element=word_count, graph=node.get_leaf_graph())
