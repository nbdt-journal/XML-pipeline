import networkx as nx

class Note:
    def __init__(self):
        self.name = 'note' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('label')
        G.add_node('p')
        G.add_node('product')
        #adding edges
        G.add_edge('start', 'label')
        G.add_edge('start', 'accept')
        G.add_edge('label', 'p')
        G.add_edge('label', 'product')
        G.add_edge('label', 'accept')
        G.add_edge('p', 'accept')
        G.add_edge('product', 'accept')
        return G