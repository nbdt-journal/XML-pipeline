import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for answer-set ''' 
# Defining Elements
answer_set = Element('answer-set')
# Creating the Nodes
G_answer_set = nx.DiGraph()
first_node = node.get_first_node()
last_node = node.get_last_node()
G_answer_set.add_nodes_from([first_node, last_node, object_id_node, label_node, title_node, subtitle_node, alt_title_node, answer_node, p_node, explanation_node])

G_answer_set.add_edge(first_node, object_id_node)
G_answer_set.add_edge(first_node, label_node)
G_answer_set.add_edge(first_node, title_node)
G_answer_set.add_edge(first_node, subtitle_node)
G_answer_set.add_edge(first_node, alt_title_node)
G_answer_set.add_edge(first_node, answer_node)
G_answer_set.add_edge(first_node, p_node)
G_answer_set.add_edge(first_node, explanation_node)

G_answer_set.add_edge(object_id_node, object_id_node)
G_answer_set.add_edge(object_id_node, label_node)
G_answer_set.add_edge(object_id_node, title_node)
G_answer_set.add_edge(object_id_node, subtitle_node)
G_answer_set.add_edge(object_id_node, alt_title_node)
G_answer_set.add_edge(object_id_node, answer_node)
G_answer_set.add_edge(object_id_node, p_node)
G_answer_set.add_edge(object_id_node, explanation_node)

G_answer_set.add_edge(label_node, title_node)
G_answer_set.add_edge(label_node, subtitle_node)
G_answer_set.add_edge(label_node, alt_title_node)
G_answer_set.add_edge(label_node, answer_node)
G_answer_set.add_edge(label_node, p_node)
G_answer_set.add_edge(label_node, explanation_node)

G_answer_set.add_edge(title_node, subtitle_node)
G_answer_set.add_edge(title_node, alt_title_node)
G_answer_set.add_edge(title_node, answer_node)
G_answer_set.add_edge(title_node, p_node)
G_answer_set.add_edge(title_node, explanation_node)

G_answer_set.add_edge(subtitle_node, subtitle_node)
G_answer_set.add_edge(subtitle_node, alt_title_node)
G_answer_set.add_edge(subtitle_node, answer_node)
G_answer_set.add_edge(subtitle_node, p_node)
G_answer_set.add_edge(subtitle_node, explanation_node)

G_answer_set.add_edge(alt_title_node, alt_title_node)
G_answer_set.add_edge(alt_title_node, answer_node)
G_answer_set.add_edge(alt_title_node, p_node)
G_answer_set.add_edge(alt_title_node, explanation_node)

G_answer_set.add_edge(answer_node, answer_node)
G_answer_set.add_edge(answer_node, p_node)
G_answer_set.add_edge(answer_node, explanation_node)
G_answer_set.add_edge(answer_node, last_node)


G_answer_set.add_edge(p_node, answer_node)
G_answer_set.add_edge(p_node, p_node)
G_answer_set.add_edge(p_node, explanation_node)
G_answer_set.add_edge(p_node, last_node)


G_answer_set.add_edge(explanation_node, answer_node)
G_answer_set.add_edge(explanation_node, p_node)
G_answer_set.add_edge(explanation_node, explanation_node)
G_answer_set.add_edge(explanation_node, last_node)


