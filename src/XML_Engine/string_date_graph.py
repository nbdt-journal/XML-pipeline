import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for string-date ''' 
# Defining Elements
string_date = Element('string-date')
G_string_date = nx.DiGraph()
G_string_date.add_nodes_from([node.get_first_node(), node.get_last_node(), day_node, era_node, month_node, season_node, year_node])

for i in list(G_string_date.nodes):
    for j in list(G_string_date.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_string_date.add_edge(i, j)
# Creating the Nodes
string_date_node = Node(element=string_date, graph=G_string_date)
