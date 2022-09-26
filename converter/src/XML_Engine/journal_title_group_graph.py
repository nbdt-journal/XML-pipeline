import networkx as nx 

import node
from node import Node 
from element import Element 

from journal_title_graph import journal_title_node
from journal_subtitle_graph import journal_subtitle_node
from trans_title_group_graph import trans_title_group_node 
from abbrev_journal_title_graph import abbrev_journal_title_node

''' Building a graph for Journal Title Group ''' 
# Defining Elements
journal_title_group = Element('journal-title-group')
# Defining the Graph
G_journal_title_group = nx.DiGraph()
# creating the first and last node
first_node = node.get_first_node()
last_node = node.get_last_node()
# adding the first node
G_journal_title_group.add_node(first_node)
# adding the elements
G_journal_title_group.add_node(journal_title_node)
G_journal_title_group.add_node(journal_subtitle_node)
G_journal_title_group.add_node(trans_title_group_node)
G_journal_title_group.add_node(abbrev_journal_title_node)
# adding the last node
G_journal_title_group.add_node(last_node)
# adding the edges
G_journal_title_group.add_edge(first_node, journal_title_node)
G_journal_title_group.add_edge(first_node, journal_subtitle_node)
G_journal_title_group.add_edge(first_node, trans_title_group_node)
G_journal_title_group.add_edge(first_node, abbrev_journal_title_node)
G_journal_title_group.add_edge(first_node, last_node)
G_journal_title_group.add_edge(journal_title_node, journal_title_node)
G_journal_title_group.add_edge(journal_title_node, journal_subtitle_node)
G_journal_title_group.add_edge(journal_title_node, trans_title_group_node)
G_journal_title_group.add_edge(journal_title_node, abbrev_journal_title_node)
G_journal_title_group.add_edge(journal_title_node, last_node)
G_journal_title_group.add_edge(journal_subtitle_node, journal_subtitle_node)
G_journal_title_group.add_edge(journal_subtitle_node, trans_title_group_node)
G_journal_title_group.add_edge(journal_subtitle_node, abbrev_journal_title_node)
G_journal_title_group.add_edge(journal_subtitle_node, last_node)
G_journal_title_group.add_edge(trans_title_group_node, trans_title_group_node)
G_journal_title_group.add_edge(trans_title_group_node, abbrev_journal_title_node)
G_journal_title_group.add_edge(trans_title_group_node, last_node)
G_journal_title_group.add_edge(abbrev_journal_title_node, abbrev_journal_title_node)
G_journal_title_group.add_edge(abbrev_journal_title_node, last_node)
# Defining the trans-title-group node
journal_title_group_node = Node(element=journal_title_group, graph=G_journal_title_group)

if __name__ == '__main__':
    import xml.etree.ElementTree as ET
    tree = ET.parse('test_samples/journal_title_group.xml')
    root = tree.getroot()
    print(journal_title_group_node.check(root))