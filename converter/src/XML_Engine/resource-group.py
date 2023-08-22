import networkx as nx

class Resource_group:
    def __init__(self):
        self.name = 'resource-group' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('resource-name')
        G.add_node('resource-wrap')
        #adding edges
        G.add_edge('start', 'resource-name')
        G.add_edge('start', 'resource-wrap')
        G.add_edge('start', 'accept')
        G.add_edge('resource-name', 'accept')
        G.add_edge('resource-wrap', 'accept')
        return G