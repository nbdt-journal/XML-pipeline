import networkx as nx

class List_item:
    def __init__(self):
        self.name = 'list-item' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('label')
        G.add_node('title')
        G.add_node('p')
        G.add_node('def-list')
        G.add_node('list')
        #adding edges
        G.add_edge('start', 'label')
        G.add_edge('start', 'accept')
        G.add_edge('label', 'title')
        G.add_edge('label', 'p')
        G.add_edge('label', 'def-list')
        G.add_edge('label', 'list')
        G.add_edge('label', 'accept')
        G.add_edge('title', 'p')
        G.add_edge('title', 'def-list')
        G.add_edge('title', 'list')
        G.add_edge('title', 'accept')
        G.add_edge('p', 'accept')
        G.add_edge('def-list', 'accept')
        G.add_edge('list', 'accept')
        return G