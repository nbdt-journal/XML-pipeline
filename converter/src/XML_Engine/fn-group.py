import networkx as nx

class Fn_group:
    def __init__(self):
        self.name = 'fn-group' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('label')
        G.add_node('title')
        G.add_node('fn')
        G.add_node('x')
        #adding edges
        G.add_edge('start', 'label')
        G.add_edge('start', 'accept')
        G.add_edge('label', 'title')
        G.add_edge('label', 'fn')
        G.add_edge('label', 'x')
        G.add_edge('label', 'accept')
        G.add_edge('title', 'fn')
        G.add_edge('title', 'x')
        G.add_edge('title', 'accept')
        G.add_edge('fn', 'accept')
        G.add_edge('x', 'accept')
        return G