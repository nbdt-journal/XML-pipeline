import networkx as nx 

import node
from node import Node 
from element import Element 

from article_version_graph import article_version_node

''' Building a graph for Article Version Alternatives''' 
# Defining Elements
article_version_alternatives = Element('article-version-alternatives')
# Creating the Nodes
first_node = node.get_first_node()
last_node = node.get_last_node()
# Creating the graph
G_article_version_alternatives = nx.DiGraph()
# adding the nodes
G_article_version_alternatives.add_node(first_node)
G_article_version_alternatives.add_node(article_version_node)
G_article_version_alternatives.add_node(last_node)
# adding the edges
G_article_version_alternatives.add_edge(first_node, article_version_node)
G_article_version_alternatives.add_edge(article_version_node, article_version_node)
G_article_version_alternatives.add_edge(article_version_node, last_node)
# creating the node
article_version_alternatives_node = Node(element=article_version_alternatives, graph=G_article_version_alternatives)