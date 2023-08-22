import networkx as nx

class Compound_kwd:
    def __init__(self):
        self.name = 'compound-kwd' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('compound-kwd-part')
        #adding edges
        G.add_edge('start', 'compound-kwd-part')
        G.add_edge('compound-kwd-part', 'compound-kwd-part')
        G.add_edge('compound-kwd-part', 'accept')
        return G