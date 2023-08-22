import networkx as nx

class Article_categories:
    def __init__(self):
        self.name = 'article-categories' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('subj-group')
        G.add_node('series-title')
        G.add_node('series-text')
        #adding edges
        G.add_edge('start', 'subj-group')
        G.add_edge('subj-group', 'subj-group')
        G.add_edge('subj-group', 'series-title')
        G.add_edge('subj-group', 'series-text')
        G.add_edge('subj-group', 'accept')
        G.add_edge('series-title', 'series-title')
        G.add_edge('series-title', 'series-text')
        G.add_edge('series-title', 'accept')
        G.add_edge('series-text', 'series-text')
        G.add_edge('series-text', 'accept')
        return G