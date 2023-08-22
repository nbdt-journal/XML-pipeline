import networkx as nx

class Def_item:
    def __init__(self):
        self.name = 'def-item' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('label')
        G.add_node('term')
        G.add_node('def')
        G.add_node('x')
        #adding edges
        G.add_edge('start', 'label')
        G.add_edge('start', 'accept')
        G.add_edge('label', 'term')
        G.add_edge('label', 'accept')
        G.add_edge('label', 'def')
        G.add_edge('label', 'x')
        G.add_edge('term', 'term')
        G.add_edge('term', 'accept')
        G.add_edge('term', 'def')
        G.add_edge('term', 'x')
        G.add_edge('def', 'accept')
        G.add_edge('x', 'accept')
        return G