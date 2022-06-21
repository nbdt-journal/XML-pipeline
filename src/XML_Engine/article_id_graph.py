import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Article-ID ''' 
# Defining Elements
article_id = Element('article-id')
# Creating the Nodes
article_id_node = Node(element=article_id, graph=node.get_leaf_graph())