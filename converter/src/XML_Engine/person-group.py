import networkx as nx

class Person_group:
    def __init__(self):
        self.name = 'person-group' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('#PCDATA')
        G.add_node('anonymous')
        G.add_node('collab')
        G.add_node('collab-alternatives')
        G.add_node('name')
        G.add_node('name-alternatives')
        G.add_node('string-name')
        G.add_node('aff')
        G.add_node('aff-alternatives')
        G.add_node('etal')
        G.add_node('role')
        G.add_node('x')
        #adding edges
        G.add_edge('start', '#PCDATA')
        G.add_edge('start', 'anonymous')
        G.add_edge('start', 'collab')
        G.add_edge('start', 'collab-alternatives')
        G.add_edge('start', 'name')
        G.add_edge('start', 'name-alternatives')
        G.add_edge('start', 'string-name')
        G.add_edge('start', 'aff')
        G.add_edge('start', 'aff-alternatives')
        G.add_edge('start', 'etal')
        G.add_edge('start', 'role')
        G.add_edge('start', 'x')
        G.add_edge('start', 'accept')
        G.add_edge('#PCDATA', 'accept')
        G.add_edge('anonymous', 'accept')
        G.add_edge('collab', 'accept')
        G.add_edge('collab-alternatives', 'accept')
        G.add_edge('name', 'accept')
        G.add_edge('name-alternatives', 'accept')
        G.add_edge('string-name', 'accept')
        G.add_edge('aff', 'accept')
        G.add_edge('aff-alternatives', 'accept')
        G.add_edge('etal', 'accept')
        G.add_edge('role', 'accept')
        G.add_edge('x', 'accept')
        return G