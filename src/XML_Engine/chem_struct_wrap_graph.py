import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for chem-struct-wrap ''' 
# Defining Elements
chem_struct_wrap = Element('chem-struct-wrap')
G_chem_struct_wrap = nx.DiGraph()
    
G_chem_struct_wrap.add_nodes_from([node.get_first_node(), node.get_last_node(), object_id_node, label_node, caption_node, abstract_node, kwd_group_node, subj_group_node])
group_1 = [alt_text_node, long_desc_node, email_node, ext_link_node, uri_node]
group_2 = [alternatives_node, chem_struct_node, code_node, graphic_node, media_node, preformat_node, textual_form_node]
group_3 = [attrib_node, permissions_node]

for i in list(G_chem_struct_wrap.nodes):
    for j in list(G_chem_struct_wrap.nodes):
        if i.element.name in ['first', 'object-id']:
            if j.element.name not in ['first', 'last'] or j.element not in group_3:
                G_chem_struct_wrap.add_edge(i, j)
        if i.element.name == 'label':
           if j.element.name not in ['first', 'last', 'object-id'] or j.element not in group_3:
                G_chem_struct_wrap.add_edge(i, j)
        if i.element.name == 'caption':
            if j.element.name not in ['first', 'last', 'object-id', 'caption'] or j.element not in group_3:
                G_chem_struct_wrap.add_edge(i, j)
        if i.element.name == 'abstract':
            if j.element.name not in ['first', 'last', 'object-id'] or j.element not in group_3:
                G_chem_struct_wrap.add_edge(i, j)
        if i.element.name == 'kwd-group':
            if j.element.name not in ['first', 'last', 'object-id', 'abstract'] or j.element not in group_3:
                G_chem_struct_wrap.add_edge(i, j)
        if i.element.name == 'subj-group':
            if j.element.name not in ['first', 'last', 'object-id', 'kwd-group'] or j.element not in group_3:
                G_chem_struct_wrap.add_edge(i, j)
        if i.element in group_1:
            if j.element in group_1 or j.element in group_2:
                G_chem_struct_wrap.add_edge(i, j)
        if i.element in group_2:
            if j.element in group_2 or j.element in group_3 or j.element.name == 'last':
                G_chem_struct_wrap.add_edge(i, j)
        if i.element in group_3:
            if j.element in group_3 or j.element.name == 'last':
                G_chem_struct_wrap.add_edge(i, j)

chem_struct_wrap_node = Node(element=chem_struct_wrap, graph=G_chem_struct_wrap)