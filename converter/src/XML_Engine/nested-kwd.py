import networkx as nx

class Nested_kwd:
    def __init__(self):
        self.name = 'nested-kwd' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('nested-kwd')
        G.add_node('kwd')
        G.add_node('compound-kwd')
        #adding edges
        G.add_edge('start', 'kwd')
        G.add_edge('start', 'compound-kwd')
        G.add_edge('start', 'accept')
        G.add_edge('start', 'nested-kwd')
        G.add_edge('nested-kwd', 'nested-kwd')
        G.add_edge('nested-kwd', 'accept')
        G.add_edge('kwd', 'nested-kwd')
        G.add_edge('kwd', 'accept')
        G.add_edge('compound-kwd', 'nested-kwd')
        G.add_edge('compound-kwd', 'accept')
        return G