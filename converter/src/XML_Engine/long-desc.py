import networkx as nx

class Long_desc:
    def __init__(self):
        self.name = 'long-desc' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('#PCDATA')
        G.add_node('x')
        #adding edges
        G.add_edge('start', '#PCDATA')
        G.add_edge('start', 'x')
        G.add_edge('start', 'accept')
        G.add_edge('#PCDATA', 'accept')
        G.add_edge('x', 'accept')
        return G