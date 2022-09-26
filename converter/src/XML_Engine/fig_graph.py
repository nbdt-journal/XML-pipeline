import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for fig ''' 
# Defining Elements
fig = Element('fig')

G_fig = nx.DiGraph()
group_1 = [alt_text_node, long_desc_node, email_node, ext_link_node, uri_node]
group_2 = [disp_formula_node, disp_formula_group_node, chem_struct_wrap_node, disp_quote_node, speech_node, statement_node, verse_group_node, table_wrap_node, p_node, def_list_node, list_node, alternatives_node, array_node, code_node, graphic_node, media_node, preformat_node, xref_node]
group_3 = [attrib_node, permissions_node]

G_fig.add_nodes_from([node.get_first_node(), node.get_last_node(), object_id_node, label_node, caption_node, abstract_node, kwd_group_node, subj_group_node])
G_fig.add_nodes_from(group_1)
G_fig.add_nodes_from(group_2)
G_fig.add_nodes_from(group_3)

for i in list(G_fig.nodes):
    for j in list(G_fig.nodes):
        if i.element.name == 'first':
            if j.element.name != 'first':
                G_fig.add_edge(i, j)
        
        if i.element.name == 'object-id':
            if j.element.name != 'first':
                G_fig.add_edge(i. j)

        if i.element.name == 'label':
            if j.element.name not in ['first', 'object-id']:
                G_fig.add_edge(i, j)

        if i.element.name == 'caption':
            if j.element.name not in ['first', 'object-id', 'label']:
                G_fig.add_edge(i, j)

        if i.element.name == 'abstract':
            if j.element.name not in ['first', 'object-id', 'label', 'caption']:
                G_fig.add_edge(i, j)

        if i.element.name == 'kwd-group':
            if j.element.name not in ['first', 'object-id', 'label', 'caption', 'abstract']:
                G_fig.add_edge(i, j)

        if i.element.name == 'subj-group':
            if j.element.name not in ['first', 'object-id', 'label', 'caption', 'abstract', 'kwd-group']:
                G_fig.add_edge(i, j)

        if i.element in group_1:
            if j.element in group_1 or j.element in group_2 or j.element in group_3 or j.element.name == 'last':
                G_fig.add_edge(i, j)

        if i.element in group_2:
            if j.element in group_2 or j.element in group_3 or j.element.name == 'last':
                G_fig.add_edge(i, j)
        
        if i.element in group_3:
            if j.element in group_3 or j.element.name == 'last':
                G_fig.add_edge(i, j)

# Creating the Nodes
fig_node = Node(element=fig, graph=G_fig)