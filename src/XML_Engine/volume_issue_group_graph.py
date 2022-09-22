import networkx as nx 

import node
from node import Node 
from element import Element 

''' Building a graph for Volume Issue Group ''' 
# Defining Elements
volume_issue_group = Element('volume-issue-group')
G_volume_issue_group = nx.DiGraph()
first_node = node.get_first_node()
last_node = node.get_last_node()
G_volume_issue_group.add_nodes_from([first_node, last_node, volume_node, volume_id_node, volume_series_node, issue_node, issue_id_node, issue_title_node, issue_title_group_node, issue_sponsor_node, issue_part_node])

exclusion_arr = ['first']
for i in list(G_volume_issue_group.nodes):
    for j in list(G_volume_issue_group.nodes):
        if i.element.name == 'first':
            if j.element.name not in exclusion_arr: 
                G_volume_issue_group.add_edge(i, j)
        if i.element.name == 'volume':
            if j.element.name not in exclusion_arr:
                G_volume_issue_group.add_edge(i, j)
                exclusion_arr.append(i.element.name)
        if i.element.name == 'volume-id':
            if j.element.name not in exclusion_arr:
                G_volume_issue_group.add_edge(i, j)
                exclusion_arr.append(i.element.name)
        if i.element.name == 'volume-series':
            exclusion_arr.append(i.element.name)
            if j.element.name not in exclusion_arr:
                G_volume_issue_group.add_edge(i, j)
        if i.element.name == 'issue':
            if j.element.name not in exclusion_arr:
                G_volume_issue_group.add_edge(i, j)
                exclusion_arr.append(i.element.name)
        if i.element.name == 'issue-id':
            if j.element.name not in exclusion_arr:
                G_volume_issue_group.add_edge(i, j)
                exclusion_arr.append(i.element.name)
        if i.element.name == 'issue-title':
            if j.element.name not in exclusion_arr:
                G_volume_issue_group.add_edge(i, j)
                exclusion_arr.append(i.element.name)
        if i.element.name == 'issue-title-group':
            if j.element.name not in exclusion_arr:
                G_volume_issue_group.add_edge(i, j)
                exclusion_arr.append(i.element.name)
        if i.element.name == 'issue-sponsor':
            if j.element.name not in exclusion_arr:
                G_volume_issue_group.add_edge(i, j)
                exclusion_arr.append(i.element.name)
        if i.element.name == 'issue-part':
            if j.element.name == 'last':
                G_volume_issue_group.add_edge(i, j)

# Creating the Nodes
volume_issue_group_node = Node(element=volume_issue_group, graph=G_volume_issue_group)