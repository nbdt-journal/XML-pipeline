import networkx as nx 

import node
from node import Node 
from element import Element 

from article_title_graph import article_title_node
from subtitle_graph import subtitle_node
from trans_title_group_graph import trans_title_group_node
from alt_title_graph import alt_title_node 
from fn_group_graph import fn_group_node

''' Building a graph for Title Group ''' 
# Defining Elements
title_group = Element('title-group')
# Creating the Graph
G_title_group = nx.DiGraph()
# adding the nodes
first_node = node.get_first_node()
last_node = node.get_last_node()
G_title_group.add_node(first_node)
G_title_group.add_node(article_title_node)
G_title_group.add_node(subtitle_node)
G_title_group.add_node(trans_title_group_node)
G_title_group.add_node(alt_title_node)
G_title_group.add_node(fn_group_node)
G_title_group.add_node(last_node)
# adding the edges
G_title_group.add_edge(first_node, article_title_node)
G_title_group.add_edge(article_title_node, subtitle_node)
G_title_group.add_edge(article_title_node, trans_title_group_node)
G_title_group.add_edge(article_title_node, alt_title_node)
G_title_group.add_edge(article_title_node, fn_group_node)
G_title_group.add_edge(article_title_node, last_node)
G_title_group.add_edge(subtitle_node, subtitle_node)
G_title_group.add_edge(subtitle_node, trans_title_group_node)
G_title_group.add_edge(subtitle_node, alt_title_node)
G_title_group.add_edge(subtitle_node, fn_group_node)
G_title_group.add_edge(subtitle_node, last_node)
G_title_group.add_edge(trans_title_group_node, trans_title_group_node)
G_title_group.add_edge(trans_title_group_node, alt_title_node)
G_title_group.add_edge(trans_title_group_node, fn_group_node)
G_title_group.add_edge(trans_title_group_node, last_node)
G_title_group.add_edge(alt_title_node, alt_title_node)
G_title_group.add_edge(alt_title_node, fn_group_node)
G_title_group.add_edge(alt_title_node, last_node)
G_title_group.add_edge(fn_group_node, fn_group_node)
# defining the node
title_group_node = Node(element=title_group, graph=G_title_group)

if __name__ == '__main__':
    import xml.etree.ElementTree as ET
    tree = ET.parse('test_samples/title_group.xml')
    root = tree.getroot()
    print(title_group_node.check(root))