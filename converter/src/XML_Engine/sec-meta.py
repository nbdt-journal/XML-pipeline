import networkx as nx

class Sec_meta:
    def __init__(self):
        self.name = 'sec-meta' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('permissions')
        G.add_node('kwd-group')
        G.add_node('abstract')
        G.add_node('contrib-group')
        G.add_node('object-id')
        G.add_node('subj-group')
        #adding edges
        G.add_edge('start', 'object-id')
        G.add_edge('kwd-group', 'permissions')
        G.add_edge('kwd-group', 'accept')
        G.add_edge('kwd-group', 'subj-group')
        G.add_edge('abstract', 'permissions')
        G.add_edge('abstract', 'accept')
        G.add_edge('abstract', 'kwd-group')
        G.add_edge('abstract', 'subj-group')
        G.add_edge('contrib-group', 'permissions')
        G.add_edge('contrib-group', 'accept')
        G.add_edge('contrib-group', 'kwd-group')
        G.add_edge('contrib-group', 'abstract')
        G.add_edge('contrib-group', 'subj-group')
        G.add_edge('object-id', 'permissions')
        G.add_edge('object-id', 'accept')
        G.add_edge('object-id', 'kwd-group')
        G.add_edge('object-id', 'abstract')
        G.add_edge('object-id', 'contrib-group')
        G.add_edge('object-id', 'subj-group')
        G.add_edge('subj-group', 'permissions')
        G.add_edge('subj-group', 'accept')
        return G