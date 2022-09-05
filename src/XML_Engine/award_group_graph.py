import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for award group ''' 
# Defining Elements
award_group = Element('award-group')
# Creating the Nodes
G_award_group = nx.DiGraph()
award_group_node = Node(element=award_group, graph=award_group)

G_award_group.add_nodes_from([funding_source_node, support_source_node, award_id_node, award_name_node, award_desc_node, principal_award_recipient_node, principal_investigator_node])

for i in list(award_group.nodes):
    for j in list(award_group.nodes):
        if i.element.name == 'first':
            if j.element.name != 'first':
                G_award_group.add_edge(i, j)
        if i.element.name == 'funding-source':
            if j.element.name not in ['first', 'support-source']:
                G_award_group.add_edge(i, j)
        if i.element.name == 'support-source':
            if j.element.name not in ['first', 'funding-source']:
                G_award_group.add_edge(i, j)
        if i.element.name == 'award-id':
            if j.element.name not in ['first', 'support-source', 'funding-source']:
                G_award_group.add_edge(i, j)
        if i.element.name == 'award-name':
            if j.element.name not in ['first', 'support-source', 'funding-source', 'award-id', 'award-name']:
                G_award_group.add_edge(i, j)
        if i.element.name == 'award-desc':
            if j.element.name not in ['first', 'support-source', 'funding-source', 'award-id', 'award-name', 'award-desc']:
                G_award_group.add_edge(i, j)
        if i.element.name == 'principal-award-recipient':
            if j.element.name not in ['first', 'support-source', 'funding-source', 'award-id', 'award-name', 'award-desc']:
                G_award_group.add_edge(i, j)
        if i.element.name == 'principal-investigator':
            if j.element.name in ['principal-investigator', 'last']:
                G_award_group.add_edge(i, j)