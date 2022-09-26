import networkx as nx 
from copy import deepcopy

import node
from node import Node 
from element import Element 

''' Building a graph for app-group ''' 
# Defining Elements
app_group = Element('app-group')
G_app_group = nx.DiGraph()
app_group_node = Node(element=app_group, graph=G_app_group)

group_1 = [node.get_first_node(), node.get_last_node(), address_node, alternatives_node, answer_node, answer_set_node, array_node, block_alternatives_node, boxed_text_node, chem_struct_wrap_node, code_node, explanation_node, fig_node, fig_group_node, graphic_node, media_node, preformat_node, question_node, question_wrap_node, question_wrap_group_node, supplementary_material_node, table_wrap_node, table_wrap_group_node, disp_formula_node, disp_formula_group_node, def_list_node, list_node, tex_math_node, mml_math_node, p_node, related_article_node, related_object_node, disp_quote_node, speech_node, statement_node, verse_group_node]
group_2 = [app_node, ref_list_node]
G_app_group.add_nodes_from(group_1)
G_app_group.add_nodes_from(group_2)
G_app_group.add_nodes_from([node.get_first_node(), node.get_last_node(), object_id_node, label_node, title_node, abstract_node, kwd_group_node, subj_group_node])

for i in list(G_app_group_group.nodes):
    for j in list(G_app_group_group.nodes):
        if i.element.name == 'first' or i.element.name == 'object-id':
            if j.element.name != 'first':
                G_app_group.add_edge(i, j)
        if i.element.name == 'label':
            if j.element.name not in ['first', 'object-id', 'label']:
                G_app_group.add_edge(i, j)
        if i.element.name == 'title':
            if j.element.name not in ['first', 'object-id', 'label', 'title']:
                G_app_group.add_edge(i, j)
        if i.element.name == 'abstract':
            if j.element.name not in ['first', 'object-id', 'label', 'title']:
                G_app_group.add_edge(i, j)
        if i.element.name == 'kwd-group':
            if j.element.name not in ['first', 'object-id', 'label', 'title', 'abstract']:
                G_app_group.add_edge(i, j)
        if i.element.name == 'subj-group':
            if j.element.name not in ['first', 'object-id', 'label', 'title', 'abstract', 'kwd-group']:
                G_app_group.add_edge(i, j)
        if i.element in group_1:
            if j.element in group_1 or j.element in group_2 or j.element.name == 'last':
                G_app_group.add_edge(i, j)
        if i.element in group_2:
            if j.element in group_2 or j.element.name == 'last':
                G_app_group.add_edge(i, j)
    