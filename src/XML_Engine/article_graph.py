import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Article ''' 
# Defining Elements
article = Element('article')
# Creating the Nodes
article_node = Node(element=article, graph=node.get_leaf_graph())
