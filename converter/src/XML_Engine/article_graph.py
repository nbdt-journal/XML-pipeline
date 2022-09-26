import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Article ''' 
# Defining Elements
article = Element('article')
# Creating the Nodes
G_article = nx.DiGraph() 
article_node = Node(element=article, graph=G_article)

G_article.add_nodes_from([processing_meta_node, front_node, body_node, back_node, floats_group_node, sub_article_node, response_node, node.get_first_node(), node.get_last_node()])

for i in G_article.nodes:
    for j in G_article.nodes:
        if i.element.name == 'first':
            if j.element.name in ['processing-meta', 'front']:
                G_article.add_edge(i, j)
        if i.element.name == 'processing-meta':
            if j.element.name == 'front':
                G_article.add_edge(i, j)
        if i.element.name == 'front':
            if j.element.name in ['body', 'back', 'floats-group', 'sub-article', 'response', 'last']:
                G_article.add_edge(i, j)
        if i.element.name == 'body':
            if j.element.name in ['back', 'floats-group', 'sub-article', 'response', 'last']:
                G_article.add_edge(i, j)
        if i.element.name == 'back':
            if j.element.name in ['floats-group', 'sub-article', 'response', 'last']:
                G_article.add_edge(i, j)
        if i.element.name == 'floats-group':
            if j.element.name in ['sub-article', 'response', 'last']:
                G_article.add_edge(i, j)
        if i.element.name == 'sub-article':
            if j.element.name in ['sub-article', 'response', 'last']:
                G_article.add_edge(i, j)
        if i.element.name == 'response':
            if j.element.name in ['response', 'last']:
                G_article.add_edge(i, j)

