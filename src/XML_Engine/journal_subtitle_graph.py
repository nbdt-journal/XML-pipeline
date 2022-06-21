import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Journal Subtitle ''' 
# Defining Elements
journal_subtitle = Element('journal-subtitle')
# Creating the Nodes
journal_subtitle_node = Node(element=journal_subtitle, graph=node.get_leaf_graph())
