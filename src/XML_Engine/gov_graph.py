import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for gov ''' 
# Defining Elements
gov = Element('gov')
G_gov = nx.DiGraph()
G_gov.add_nodes_from([node.get_first_node(), node.get_last_node(), bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, sub_node, sup_node, named_content_node, styled_content_node])
for i in list(G_gov.nodes):
    for j in list(G_gov.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_gov.add_edge(i, j)

# Creating the Nodes
gov_node = Node(element=gov, graph=G_gov)
