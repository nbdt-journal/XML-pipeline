import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for conference ''' 
# Defining Elements
conference = Element('conference')
# Creating the Nodes
G_conference = nx.DiGraph()
conference_node = Node(element=conference, graph=G_conference)

first_node = node.get_first_node()
last_node = node.get_last_node()

G_conference.add_nodes_from([first_node, last_node, conf_date_node, conf_name_node, conf_acronym_node, conf_num_node, conf_loc_node, conf_sponsor_node, conf_theme_node])
G_conference.add_edge(first_node, conf_date_node)
G_conference.add_edge(conf_date_node, conf_name_node)
G_conference.add_edge(conf_date_node, conf_acronym_node)
G_conference.add_edge(conf_name_node, conf_name_node)
G_conference.add_edge(conf_name_node, conf_acronym_node)
G_conference.add_edge(conf_acronym_node, conf_name_node)
G_conference.add_edge(conf_acronym_node, conf_acronym_node)
G_conference.add_edge(conf_name_node, conf_num_node)
G_conference.add_edge(conf_name_node, conf_loc_node)
G_conference.add_edge(conf_name_node, conf_sponsor_node)
G_conference.add_edge(conf_name_node, conf_theme_node)
G_conference.add_edge(conf_name_node, last_node)
G_conference.add_edge(conf_acronym_node, conf_num_node)
G_conference.add_edge(conf_acronym_node, conf_loc_node)
G_conference.add_edge(conf_acronym_node, conf_sponsor_node)
G_conference.add_edge(conf_acronym_node, conf_theme_node)
G_conference.add_edge(conf_acronym_node, last_node)
G_conference.add_edge(conf_num_node, conf_loc_node)
G_conference.add_edge(conf_num_node, conf_sponsor_node)
G_conference.add_edge(conf_num_node, conf_theme_node)
G_conference.add_edge(conf_num_node, last_node)
G_conference.add_edge(conf_loc_node, conf_sponsor_node)
G_conference.add_edge(conf_loc_node, conf_theme_node)
G_conference.add_edge(conf_loc_node, last_node)
G_conference.add_edge(conf_sponsor_node, conf_sponsor_node)
G_conference.add_edge(conf_sponsor_node, conf_theme_node)
G_conference.add_edge(conf_sponsor_node, last_node)
G_conference.add_edge(conf_theme_node, last_node)
