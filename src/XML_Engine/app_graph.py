import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for app ''' 
# Defining Elements
app = Element('app')
G_app = nx.DiGraph()

group_1 = [address_node, alternatives_node, answer_node, answer_set_node, array_node, block_alternatives_node, boxed_text_node, chem_struct_wrap_node, code_node, explanation_node, fig_node, fig_group_node, graphic_node, media_node, preformat_node, question_node, question_wrap_node, question_wrap_group_node, supplementary_material_node, table_wrap_node, table_wrap_group_node, disp_formula_node, disp_formula_group_node, def_list_node, list_node, tex_math_node, mml_math_node, p_node, related_article_node, related_object_node, disp_quote_node, speech_node, statement_node, verse_group_node]
group_2 = [fn_group_node, glossary_node, ref_list_node]
G_app.add_nodes_from(group_1)
G_app.add_nodes_from(group_2)
G_app.add_nodes_from([sec_meta_node, label_node, title_node, sec_node, permissions_node, node.get_first_node(), node.get_last_node()])

for i in list(G_app.nodes):
    for j in list(G_app.nodes):
        if i.element.name == 'first':
            if j.element.name in ['sec-meta', 'label', 'title']:
                G_app.add_edge(i, j)
        if i.element.name == 'sec-meta':
            if j.element.name in ['label', 'title']:
                G_app.add_edge(i, j)
        if i.element.name == 'label':
            if j.element.name not in ['last', 'sec-meta', 'label']:
                G_app.add_edge(i, j)
        if i.element.name == 'title':
            if j.element.name not in ['last', 'sec-meta', 'title', 'label']:
                G_app.add_edge(i, j)
        if i.element in group_1:
            if j.element.name in ['sec', 'permissions', 'last'] or j.element in group_1 or j.element in group_2:
                G_app.add_edge(i, j)
        if i.element.name == 'sec':
            if j.element.name in ['sec', 'permissions', 'last'] or j.element in group_2:
                G_app.add_edge(i, j)
        if i.element in group_2:
            if j.element.name in ['last', 'permissions'] or j.element in group_2:
                G_add.add_edge(i, j)
        if i.element.name == 'permissions':
            if j.element.name == 'last':
                G_app.add_edge(i, j) 
        

app_node = Node(element=app, graph=G_app)