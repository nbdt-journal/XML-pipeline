import networkx as nx

class Principal_award_recipient:
    def __init__(self):
        self.name = 'principal-award-recipient' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('#PCDATA')
        G.add_node('contrib-id')
        G.add_node('name')
        G.add_node('name-alternatives')
        G.add_node('institution')
        G.add_node('institution-wrap')
        G.add_node('string-name')
        #adding edges
        G.add_edge('start', '#PCDATA')
        G.add_edge('start', 'contrib-id')
        G.add_edge('start', 'name')
        G.add_edge('start', 'name-alternatives')
        G.add_edge('start', 'institution')
        G.add_edge('start', 'institution-wrap')
        G.add_edge('start', 'string-name')
        G.add_edge('start', 'accept')
        G.add_edge('#PCDATA', 'accept')
        G.add_edge('contrib-id', 'accept')
        G.add_edge('name', 'accept')
        G.add_edge('name-alternatives', 'accept')
        G.add_edge('institution', 'accept')
        G.add_edge('institution-wrap', 'accept')
        G.add_edge('string-name', 'accept')
        return G