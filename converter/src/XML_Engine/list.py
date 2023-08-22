import networkx as nx

class List:
    def __init__(self):
        self.name = 'list' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('label')
        G.add_node('title')
        G.add_node('object-id')
        G.add_node('list-item')
        G.add_node('x')
        #adding edges
        G.add_edge('start', 'object-id')
        G.add_edge('start', 'accept')
        G.add_edge('label', 'title')
        G.add_edge('label', 'list-item')
        G.add_edge('label', 'x')
        G.add_edge('label', 'accept')
        G.add_edge('title', 'list-item')
        G.add_edge('title', 'x')
        G.add_edge('title', 'accept')
        G.add_edge('object-id', 'label')
        G.add_edge('object-id', 'title')
        G.add_edge('object-id', 'list-item')
        G.add_edge('object-id', 'x')
        G.add_edge('object-id', 'accept')
        G.add_edge('list-item', 'accept')
        G.add_edge('x', 'accept')
        return G