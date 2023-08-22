import networkx as nx

class Journal_title_group:
    def __init__(self):
        self.name = 'journal-title-group' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('journal-title')
        G.add_node('journal-subtitle')
        G.add_node('trans-title-group')
        G.add_node('abbrev-journal-title')
        #adding edges
        G.add_edge('start', 'journal-title')
        G.add_edge('journal-title', 'journal-title')
        G.add_edge('journal-title', 'journal-subtitle')
        G.add_edge('journal-title', 'trans-title-group')
        G.add_edge('journal-title', 'abbrev-journal-title')
        G.add_edge('journal-title', 'accept')
        G.add_edge('journal-subtitle', 'journal-subtitle')
        G.add_edge('journal-subtitle', 'trans-title-group')
        G.add_edge('journal-subtitle', 'abbrev-journal-title')
        G.add_edge('journal-subtitle', 'accept')
        G.add_edge('trans-title-group', 'trans-title-group')
        G.add_edge('trans-title-group', 'abbrev-journal-title')
        G.add_edge('trans-title-group', 'accept')
        G.add_edge('abbrev-journal-title', 'abbrev-journal-title')
        G.add_edge('abbrev-journal-title', 'accept')
        return G