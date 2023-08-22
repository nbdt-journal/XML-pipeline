import networkx as nx

class Resource_name:
    def __init__(self):
        self.name = 'resource-name' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('#PCDATA')
        G.add_node('bold')
        G.add_node('fixed-case')
        G.add_node('italic')
        G.add_node('monospace')
        G.add_node('overline')
        G.add_node('overline-start')
        G.add_node('overline-end')
        G.add_node('roman')
        G.add_node('sans-serif')
        G.add_node('sc')
        G.add_node('strike')
        G.add_node('underline')
        G.add_node('underline-start')
        G.add_node('underline-end')
        G.add_node('sub')
        G.add_node('sup')
        #adding edges
        G.add_edge('start', '#PCDATA')
        G.add_edge('start', 'bold')
        G.add_edge('start', 'fixed-case')
        G.add_edge('start', 'italic')
        G.add_edge('start', 'monospace')
        G.add_edge('start', 'overline')
        G.add_edge('start', 'overline-start')
        G.add_edge('start', 'overline-end')
        G.add_edge('start', 'roman')
        G.add_edge('start', 'sans-serif')
        G.add_edge('start', 'sc')
        G.add_edge('start', 'strike')
        G.add_edge('start', 'underline')
        G.add_edge('start', 'underline-start')
        G.add_edge('start', 'underline-end')
        G.add_edge('start', 'sub')
        G.add_edge('start', 'sup')
        G.add_edge('start', 'accept')
        G.add_edge('#PCDATA', 'accept')
        G.add_edge('bold', 'accept')
        G.add_edge('fixed-case', 'accept')
        G.add_edge('italic', 'accept')
        G.add_edge('monospace', 'accept')
        G.add_edge('overline', 'accept')
        G.add_edge('overline-start', 'accept')
        G.add_edge('overline-end', 'accept')
        G.add_edge('roman', 'accept')
        G.add_edge('sans-serif', 'accept')
        G.add_edge('sc', 'accept')
        G.add_edge('strike', 'accept')
        G.add_edge('underline', 'accept')
        G.add_edge('underline-start', 'accept')
        G.add_edge('underline-end', 'accept')
        G.add_edge('sub', 'accept')
        G.add_edge('sup', 'accept')
        return G