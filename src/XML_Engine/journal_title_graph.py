import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Journal Title''' 
# Defining Elements
journal_title = Element('journal-title')
# Creating the Nodes
journal_title_node = Node(element=journal_title, graph=node.get_leaf_graph())
