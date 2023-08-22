import networkx as nx

class Table:
    def __init__(self):
        self.name = 'table' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('thead')
        G.add_node('tbody')
        G.add_node('col')
        G.add_node('colgroup')
        G.add_node('tr')
        #adding edges
        G.add_edge('start', 'accept')
        G.add_edge('start', 'col')
        G.add_edge('tbody', 'accept')
        G.add_edge('col', 'accept')
        G.add_edge('col', 'thead')
        G.add_edge('col', 'tr')
        G.add_edge('colgroup', 'accept')
        G.add_edge('colgroup', 'thead')
        G.add_edge('colgroup', 'tr')
        G.add_edge('tr', 'accept')
        return G