import networkx as nx

class Award_group:
    def __init__(self):
        self.name = 'award-group' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('award-id')
        G.add_node('award-name')
        G.add_node('award-desc')
        G.add_node('principal-award-recipient')
        G.add_node('principal-investigator')
        G.add_node('funding-source')
        G.add_node('support-source')
        #adding edges
        G.add_edge('start', 'funding-source')
        G.add_edge('award-id', 'award-id')
        G.add_edge('award-id', 'award-name')
        G.add_edge('award-id', 'award-desc')
        G.add_edge('award-id', 'principal-award-recipient')
        G.add_edge('award-id', 'principal-investigator')
        G.add_edge('award-id', 'accept')
        G.add_edge('award-name', 'award-desc')
        G.add_edge('award-name', 'principal-award-recipient')
        G.add_edge('award-name', 'principal-investigator')
        G.add_edge('award-name', 'accept')
        G.add_edge('award-desc', 'principal-award-recipient')
        G.add_edge('award-desc', 'principal-investigator')
        G.add_edge('award-desc', 'accept')
        G.add_edge('principal-award-recipient', 'principal-award-recipient')
        G.add_edge('principal-award-recipient', 'principal-investigator')
        G.add_edge('principal-award-recipient', 'accept')
        G.add_edge('principal-investigator', 'principal-investigator')
        G.add_edge('principal-investigator', 'accept')
        G.add_edge('funding-source', 'award-id')
        G.add_edge('funding-source', 'award-name')
        G.add_edge('funding-source', 'award-desc')
        G.add_edge('funding-source', 'principal-award-recipient')
        G.add_edge('funding-source', 'principal-investigator')
        G.add_edge('funding-source', 'accept')
        G.add_edge('support-source', 'award-id')
        G.add_edge('support-source', 'award-name')
        G.add_edge('support-source', 'award-desc')
        G.add_edge('support-source', 'principal-award-recipient')
        G.add_edge('support-source', 'principal-investigator')
        G.add_edge('support-source', 'accept')
        return G