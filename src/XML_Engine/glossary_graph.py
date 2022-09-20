import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for glossary ''' 
# Defining Elements
glossary = Element('glossary')


G_glossary = nx.DiGraph()
G_glossary.add_nodes_from([object_id_node, label_node, title_node, glossary_node, node.get_first_node(), node.get_last_node()])
group = [address_node, alternatives_node, answer_node, answer_set_node, array_node, block_alternatives_node, boxed_text_node, chem_struct_wrap_node, code_node, explanation_node, fig_node, fig_group_node, graphic_node, media_node, preformat_node, question_node, question_wrap_node, question_wrap_group_node, supplementary_material_node, table_wrap_node, table_wrap_group_node, disp_formula_node, disp_formula_group_node, def_list_node, list_node, tex_math_node, mml_math_node, p_node, related_article_node, related_object_node, disp_quote_node, speech_node, statement_node, verse_group_node]

for i in list(G_glossary.nodes):
    for j in list(G_glossary.nodes):
        if i.element.name == 'first' or i.element.name == 'object-id':
            if j.element.name != 'first':
                G_glossary.add_edge(i, j)

        if i.element.name == 'label':
            if j.element.name not in ['first', 'object-id', 'label']:
                G_glossary.add_edge(i, j)
        
        if i.element.name == 'title':
            if j.element.name not in ['first', 'object-id', 'label', 'title']:
                G_glossary.add_edge(i, j)
        
        if i in group:
            if j in group or j.element.name in ['glossary', 'last']:
                G_glossary.add_edge(i, j)
        
        if i.element.name == 'glossary':
            if j.element.name in ['glossary', 'last']:
                G_glossary.add_edge(i, j)

# Creating the Nodes
glossary_node = Node(element=glossary, graph=G_glossary)
