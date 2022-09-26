import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for caption ''' 
# Defining Elements
caption = Element('caption')
# Creating the Nodes
G_caption = nx.DiGraph()
caption_node = Node(element=caption, graph=G_caption)

first_node = node.get_first_node()
last_node = node.get_last_node()
G_caption.add_nodes_from([first_node, title_node, p_node, last_node])

G_caption.add_edge(first_node, title_node)
G_caption.add_edge(first_node, p_node)
G_caption.add_edge(first_node, last_node)
G_caption.add_edge(title_node, p_node)
G_caption.add_edge(title_node, last_node)
G_caption.add_edge(p_node, p_node)
G_caption.add_edge(p_node, last_node)