import networkx as nx 
from copy import deepcopy

import node
from node import Node 
from element import Element 

''' Building a graph for answer ''' 
# Defining Elements
answer = Element('answer')
G_answer = nx.DiGraph()

answer_node = Node(element=answer, graph=G_answer)

group_1 = [address_node, alternatives_node, answer_node, answer_set_node, array_node, block_alternatives_node, boxed_text_node, chem_struct_wrap_node, code_node, fig_node, fig_group_node, graphic_node, media_node, preformat_node, question_node, question_wrap_node, question_wrap_group_node, supplementary_material_node, table_wrap_node, table_wrap_group_node, disp_formula_node, disp_formula_group_node, def_list_node, list_node, tex_math_node, mml_math_node, p_node, related_article_node, related_object_node, disp_quote_node, speech_node, statement_node, verse_group_node]
group_2 = [fn_group_node, glossary_node, ref_list_node]

G_answer.add_nodes_from(group_1)
G_answer.add_nodes_from(group_2)
G_answer.add_nodes_from([node.get_first_node(), node.get_last_node(), label_node, title_node, subtitle_node, atl_title_node, sec_node, explanation_node])


for i in list(G_answer.nodes):
    for j in list(G_answer.nodes):
        if i.element.name == 'first':
            if j.element.name in ['object-id', 'label', 'title', 'subtitle', 'alt-title', 'sec'] or j.element in group_1:
                G_answer.add_edge(i, j)
        if  i.element.name == 'object-id':
            if j.element.name in ['object-id', 'label', 'title', 'subtitle', 'alt-title', 'sec'] or j.element in group_1:
                G_answer.add_edge(i, j)
        if  i.element.name == 'label':
            if j.element.name in ['title', 'subtitle', 'alt-title', 'sec'] or j.element in group_1:
                G_answer.add_edge(i, j)
        if  i.element.name == 'title':
            if j.element.name in ['subtitle', 'alt-title', 'sec'] or j.element in group_1:
                G_answer.add_edge(i, j)
        if  i.element.name == 'subtitle':
            if j.element.name in ['subtitle', 'alt-title', 'sec'] or j.element in group_1:
                G_answer.add_edge(i, j)
        if  i.element.name == 'alt-title':
            if j.element.name in ['alt-title', 'sec'] or j.element in group_1:
                G_answer.add_edge(i, j)
        if i.element.name == 'sec':
            if j.element.name == 'sec' or j.element in group_2 or j.element.name == 'explanation' or j.element.name == 'last':
                G_answer.add_edge(i, j)
        if i.element in group_1:
            if j.element in group_1 or j.element in group_2 or j.element.name in ['sec', 'explanation', 'last']:
                G_answer.add_edge(i, j)
        if i.element in group_2:
            if j.element in group_2 or j.element.name in ['explanation', 'last']:
                G_answer.add_edge(i, j)
        if i.element.name == 'explanation':
            if j.element.name in ['explanation', 'last']:
                G_answer.add_edge(i, j)
        