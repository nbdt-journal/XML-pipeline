import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for price ''' 
# Defining Elements
price = Element('price')
G_price = nx.DiGraph()
G_price.add_nodes_from([node.get_first_node(), node.get_last_node(), bold_node, fixed_case_node, italic_node, monospace_node, overline_node, roman_node, sans_serif_node, sc_node, strike_node, underline_node, ruby_node])

for i in list(G_price.nodes):
    for j in list(G_price.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_price.add_edge(i, j)
# Creating the Nodes
price_node = Node(element=price, graph=G_price)
