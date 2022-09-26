import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for disp-quote ''' 
# Defining Elements
disp_quote = Element('disp-quote')
# Creating the Nodes
G_disp_quote = nx.DiGraph()
disp_quote_node = Node(element=disp_quote, graph=G_disp_quote)

group_1 = [address_node, alternatives_node, answer_node, answer_set_node, array_node, block_alternatives_node, boxed_text_node, chem_struct_wrap_node, code_node, explanation_node, fig_node, fig_group_node, graphic_node, media_node, preformat_node, question_node, question_wrap_node, question_wrap_group_node, supplementary_material_node, table_wrap_node, table_wrap_group_node, disp_formula_node, disp_formula_group_node, def_list_node, list_node, tex_math_node, mml_math_node, p_node, related_article_node, related_object_node, disp_quote_node, speech_node, statement_node, verse_group_node]
group_2 = [attrib_node, permissions_node]

G_disp_quote.add_nodes_from([node.get_first_node(), node.get_last_node()])
G_disp_quote.add_nodes_from(group_1)
G_disp_quote.add_nodes_from(group_2)

for i in list(G_disp_quote.nodes):
    for j in list(G_disp_quote.nodes):
        if i.element.name == 'first':
            if j.element.name != 'first':
                G_disp_quote.add_edge(i, j)
        if i.element.name == 'label':
            if j.element.name not in ['first', 'label']:
                G_disp_quote.add_edge(i, j)
        if i.element.name == 'title':
            if j.element.name not in ['first', 'label', 'title']:
                G_disp_quote.add_edge(i, j)
        if i in group_1:
            if j.element.name not in ['first', 'label', 'title']:
                G_disp_quote.add_edge(i, j)
        if i in group_2:
            if j in group_2 or j.element.name == 'last':
                G_disp_quote.add_edge(i, j)

