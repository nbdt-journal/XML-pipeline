import networkx as nx

class Fpage:
    def __init__(self):
        self.name = 'fpage' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('#PCDATA')
        #adding edges
        G.add_edge('start', '#PCDATA')
        G.add_edge('#PCDATA', 'accept')
        return G