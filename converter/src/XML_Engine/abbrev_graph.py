import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for abbrev ''' 
# Defining Elements
abbrev = Element('abbrev')
abbrev = nx.DiGraph()
abbrev.add_nodes_from([node.get_first_node(), node.get_last_node(), def_node])
for i in list(abbrev.nodes):
    for j in list(abbrev.nodes):
        if i.element.name == 'last':
            break 
        if i.element.name == j.element.name:
            continue 
        if j.element.name == 'first':
            continue 
        abbrev.add_edge(i, j)

abbrev_node = Node(element=abbrev, graph=abbrev)