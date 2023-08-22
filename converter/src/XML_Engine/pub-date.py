import networkx as nx

class Pub_date:
    def __init__(self):
        self.name = 'pub-date' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('day')
        G.add_node('era')
        G.add_node('month')
        G.add_node('season')
        G.add_node('year')
        G.add_node('string-date')
        G.add_node('x')
        #adding edges
        G.add_edge('start', 'day')
        G.add_edge('start', 'era')
        G.add_edge('start', 'month')
        G.add_edge('start', 'season')
        G.add_edge('start', 'year')
        G.add_edge('start', 'string-date')
        G.add_edge('start', 'x')
        G.add_edge('start', 'accept')
        G.add_edge('day', 'accept')
        G.add_edge('era', 'accept')
        G.add_edge('month', 'accept')
        G.add_edge('season', 'accept')
        G.add_edge('year', 'accept')
        G.add_edge('string-date', 'accept')
        G.add_edge('x', 'accept')
        return G