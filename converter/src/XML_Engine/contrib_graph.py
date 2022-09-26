import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Contrib ''' 
# Defining Elements
contrib = Element('contrib')
# Creating the Nodes
G_contrib = nx.DiGraph()
group_1 = [anonymous_node, collab_node, collab_node, collab_alternatives_node, name_node, name_alternatives_node, string_name_node]
group_2 = [address_node, aff_node, aff_alternatives_node, author_comment_node, bio_node, email_node, ext_link_node, on_behalf_of_node, role_node, uri_node, xref_node]
G_contrib.add_nodes_from([node.get_first_node(), node.get_last_node(), contrib_id_node, degrees_node])
G_contrib.add_nodes_from(group_1)
G_contrib.add_nodes_from(group_2)
contrib_node = Node(element=contrib, graph=G_contrib)

for i in list(G_contrib.nodes):
    for j in list(G_contrib.nodes):
        if i.element.name == 'first' or i.element.name == 'contrib-id':
            if j.element.name != 'first':
                G_contrib.add_edge(i, j)
        if i in group_1:
            if j.element.name not in ['first', 'contrib-id']:
                G_contrib.add_edge(i, j)
        if i in group_2:
            if j.element.name not in ['first', 'contrib-id']:
                if j not in group_1:
                    G_contrib.add_edge(i, j)
        