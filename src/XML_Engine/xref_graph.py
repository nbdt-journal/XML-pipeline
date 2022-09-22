import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for xref ''' 
# Defining Elements
xref = Element('xref')
G_xref = nx.DiGraph()
G_xref.add_nodes_from([node.get_first_node(), node.get_last_node(), bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node, named_content_node, styled_content_node, sub_node, sup_node])
for i in list(G_xref.nodes):
    for j in list(G_xref.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_xref.add_edge(i, j)

# Creating the Nodes
xref_node = Node(element=xref, graph=G_xref)