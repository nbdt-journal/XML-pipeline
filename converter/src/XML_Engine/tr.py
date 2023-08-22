import networkx as nx

class Tr:
    def __init__(self):
        self.name = 'tr' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('th')
        G.add_node('td')
        #adding edges
        G.add_edge('start', 'th')
        G.add_edge('start', 'td')
        G.add_edge('start', 'accept')
        G.add_edge('th', 'accept')
        G.add_edge('td', 'accept')
        return G