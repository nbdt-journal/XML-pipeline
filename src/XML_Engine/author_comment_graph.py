import networkx as nx 

import node
from node import Node 
from element import Element 

from title_graph import title_node 
from p_graph import p_node

''' Building a graph for Author Comment ''' 
# Defining Elements
author_comment = Element('author-comment')
# Creating the Graph
G_author_comment = nx.DiGraph()
# adding the nodes
first_node = node.get_first_node()
last_node = node.get_last_node()
G_author_comment.add_node(first_node)
G_author_comment.add_node(title_node)
G_author_comment.add_node(p_node)
G_author_comment.add_node(last_node)
# creating the node
author_comment_node = Node(element=author_comment, graph=G_author_comment)
# adding the edges
G_author_comment.add_edge(first_node, title_node)
G_author_comment.add_edge(first_node, p_node)
G_author_comment.add_edge(title_node, p_node)
G_author_comment.add_edge(p_node, p_node)
G_author_comment.add_edge(p_node, last_node)

if __name__ == '__main__':
    import xml.etree.ElementTree as ET
    tree = ET.parse('test_samples/author_comment.xml')
    root = tree.getroot()
    print(author_comment_node.check(root))