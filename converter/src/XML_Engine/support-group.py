import networkx as nx

class Support_group:
    def __init__(self):
        self.name = 'support-group' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('funding-group')
        G.add_node('contributed-resource-group')
        #adding edges
        G.add_edge('start', 'funding-group')
        G.add_edge('funding-group', 'funding-group')
        G.add_edge('funding-group', 'contributed-resource-group')
        G.add_edge('funding-group', 'accept')
        G.add_edge('contributed-resource-group', 'contributed-resource-group')
        G.add_edge('contributed-resource-group', 'accept')
        return G