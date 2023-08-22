import networkx as nx

class Date:
    def __init__(self):
        self.name = 'date' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('year')
        G.add_node('era')
        G.add_node('string-date')
        G.add_node('season')
        G.add_node('day')
        #adding edges
        G.add_edge('start', 'season')
        G.add_edge('start', 'accept')
        G.add_edge('start', 'year')
        G.add_edge('start', 'era')
        G.add_edge('start', 'string-date')
        G.add_edge('start', 'day')
        G.add_edge('year', 'era')
        G.add_edge('year', 'string-date')
        G.add_edge('year', 'accept')
        G.add_edge('era', 'string-date')
        G.add_edge('era', 'accept')
        G.add_edge('season', 'year')
        G.add_edge('season', 'era')
        G.add_edge('season', 'string-date')
        G.add_edge('season', 'accept')
        G.add_edge('day', 'year')
        G.add_edge('day', 'era')
        G.add_edge('day', 'string-date')
        G.add_edge('day', 'accept')
        return G