import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for sub-article ''' 
# Defining Elements
sub_article = Element('sub-article')
# Creating the Nodes
sub_article_node = Node(element=sub_article, graph=node.get_leaf_graph())
