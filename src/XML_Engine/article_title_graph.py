import networkx as nx 

import node
from node import Node 
from element import Element 



''' Building a graph for Article Title ''' 
# Defining Elements
article_title = Element('article-title')
# Creating the Nodes
article_title_node = Node(element=article_title, graph=node.get_leaf_graph())