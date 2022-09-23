import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for event-desc ''' 
# Defining Elements
event_desc = Element('event-desc')
G_event_desc = nx.DiGraph()
first_node = node.get_first_node()
last_node = node.get_last_node()
G_event_desc.add_nodes_from([node.get_first_node(), node.get_last_node(), email_node, ext_link_node, uri_node, article_id_node, issn_node, issn_l_node, isbn_node, article_version_node, article_version_alternatives_node, date_node, string_date_node, pub_date_not_available_node])

for i in list(G_event_desc.nodes):
    for j in list(G_event_desc.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_event_desc.add_edge(i, j)
# Creating the Nodes
event_desc_node = Node(element=event_desc, graph=G_event_desc)