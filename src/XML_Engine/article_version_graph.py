import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Article Version ''' 
# Defining Elements
article_version = Element('article-version')
# Creating the Nodes
article_version_node = Node(element=article_version, graph=node.get_leaf_graph())