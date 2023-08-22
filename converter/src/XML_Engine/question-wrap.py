import networkx as nx

class Question_wrap:
    def __init__(self):
        self.name = 'question-wrap' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('question')
        G.add_node('explanation')
        G.add_node('object-id')
        G.add_node('answer')
        G.add_node('answer-set')
        #adding edges
        G.add_edge('start', 'object-id')
        G.add_edge('start', 'explanation')
        G.add_edge('start', 'accept')
        G.add_edge('question', 'explanation')
        G.add_edge('question', 'accept')
        G.add_edge('question', 'answer')
        G.add_edge('question', 'answer-set')
        G.add_edge('explanation', 'explanation')
        G.add_edge('explanation', 'accept')
        G.add_edge('object-id', 'question')
        G.add_edge('answer', 'explanation')
        G.add_edge('answer', 'accept')
        G.add_edge('answer-set', 'explanation')
        G.add_edge('answer-set', 'accept')
        return G