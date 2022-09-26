import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for front ''' 
# Defining Elements
front = Element('front')

first_node = node.get_first_node()
last_node = node.get_last_node()

G_front = nx.DiGraph()
G_front.add_nodes_from([first_node, last_node, journal_meta_node, article_meta_node, notes_node])
G_front.add_edge(first_node, journal_meta_node)
G_front.add_edge(journal_meta_node, article_meta_node)
G_front.add_edge(article_meta_node, notes_node)
G_front.add_edge(article_meta_node, last_node)
G_front.add_edge(notes_node, last_node)

# Creating the Nodes
front_node = Node(element=front, graph=G_front)