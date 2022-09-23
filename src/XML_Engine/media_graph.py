import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for media ''' 
# Defining Elements
media = Element('media')
G_media = nx.DiGraph()
G_media.add_nodes_from([node.get_first_node(), node.get_last_node(), alt_text_node, long_desc_node, abstract_node, email_node, ext_link_node, uri_node, caption_node, attrib_node, permissions_node, object_id_node, label_node, kwd_group_node, subj_group, xref_node])

for i in list(G_media.nodes):
    for j in list(G_media.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_media.add_edge(i, j)
# Creating the Nodes
media_node = Node(element=media, graph=G_media)