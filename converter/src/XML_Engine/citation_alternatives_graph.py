import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for citation-alternatives ''' 
# Defining Elements
citation_alternatives = Element('citation-alternatives')
# Creating the Nodes
G_citation_alternatives = nx.DiGraph()
citation_alternatives_node = Node(element=citation_alternatives, graph=G_citation_alternatives)

G_citation_alternatives.add_nodes_from([node.get_first_node(), node.get_last_node(), object_id_node, element_citation_node, mixed_citation_node, nlm_citation_node])

for i in list(G_citation_alternatives.nodes):
    for j in list(G_citation_alternatives.nodes):
        if i.element.name == 'first':
            if j.element.name not in ['first', 'last']:
                G_citation_alternatives.add_edge(i, j)
        elif i.element.name == 'object-id':
            if j.element.name not in ['first', 'last']:
                G_citation_alternatives.add_edge(i, j)
        elif i.element.name != 'last':
            if j.element.name not in ['first', 'object-id']:
                G_citation_alternatives.add_edge(i, j)


