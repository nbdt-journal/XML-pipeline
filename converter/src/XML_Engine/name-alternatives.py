import networkx as nx

class Name_alternatives:
    def __init__(self):
        self.name = 'name-alternatives' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('name')
        G.add_node('string-name')
        #adding edges
        G.add_edge('start', 'name')
        G.add_edge('start', 'string-name')
        G.add_edge('start', 'accept')
        G.add_edge('name', 'accept')
        G.add_edge('string-name', 'accept')
        return G