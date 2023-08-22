import networkx as nx

class Conference:
    def __init__(self):
        self.name = 'conference' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('conf-date')
        G.add_node('conf-name')
        G.add_node('conf-num')
        G.add_node('conf-loc')
        G.add_node('conf-sponsor')
        G.add_node('conf-theme')
        G.add_node('conf-acronym')
        G.add_node('string-conf')
        G.add_node('x')
        #adding edges
        G.add_edge('start', 'conf-date')
        G.add_edge('start', 'conf-name')
        G.add_edge('start', 'conf-num')
        G.add_edge('start', 'conf-loc')
        G.add_edge('start', 'conf-sponsor')
        G.add_edge('start', 'conf-theme')
        G.add_edge('start', 'conf-acronym')
        G.add_edge('start', 'string-conf')
        G.add_edge('start', 'x')
        G.add_edge('start', 'accept')
        G.add_edge('conf-date', 'accept')
        G.add_edge('conf-name', 'accept')
        G.add_edge('conf-num', 'accept')
        G.add_edge('conf-loc', 'accept')
        G.add_edge('conf-sponsor', 'accept')
        G.add_edge('conf-theme', 'accept')
        G.add_edge('conf-acronym', 'accept')
        G.add_edge('string-conf', 'accept')
        G.add_edge('x', 'accept')
        return G