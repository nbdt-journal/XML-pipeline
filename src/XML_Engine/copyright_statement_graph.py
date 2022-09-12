import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for copyright-statement ''' 
# Defining Elements
copyright_statement = Element('copyright-statement')
# Creating the Nodes
G_copyright_statement = nx.DiGraph()
G_copyright_statement.add_nodes_from([node.get_first_node(), node.get_last_node(), email_node, ext_link_node, uri_node, bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, named_content_node, styled_content_node, sub_node, sup_node])

copyright_statement_node = Node(element=copyright_statement, graph=G_copyright_statement)

for i in list(G_copyright_statement.nodes):
    for j in list(G_copyright_statement.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_copyright_statement.add_edge(i, j)

