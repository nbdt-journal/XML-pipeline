import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for related-article ''' 
# Defining Elements
related_article = Element('related-article')
# Creating the Nodes
related_article_node = Node(element=related_article, graph=node.get_leaf_graph())