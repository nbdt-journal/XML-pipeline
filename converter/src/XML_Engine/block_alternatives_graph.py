import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for bio ''' 
# Defining Elements
bio = Element('bio')
# Creating the Nodes
bio_node = Node(element=bio, graph=node.get_leaf_graph())

group_1 = [sec_meta_node, label_node, title_node]
group_2 = [address_node, alternatives_node, answer_node, answer_set_node, array_node, block_alternatives_node, boxed_text_node, chem_struct_wrap_node, code_node, explanation_node, fig_node, fig_group_node, graphic_node, media_node, preformat_node, question_node, question_wrap_node, question_wrap_group_node, supplementary_material_node, table_wrap_node, table_wrap_group_node, disp_formula_node, disp_formula_group_node, def_list_node, list_node, tex_math_node, mml_math_node, p_node, related_article_node, related_object_node, disp_quote_node, speech_node, statement_node, verse_group_node]
group_3 = [sec_node]
group_4 = [fn_group_node, glossary_node, ref_list_node]

G_bio = nx.DiGraph()
rom([node.get_first_node(), node.get_last_node()])

for i in list(G.nodes):
    for j in list(G.nodes):
       