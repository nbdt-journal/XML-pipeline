import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for disp-formula-group ''' 
# Defining Elements
disp_formula_group = Element('disp-formula-group')
# Creating the Nodes
G_disp_formula_group = nx.DiGraph()
disp_formula_group_node = Node(element=disp_formula_group, graph=G_disp_formula_group)

group_1 = [alt_text_node, long_desc_node, email_node, ext_link_node, uri_node]
group_2 = [disp_formula_node, disp_formula_group_node]
G_disp_formula_group.add_nodes_from([node.get_first_node(), node.get_last_node(), object_id_node, label_node, caption_node, abstract_node, kwd_group_node, subj_group_node])
G_disp_formula_group.add_nodes_from(group_1)
G_disp_formula_group.add_nodes_from(group_2)

for i in list(G_disp_formula_group.nodes):
    for j in list(G_disp_formula_group.nodes):
        if i.element.name in ['first', 'object-id']
            if j.element.name != 'first':
                G_disp_formula_group.add_edge(i, j)
        if i.element.name == 'label':
            if j.element.name not in ['first', 'object-id', 'label']
                G_disp_formula_group.add_edge(i, j)  
        if i.element.name == 'caption':
            if j.element.name not in ['first', 'object-id', 'label', 'caption']
                G_disp_formula_group.add_edge(i, j) 
        if i.element.name == 'abstract':
            if j.element.name not in ['first', 'object-id', 'label', 'caption']
                G_disp_formula_group.add_edge(i, j)   
        if i.element.name == 'kwd-group':
            if j.element.name not in ['first', 'object-id', 'label', 'caption', 'abstract']
                G_disp_formula_group.add_edge(i, j)    
        if i.element.name == 'subj-group':
            if j.element.name not in ['first', 'object-id', 'label', 'caption', 'kwd-group']
                G_disp_formula_group.add_edge(i, j)   
        if i in group_1:
            if j in group_1 or j in group_2 or j.element.name == 'last':
                G_disp_formula_group.add_edge(i, j)
        if i in group_2:
            if j in group_2 or j.element.name == 'last':
                G_disp_formula_group.add_edge(i, j)
   

