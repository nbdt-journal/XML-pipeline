import networkx as nx

class Name:
    def __init__(self):
        self.name = 'name' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('prefix')
        G.add_node('suffix')
        G.add_node('given-names')
        G.add_node('surname')
        #adding edges
        G.add_edge('start', 'given-names')
        G.add_edge('start', 'accept')
        G.add_edge('start', 'prefix')
        G.add_edge('start', 'suffix')
        G.add_edge('start', 'surname')
        G.add_edge('prefix', 'suffix')
        G.add_edge('prefix', 'accept')
        G.add_edge('given-names', 'prefix')
        G.add_edge('given-names', 'suffix')
        G.add_edge('given-names', 'accept')
        G.add_edge('surname', 'prefix')
        G.add_edge('surname', 'suffix')
        G.add_edge('surname', 'accept')
        return G