import networkx as nx

class Def_list:
    def __init__(self):
        self.name = 'def-list' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('label')
        G.add_node('title')
        G.add_node('term-head')
        G.add_node('def-head')
        G.add_node('def-item')
        G.add_node('x')
        G.add_node('def-list')
        #adding edges
        G.add_edge('start', 'label')
        G.add_edge('start', 'accept')
        G.add_edge('start', 'def-list')
        G.add_edge('label', 'title')
        G.add_edge('label', 'term-head')
        G.add_edge('label', 'def-head')
        G.add_edge('label', 'accept')
        G.add_edge('label', 'def-item')
        G.add_edge('label', 'x')
        G.add_edge('label', 'def-list')
        G.add_edge('title', 'term-head')
        G.add_edge('title', 'def-head')
        G.add_edge('title', 'accept')
        G.add_edge('title', 'def-item')
        G.add_edge('title', 'x')
        G.add_edge('title', 'def-list')
        G.add_edge('term-head', 'def-head')
        G.add_edge('term-head', 'accept')
        G.add_edge('term-head', 'def-item')
        G.add_edge('term-head', 'x')
        G.add_edge('term-head', 'def-list')
        G.add_edge('def-head', 'accept')
        G.add_edge('def-head', 'def-item')
        G.add_edge('def-head', 'x')
        G.add_edge('def-head', 'def-list')
        G.add_edge('def-item', 'accept')
        G.add_edge('def-item', 'def-list')
        G.add_edge('x', 'accept')
        G.add_edge('x', 'def-list')
        G.add_edge('def-list', 'accept')
        return G