import networkx as nx

class Era:
    def __init__(self):
        self.name = 'era' 
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