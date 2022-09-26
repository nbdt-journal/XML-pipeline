import networkx as nx 

import node
from node import Node 
from element import Element 

from journal_id_graph import journal_id_node
from journal_title_group_graph import journal_title_group_node 
from contrib_group_graph import contrib_group_node 
from aff_graph import aff_node 
from aff_alternatives_graph import aff_alternatives_node
from issn_graph import issn_node
from issn_l_graph import issn_l_node
from isbn_graph import isbn_node
from publisher_graph import publisher_node
from notes_graph import notes_node
from self_uri_graph import self_uri_node

''' Building a graph for Journal-Meta ''' 
# Defining Elements
journal_meta = Element('journal-meta')
# Creating the Graph
G_journal_meta = nx.DiGraph()
# creating the first and last node
first_node = node.get_first_node()
last_node = node.get_last_node()
# adding the nodes
G_journal_meta.add_node(first_node)
G_journal_meta.add_node(journal_id_node)
G_journal_meta.add_node(journal_title_group_node)
G_journal_meta.add_node(contrib_group_node)
G_journal_meta.add_node(aff_node)
G_journal_meta.add_node(aff_alternatives_node)
G_journal_meta.add_node(issn_node)
G_journal_meta.add_node(issn_l_node)
G_journal_meta.add_node(isbn_node)
G_journal_meta.add_node(publisher_node)
G_journal_meta.add_node(notes_node)
G_journal_meta.add_node(self_uri_node)
G_journal_meta.add_node(last_node)
# adding the edges
G_journal_meta.add_edge(first_node, journal_id_node)
G_journal_meta.add_edge(journal_id_node, journal_id_node)
G_journal_meta.add_edge(journal_id_node, journal_title_group_node)
G_journal_meta.add_edge(journal_id_node, contrib_group_node)
G_journal_meta.add_edge(journal_id_node, aff_node)
G_journal_meta.add_edge(journal_id_node, aff_alternatives_node)
G_journal_meta.add_edge(journal_id_node, issn_node)
G_journal_meta.add_edge(contrib_group_node, contrib_group_node)
G_journal_meta.add_edge(contrib_group_node, aff_node)
G_journal_meta.add_edge(contrib_group_node, aff_alternatives_node)
G_journal_meta.add_edge(contrib_group_node, issn_node)
G_journal_meta.add_edge(aff_node, contrib_group_node)
G_journal_meta.add_edge(aff_node, aff_node)
G_journal_meta.add_edge(aff_node, aff_alternatives_node)
G_journal_meta.add_edge(aff_node, issn_node)
G_journal_meta.add_edge(aff_alternatives_node, contrib_group_node)
G_journal_meta.add_edge(aff_alternatives_node, aff_node)
G_journal_meta.add_edge(aff_alternatives_node, aff_alternatives_node)
G_journal_meta.add_edge(aff_alternatives_node, issn_node)
G_journal_meta.add_edge(issn_node, issn_node)
G_journal_meta.add_edge(issn_node, issn_l_node)
G_journal_meta.add_edge(issn_node, isbn_node)
G_journal_meta.add_edge(issn_node, publisher_node)
G_journal_meta.add_edge(issn_node, notes_node)
G_journal_meta.add_edge(issn_node, self_uri_node)
G_journal_meta.add_edge(issn_node, last_node)
G_journal_meta.add_edge(issn_l_node, isbn_node)
G_journal_meta.add_edge(issn_l_node, publisher_node)
G_journal_meta.add_edge(issn_l_node, notes_node)
G_journal_meta.add_edge(issn_l_node, self_uri_node)
G_journal_meta.add_edge(issn_l_node, last_node)
G_journal_meta.add_edge(isbn_node, isbn_node)
G_journal_meta.add_edge(isbn_node, publisher_node)
G_journal_meta.add_edge(isbn_node, notes_node)
G_journal_meta.add_edge(isbn_node, self_uri_node)
G_journal_meta.add_edge(isbn_node, last_node)
G_journal_meta.add_edge(publisher_node, notes_node)
G_journal_meta.add_edge(publisher_node, self_uri_node)
G_journal_meta.add_edge(publisher_node, last_node)
G_journal_meta.add_edge(notes_node, notes_node)
G_journal_meta.add_edge(notes_node, self_uri_node)
G_journal_meta.add_edge(notes_node, last_node)
G_journal_meta.add_edge(self_uri_node, self_uri_node)
G_journal_meta.add_edge(self_uri_node, last_node)
# defining the node
journal_meta_node = Node(element=journal_meta, graph=G_journal_meta)

if __name__ == '__main__':
    import xml.etree.ElementTree as ET
    tree = ET.parse('test_samples/journal_meta.xml')
    root = tree.getroot()
    print(journal_meta_node.check(root))