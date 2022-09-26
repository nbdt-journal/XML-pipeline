import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for date-in-citation ''' 
# Defining Elements
date_in_citation = Element('date-in-citation')
# Creating the Nodes
G_date_in_citation = nx.DiGraph()
G_date_in_citation.add_nodes_from([node.get_first_node(), node.get_last_node(), day_node, era_node, month_node, season_node, year_node])



date_in_citation_node = Node(element=date_in_citation, graph=G_date_in_citation)

for i in list(G_date_in_citation.nodes):
    for j in list(G_date_in_citation.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_date_in_citation.add_edge(i, j)

