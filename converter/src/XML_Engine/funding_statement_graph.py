import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for funding-statement ''' 
# Defining Elements
dfunding_statement = Element('funding-statement')
G_dfunding_statement = nx.DiGraph()
G_dfunding_statement.add_nodes_from([node.get_first_node(), node.get_last_node(), email_node, ext_link_node, uri_node, bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, named_content_node, styled_content_node, sub_node, sup_node])
for i in list(G_dfunding_statement.nodes):
    for j in list(G_dfunding_statement.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_dfunding_statement.add_edge(i, j)

# Creating the Nodes
dfunding_statement_node = Node(element=dfunding_statement, graph=G_dfunding_statement)
