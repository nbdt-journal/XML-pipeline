import networkx as nx

class Subj_group:
    def __init__(self):
        self.name = 'subj-group' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('subj-group')
        G.add_node('subject')
        G.add_node('compound-subject')
        #adding edges
        G.add_edge('start', 'subject')
        G.add_edge('start', 'compound-subject')
        G.add_edge('start', 'accept')
        G.add_edge('start', 'subj-group')
        G.add_edge('subj-group', 'subj-group')
        G.add_edge('subj-group', 'accept')
        G.add_edge('subject', 'subj-group')
        G.add_edge('subject', 'accept')
        G.add_edge('compound-subject', 'subj-group')
        G.add_edge('compound-subject', 'accept')
        return G