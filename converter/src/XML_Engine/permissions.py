import networkx as nx

class Permissions:
    def __init__(self):
        self.name = 'permissions' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('copyright-statement')
        G.add_node('copyright-year')
        G.add_node('copyright-holder')
        G.add_node('ali:free_to_read')
        G.add_node('license')
        #adding edges
        G.add_edge('start', 'copyright-statement')
        G.add_edge('start', 'accept')
        G.add_edge('copyright-statement', 'copyright-statement')
        G.add_edge('copyright-statement', 'copyright-year')
        G.add_edge('copyright-statement', 'copyright-holder')
        G.add_edge('copyright-statement', 'accept')
        G.add_edge('copyright-statement', 'ali:free_to_read')
        G.add_edge('copyright-statement', 'license')
        G.add_edge('copyright-year', 'copyright-year')
        G.add_edge('copyright-year', 'copyright-holder')
        G.add_edge('copyright-year', 'accept')
        G.add_edge('copyright-year', 'ali:free_to_read')
        G.add_edge('copyright-year', 'license')
        G.add_edge('copyright-holder', 'copyright-holder')
        G.add_edge('copyright-holder', 'accept')
        G.add_edge('copyright-holder', 'ali:free_to_read')
        G.add_edge('copyright-holder', 'license')
        G.add_edge('ali:free_to_read', 'accept')
        G.add_edge('license', 'accept')
        return G