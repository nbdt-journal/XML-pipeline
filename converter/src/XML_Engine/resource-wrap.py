import networkx as nx

class Resource_wrap:
    def __init__(self):
        self.name = 'resource-wrap' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('resource-name')
        G.add_node('resource-id')
        #adding edges
        G.add_edge('start', 'resource-name')
        G.add_edge('resource-name', 'resource-id')
        G.add_edge('resource-name', 'accept')
        G.add_edge('resource-id', 'resource-id')
        G.add_edge('resource-id', 'accept')
        return G