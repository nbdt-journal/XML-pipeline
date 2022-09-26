import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for fig-group ''' 
# Defining Elements
fig_group = Element('fig-group')

G_fig_group = nx.DiGraph()
group_1 = [alt_text_node, long_desc_node, email_node, ext_link_node, uri_node]
group_2 = [fig_node, block_alternatives_node, xref_node, alternatives_node, graphic_node, media_node]

G_fig_group.add_nodes_from([node.get_first_node(), node.get_last_node(), object_id_node, label_node, caption_node, abstract_node, kwd_group_node, subj_group_node])
G_fig_group.add_nodes_from(group_1)
G_fig_group.add_nodes_from(group_2)

for i in list(G_fig_group.nodes):
    for j in list(G_fig_group.nodes):
        if i.element.name == 'first':
            if j.element.name != 'first':
                G_fig_group.add_edge(i, j)
        
        if i.element.name == 'object-id':
            if j.element.name != 'first':
                G_fig_group.add_edge(i. j)

        if i.element.name == 'label':
            if j.element.name not in ['first', 'object-id']:
                G_fig_group.add_edge(i, j)

        if i.element.name == 'caption':
            if j.element.name not in ['first', 'object-id', 'label']:
                G_fig_group.add_edge(i, j)

        if i.element.name == 'abstract':
            if j.element.name not in ['first', 'object-id', 'label', 'caption']:
                G_fig_group.add_edge(i, j)

        if i.element.name == 'kwd-group':
            if j.element.name not in ['first', 'object-id', 'label', 'caption', 'abstract']:
                G_fig_group.add_edge(i, j)

        if i.element.name == 'subj-group':
            if j.element.name not in ['first', 'object-id', 'label', 'caption', 'abstract', 'kwd-group']:
                G_fig_group.add_edge(i, j)

        if i.element in group_1:
            if j.element in group_1 or j.element in group_2 or j.element.name == 'last':
                G_fig_group.add_edge(i, j)

        if i.element in group_2:
            if j.element in group_2 or j.element.name == 'last':
                G_fig_group.add_edge(i, j)


# Creating the Nodes
fig_group_node = Node(element=fig_group, graph=G_fig_group)