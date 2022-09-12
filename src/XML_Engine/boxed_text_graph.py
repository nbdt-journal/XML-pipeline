import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Boxed Text ''' 
# Defining Elements
boxed_text = Element('boxed-text')
# Creating the Nodes
G_boxed_text = nx.DiGraph()
boxed_text_node = Node(element=boxed_text, graph=G_boxed_text)


group_1 = [address_node, alternatives_node, answer_node, answer_set_node, array_node, block_alternatives_node, boxed_text_node, chem_struct_wrap_node, code_node, explanation_node, fig_node, fig_group_node, graphic_node, media_node, preformat_node, question_node, question_wrap_node, question_wrap_group_node, supplementary_material_node, table_wrap_node, table_wrap_group_node, disp_formula_node, disp_formula_group_node, def_list_node, list_node, tex_math_node, mml_math_node, p_node, related_article_node, related_object_node, disp_quote_node, speech_node, statement_node, verse_group_node]
group_2 = [fn_group_node, glossary_node, ref_list_node]
group_3 = [attrib_node, permissions_node]

G_boxed_text.add_node(node.get_first_node())
G_boxed_text.add_node(node.get_last_node())
G_boxed_text.add_nodes_from([object_id_node, sec_meta_node, label_node, caption_node])
G_boxed_text.add_nodes_from(group_1)
G_boxed_text.add_nodes_from(group_2)
G_boxed_text.add_nodes_from(group_3)

for i in list(G_boxed_text.nodes):
    for j in list(G_boxed_text.nodes):
        if i.element.name in ['first', 'object-id']:
            if j.element.name != 'first':
                G_boxed_text.add_edge(i, j)
        if i.element.name == 'sec-meta':
            if j.element.name not in ['first', 'object-id', 'sec-meta']:
                G_boxed_text.add_edge(i, j)
        if i.element.name == 'label':
            if j.element.name not in ['first', 'object-id', 'sec-meta', 'label']:
                G_boxed_text.add_edge(i, j)
        if i.element.name == 'caption':
            if j.element.name not in ['first', 'object-id', 'sec-meta', 'label', 'caption']:
                G_boxed_text.add_edge(i, j)
        if i.element in group_1:
            if j.element.name not in ['first', 'object-id', 'sec-meta', 'label', 'caption']:
                G_boxed_text.add_edge(i, j)
        if i.element in group_2:
            if j.element.name not in ['first', 'object-id', 'sec-meta', 'label', 'caption']:
                if j.element not in group_1:
                    G_boxed_text.add_edge(i, j)
        if i.element in group_3:
           if j.element.name not in ['first', 'object-id', 'sec-meta', 'label', 'caption']:
                if j.element not in group_1:
                    if j.element not in group_2:
                        G_boxed_text.add_edge(i, j) 