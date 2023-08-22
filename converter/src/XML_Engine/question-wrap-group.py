import networkx as nx

class Question_wrap_group:
    def __init__(self):
        self.name = 'question-wrap-group' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('label')
        G.add_node('title')
        G.add_node('subtitle')
        G.add_node('alt-title')
        G.add_node('question-preamble')
        G.add_node('object-id')
        G.add_node('question-wrap')
        #adding edges
        G.add_edge('start', 'object-id')
        G.add_edge('label', 'title')
        G.add_edge('label', 'subtitle')
        G.add_edge('label', 'alt-title')
        G.add_edge('label', 'question-preamble')
        G.add_edge('label', 'question-wrap')
        G.add_edge('title', 'subtitle')
        G.add_edge('title', 'alt-title')
        G.add_edge('title', 'question-preamble')
        G.add_edge('title', 'question-wrap')
        G.add_edge('subtitle', 'subtitle')
        G.add_edge('subtitle', 'alt-title')
        G.add_edge('subtitle', 'question-preamble')
        G.add_edge('subtitle', 'question-wrap')
        G.add_edge('alt-title', 'alt-title')
        G.add_edge('alt-title', 'question-preamble')
        G.add_edge('alt-title', 'question-wrap')
        G.add_edge('question-preamble', 'question-wrap')
        G.add_edge('object-id', 'label')
        G.add_edge('object-id', 'title')
        G.add_edge('object-id', 'subtitle')
        G.add_edge('object-id', 'alt-title')
        G.add_edge('object-id', 'question-preamble')
        G.add_edge('object-id', 'question-wrap')
        G.add_edge('question-wrap', 'accept')
        return G