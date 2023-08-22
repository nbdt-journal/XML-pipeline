import networkx as nx

class Funding_group:
    def __init__(self):
        self.name = 'funding-group' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('award-group')
        G.add_node('funding-statement')
        G.add_node('open-access')
        #adding edges
        G.add_edge('start', 'award-group')
        G.add_edge('award-group', 'award-group')
        G.add_edge('award-group', 'funding-statement')
        G.add_edge('award-group', 'open-access')
        G.add_edge('award-group', 'accept')
        G.add_edge('funding-statement', 'funding-statement')
        G.add_edge('funding-statement', 'open-access')
        G.add_edge('funding-statement', 'accept')
        G.add_edge('open-access', 'open-access')
        G.add_edge('open-access', 'accept')
        return G