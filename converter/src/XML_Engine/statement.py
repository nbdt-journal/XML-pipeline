import networkx as nx

class Statement:
    def __init__(self):
        self.name = 'statement' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('label')
        G.add_node('title')
        G.add_node('p')
        G.add_node('statement')
        G.add_node('subj-group')
        G.add_node('kwd-group')
        G.add_node('abstract')
        G.add_node('attrib')
        G.add_node('permissions')
        #adding edges
        G.add_edge('start', 'label')
        G.add_edge('start', 'accept')
        G.add_edge('start', 'attrib')
        G.add_edge('start', 'permissions')
        G.add_edge('label', 'title')
        G.add_edge('label', 'p')
        G.add_edge('label', 'statement')
        G.add_edge('label', 'accept')
        G.add_edge('label', 'subj-group')
        G.add_edge('label', 'kwd-group')
        G.add_edge('label', 'abstract')
        G.add_edge('title', 'p')
        G.add_edge('title', 'statement')
        G.add_edge('title', 'accept')
        G.add_edge('title', 'subj-group')
        G.add_edge('title', 'kwd-group')
        G.add_edge('title', 'abstract')
        G.add_edge('p', 'accept')
        G.add_edge('p', 'attrib')
        G.add_edge('p', 'permissions')
        G.add_edge('statement', 'accept')
        G.add_edge('statement', 'attrib')
        G.add_edge('statement', 'permissions')
        G.add_edge('subj-group', 'p')
        G.add_edge('subj-group', 'statement')
        G.add_edge('subj-group', 'accept')
        G.add_edge('kwd-group', 'p')
        G.add_edge('kwd-group', 'statement')
        G.add_edge('kwd-group', 'accept')
        G.add_edge('kwd-group', 'subj-group')
        G.add_edge('abstract', 'p')
        G.add_edge('abstract', 'statement')
        G.add_edge('abstract', 'accept')
        G.add_edge('abstract', 'subj-group')
        G.add_edge('abstract', 'kwd-group')
        G.add_edge('attrib', 'accept')
        G.add_edge('permissions', 'accept')
        return G