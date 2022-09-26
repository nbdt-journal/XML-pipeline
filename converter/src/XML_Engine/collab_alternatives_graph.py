import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for collab-alternatives ''' 
# Defining Elements
collab_alternatives = Element('collab-alternatives')
# Creating the Nodes
G_collab_alternatives = nx.DiGraph()
first_node = node.get_first_node()
last_node = node.get_last_node()
G_collab_alternatives.add_edge(first_node, collab_node)
G_collab_alternatives.add_edge(collab_node, collab_node)
G_collab_alternatives.add_edge(collab_node, last_node)
    
collab_alternatives_node = Node(element=collab_alternatives, graph=G_collab_alternatives)
