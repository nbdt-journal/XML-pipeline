import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for counts ''' 
# Defining Elements
counts = Element('counts')
G_counts = nx.DiGraph()
# Creating the Nodes
counts_node = Node(element=counts, graph=G_counts)

G_counts.add_nodes_from([node.get_first_node(), node.get_last_node(), count_node, fig_count_node, table_count_node, equation_count_node, ref_count_node, page_count_node, word_count_node])

exclude_list = ['first', 'count', 'fig-count']

for i in list(G_counts):
    for j in list(G_counts):
        if i.element.name in ['first', 'count']:
            if j.element.name != 'first':
                G_counts.add_edge(i, j)
        if i.element.name not in ['first', 'count', 'last']:
            if j.element.name not in exclude_list:
                G_counts.add_edge(i, j)
    exclude_list.append(i.element.name)