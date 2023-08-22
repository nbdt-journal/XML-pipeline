import networkx as nx

class Compound_subject:
    def __init__(self):
        self.name = 'compound-subject' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('compound-subject-part')
        #adding edges
        G.add_edge('start', 'compound-subject-part')
        G.add_edge('compound-subject-part', 'compound-subject-part')
        G.add_edge('compound-subject-part', 'accept')
        return G