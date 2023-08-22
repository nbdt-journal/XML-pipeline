import networkx as nx

class Issue_title_group:
    def __init__(self):
        self.name = 'issue-title-group' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('issue-title')
        G.add_node('issue-subtitle')
        G.add_node('trans-title-group')
        #adding edges
        G.add_edge('start', 'issue-title')
        G.add_edge('issue-title', 'issue-subtitle')
        G.add_edge('issue-title', 'trans-title-group')
        G.add_edge('issue-title', 'accept')
        G.add_edge('issue-subtitle', 'issue-subtitle')
        G.add_edge('issue-subtitle', 'trans-title-group')
        G.add_edge('issue-subtitle', 'accept')
        G.add_edge('trans-title-group', 'trans-title-group')
        G.add_edge('trans-title-group', 'accept')
        return G