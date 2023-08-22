import networkx as nx

class Kwd_group:
    def __init__(self):
        self.name = 'kwd-group' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('label')
        G.add_node('title')
        G.add_node('kwd')
        G.add_node('compound-kwd')
        G.add_node('nested-kwd')
        G.add_node('x')
        G.add_node('unstructured-kwd-group')
        #adding edges
        G.add_edge('start', 'label')
        G.add_edge('start', 'accept')
        G.add_edge('label', 'title')
        G.add_edge('label', 'kwd')
        G.add_edge('label', 'compound-kwd')
        G.add_edge('label', 'nested-kwd')
        G.add_edge('label', 'x')
        G.add_edge('label', 'accept')
        G.add_edge('title', 'kwd')
        G.add_edge('title', 'compound-kwd')
        G.add_edge('title', 'nested-kwd')
        G.add_edge('title', 'x')
        G.add_edge('title', 'accept')
        G.add_edge('kwd', 'accept')
        G.add_edge('compound-kwd', 'accept')
        G.add_edge('nested-kwd', 'accept')
        G.add_edge('x', 'accept')
        G.add_edge('unstructured-kwd-group', 'accept')
        return G