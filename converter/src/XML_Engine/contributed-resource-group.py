import networkx as nx

class Contributed_resource_group:
    def __init__(self):
        self.name = 'contributed-resource-group' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('award-group')
        G.add_node('support-description')
        G.add_node('resource-group')
        #adding edges
        G.add_edge('start', 'award-group')
        G.add_edge('award-group', 'award-group')
        G.add_edge('award-group', 'support-description')
        G.add_edge('award-group', 'resource-group')
        G.add_edge('award-group', 'accept')
        G.add_edge('support-description', 'support-description')
        G.add_edge('support-description', 'resource-group')
        G.add_edge('support-description', 'accept')
        G.add_edge('resource-group', 'resource-group')
        G.add_edge('resource-group', 'accept')
        return G