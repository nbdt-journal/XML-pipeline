import networkx as nx 

import node 
from node import Node
from element import Element
from front_graph import front_node

''' Building a graph for Article '''
# defining the Elements
processing_meta = Element('processing-meta')
front = Element('front')
body = Element('body')
back = Element('back')
floats_group = Element('floats-group')
sub_article = Element('sub-article')
response = Element('response')
article = Element('article')
# Defining the Nodes
processing_meta_node = Node(element=processing_meta, graph=node.get_leaf_graph())
body_node = Node(element=body, graph=node.get_leaf_graph())
back_node = Node(element=back, graph=node.get_leaf_graph())
floats_group_node = Node(element=floats_group, graph=node.get_leaf_graph())
sub_article_node = Node(element=sub_article, graph=node.get_leaf_graph())
response_node = Node(element=response, graph=node.get_leaf_graph())
# Defining the Graph 
G_article = nx.DiGraph()
# creating the first and last node
first_node = node.get_first_node()
last_node = node.get_last_node()
# adding the first-node
G_article.add_node(first_node)
# adding the element nodes
G_article.add_node(processing_meta_node)
G_article.add_node(front_node)
G_article.add_node(body_node)
G_article.add_node(back_node)
G_article.add_node(floats_group_node)
G_article.add_node(sub_article_node)
G_article.add_node(response_node)
# adding the last node
G_article.add_node(last_node)
# adding the edges
G_article.add_edge(first_node, processing_meta_node)
G_article.add_edge(first_node, front_node)
G_article.add_edge(processing_meta_node, front_node)
G_article.add_edge(front_node, body_node)
G_article.add_edge(front_node, back_node)
G_article.add_edge(front_node, floats_group_node)
G_article.add_edge(front_node, sub_article_node)
G_article.add_edge(front_node, response_node)
G_article.add_edge(front_node, last_node)
G_article.add_edge(body_node, back_node)
G_article.add_edge(body_node, floats_group_node)
G_article.add_edge(body_node, sub_article_node)
G_article.add_edge(body_node, response_node)
G_article.add_edge(body_node, last_node)
G_article.add_edge(back_node, floats_group_node)
G_article.add_edge(back_node, sub_article_node)
G_article.add_edge(back_node, response_node)
G_article.add_edge(back_node, last_node)
G_article.add_edge(floats_group_node, sub_article_node)
G_article.add_edge(floats_group_node, response_node)
G_article.add_edge(floats_group_node, last_node)
G_article.add_edge(sub_article_node, sub_article_node)
G_article.add_edge(sub_article_node, last_node)
G_article.add_edge(response_node, response_node)
G_article.add_edge(response_node, last_node)
# defining the article-node
article_node = Node(element=article, graph=G_article)