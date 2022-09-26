import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for graphic ''' 
# Defining Elements
graphic = Element('graphic')
G_graphic = nx.DiGraph()
G_graphic.add_nodes_from([node.get_first_node(), node.get_last_node(), alt_text_node, long_desc_node, abstract_node, email_node, ext_link_node, uri_node, caption_node, attrib_node, permissions_node, object_id_node, label_node, kwd_group_node, subj_group_node, xref_node])
for i in list(G_graphic.nodes):
    for j in list(G_graphic.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_graphic.add_edge(i, j)

# Creating the Nodes
graphic_node = Node(element=graphic, graph=G_graphic)
