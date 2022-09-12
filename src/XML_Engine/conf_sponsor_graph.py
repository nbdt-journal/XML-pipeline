import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for conf-sponsor ''' 
# Defining Elements
conf_sponsor = Element('conf-sponsor')
G_conf_sponsor = nx.DiGraph()
first_node = node.get_first_node()
last_node = node.get_last_node()
# Creating the Nodes
G_conf_sponsor.add_edge(first_node, institution_node)
G_conf_sponsor.add_edge(first_node, institution_wrap_node)
G_conf_sponsor.add_edge(first_node, last_node)
G_conf_sponsor.add_edge(institution_node, institution_node)
G_conf_sponsor.add_edge(institution_node, institution_wrap_node)
G_conf_sponsor.add_edge(institution_node, last_node)
G_conf_sponsor.add_edge(institution_wrap_node, institution_node)
G_conf_sponsor.add_edge(institution_wrap_node, institution_wrap_node)
G_conf_sponsor.add_edge(institution_wrap_node, last_node)

conf_sponsor_node = Node(element=conf_sponsor, graph=G_conf_sponsor)