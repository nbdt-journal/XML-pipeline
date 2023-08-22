import networkx as nx

class Copyright_holder:
    def __init__(self):
        self.name = 'copyright-holder' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('#PCDATA')
        G.add_node('institution')
        G.add_node('institution-wrap')
        G.add_node('sub')
        G.add_node('sup')
        G.add_node('x')
        #adding edges
        G.add_edge('start', '#PCDATA')
        G.add_edge('start', 'institution')
        G.add_edge('start', 'institution-wrap')
        G.add_edge('start', 'sub')
        G.add_edge('start', 'sup')
        G.add_edge('start', 'x')
        G.add_edge('start', 'accept')
        G.add_edge('#PCDATA', 'accept')
        G.add_edge('institution', 'accept')
        G.add_edge('institution-wrap', 'accept')
        G.add_edge('sub', 'accept')
        G.add_edge('sup', 'accept')
        G.add_edge('x', 'accept')
        return G