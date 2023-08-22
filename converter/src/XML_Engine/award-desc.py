import networkx as nx

class Award_desc:
    def __init__(self):
        self.name = 'award-desc' 
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