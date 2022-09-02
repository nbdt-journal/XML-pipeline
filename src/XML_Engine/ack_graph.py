import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Acknowledgements ''' 
# Defining Elements
ack = Element('ack')
# Creating the Nodes
G_ack = nx.DiGraph()
ack_node = Node(element=ack, graph=G_ack)
first_node = node.get_first_node()
last_node = node.get_last_node()
G_ack.add_nodes_from([first_node, last_node, object_id_node, label_node, title_node, abstract_node, kwd_group_node, subj_group_node, p_node, sec_node, ref_list_node])

G_ack.add_edge(first_node, object_id_node)
G_ack.add_edge(first_node, label_node)
G_ack.add_edge(first_node, title_node)
G_ack.add_edge(first_node, abstract_node)
G_ack.add_edge(first_node, kwd_group_node)
G_ack.add_edge(first_node, subj_group_node)
G_ack.add_edge(first_node, p_node)
G_ack.add_edge(first_node, sec_node)
G_ack.add_edge(first_node, ref_list_node)
G_ack.add_edge(first_node, last_node)

G_ack.add_edge(object_id_node, object_id_node)
G_ack.add_edge(object_id_node, label_node)
G_ack.add_edge(object_id_node, title_node)
G_ack.add_edge(object_id_node, abstract_node)
G_ack.add_edge(object_id_node, kwd_group_node)
G_ack.add_edge(object_id_node, subj_group_node)
G_ack.add_edge(object_id_node, p_node)
G_ack.add_edge(object_id_node, sec_node)
G_ack.add_edge(object_id_node, ref_list_node)
G_ack.add_edge(object_id_node, last_node)

G_ack.add_edge(label_node, title_node)
G_ack.add_edge(label_node, abstract_node)
G_ack.add_edge(label_node, kwd_group_node)
G_ack.add_edge(label_node, subj_group_node)
G_ack.add_edge(label_node, p_node)
G_ack.add_edge(label_node, sec_node)
G_ack.add_edge(label_node, ref_list_node)
G_ack.add_edge(label_node, last_node)

G_ack.add_edge(title_node, abstract_node)
G_ack.add_edge(title_node, kwd_group_node)
G_ack.add_edge(title_node, subj_group_node)
G_ack.add_edge(title_node, p_node)
G_ack.add_edge(title_node, sec_node)
G_ack.add_edge(title_node, ref_list_node)
G_ack.add_edge(title_node, last_node)

G_ack.add_edge(abstract_node, abstract_node)
G_ack.add_edge(abstract_node, kwd_group_node)
G_ack.add_edge(abstract_node, subj_group_node)
G_ack.add_edge(abstract_node, p_node)
G_ack.add_edge(abstract_node, sec_node)
G_ack.add_edge(abstract_node, ref_list_node)
G_ack.add_edge(abstract_node, last_node)

G_ack.add_edge(kwd_group_node, kwd_group_node)
G_ack.add_edge(kwd_group_node, subj_group_node)
G_ack.add_edge(kwd_group_node, p_node)
G_ack.add_edge(kwd_group_node, sec_node)
G_ack.add_edge(kwd_group_node, ref_list_node)
G_ack.add_edge(kwd_group_node, last_node)

G_ack.add_edge(subj_group_node, subj_group_node)
G_ack.add_edge(subj_group_node, p_node)
G_ack.add_edge(subj_group_node, sec_node)
G_ack.add_edge(subj_group_node, ref_list_node)
G_ack.add_edge(subj_group_node, last_node)

G_ack.add_edge(p_node, p_node)
G_ack.add_edge(p_node, sec_node)
G_ack.add_edge(p_node, ref_list_node)
G_ack.add_edge(p_node, last_node)

G_ack.add_edge(sec_node, sec_node)
G_ack.add_edge(sec_node, ref_list_node)
G_ack.add_edge(sec_node, last_node)

G_ack.add_edge(ref_list_node, ref_list_node)
G_ack.add_edge(ref_list_node, last_node)