import networkx as nx 

import node
from node import Node 
from element import Element 

from subj_group_graph import subj_group_node 
from series_title_graph import series_title_node
from series_text_graph import series_text_node

''' Building a graph for Article Categories ''' 
# Defining Elements
article_categories = Element('article-categories')
# Creating the Graph 
G_article_categories = nx.DiGraph()
article_categories_node = Node(element=article_categories, graph=G_article_categories)
# creating the nodes
first_node = node.get_first_node()
last_node = node.get_last_node()
# adding the nodes
G_article_categories.add_node(first_node)
G_article_categories.add_node(subj_group_node)
G_article_categories.add_node(series_title_node)
G_article_categories.add_node(series_text_node)
G_article_categories.add_node(last_node)
# adding the edges
G_article_categories.add_edge(first_node, subj_group_node)
G_article_categories.add_edge(first_node, series_title_node)
G_article_categories.add_edge(first_node, series_text_node)
G_article_categories.add_edge(first_node, last_node)
G_article_categories.add_edge(subj_group_node, subj_group_node)
G_article_categories.add_edge(subj_group_node, series_title_node)
G_article_categories.add_edge(subj_group_node, series_text_node)
G_article_categories.add_edge(subj_group_node, last_node)
G_article_categories.add_edge(series_title_node, series_title_node)
G_article_categories.add_edge(series_title_node, series_text_node)
G_article_categories.add_edge(series_title_node, last_node)
G_article_categories.add_edge(series_text_node, series_text_node)
G_article_categories.add_edge(series_text_node, last_node)

if __name__ == '__main__':
    import xml.etree.ElementTree as ET
    tree = ET.parse('test_samples/article_categories.xml')
    root = tree.getroot()
    print(article_categories_node.check(root))