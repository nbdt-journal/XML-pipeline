import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for conf-loc ''' 
# Defining Elements
conf_loc = Element('conf-loc')
# Creating the Nodes
G_conf_loc = nx.DiGraph()
G_conf_loc.add_nodes_from([node.get_first_node(), node.get_last_node(), addr_line_node, city_node, country_node, fax_node, institution_node, institution_wrap_node, phone_node, postal_code_node, state_node])




conf_loc_node = Node(element=conf_loc, graph=G_conf_loc)

for i in list(G_conf_loc.nodes):
    for j in list(G_conf_loc.nodes):
        if i.element.name != 'last':
            if j.element.name != 'first':
                G_conf_loc.add_edge(i, j)

