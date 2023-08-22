import networkx as nx

class Event:
    def __init__(self):
        self.name = 'event' 
        self.DTD  = self.make_DTD()

    def make_DTD(self):
        G = nx.DiGraph()
        #adding nodes
        G.add_node('start')
        G.add_node('accept')
        G.add_node('event-desc')
        G.add_node('article-id')
        G.add_node('issn')
        G.add_node('issn-l')
        G.add_node('isbn')
        G.add_node('permissions')
        G.add_node('notes')
        G.add_node('self-uri')
        G.add_node('pub-date')
        G.add_node('article-version')
        G.add_node('article-version-alternatives')
        G.add_node('date')
        G.add_node('string-date')
        #adding edges
        G.add_edge('start', 'event-desc')
        G.add_edge('start', 'pub-date')
        G.add_edge('start', 'issn')
        G.add_edge('start', 'issn-l')
        G.add_edge('start', 'isbn')
        G.add_edge('start', 'permissions')
        G.add_edge('start', 'notes')
        G.add_edge('start', 'self-uri')
        G.add_edge('start', 'accept')
        G.add_edge('event-desc', 'article-id')
        G.add_edge('event-desc', 'pub-date')
        G.add_edge('event-desc', 'article-version')
        G.add_edge('event-desc', 'article-version-alternatives')
        G.add_edge('event-desc', 'accept')
        G.add_edge('article-id', 'article-id')
        G.add_edge('article-id', 'pub-date')
        G.add_edge('article-id', 'article-version')
        G.add_edge('article-id', 'article-version-alternatives')
        G.add_edge('article-id', 'accept')
        G.add_edge('issn', 'issn')
        G.add_edge('issn', 'issn-l')
        G.add_edge('issn', 'isbn')
        G.add_edge('issn', 'permissions')
        G.add_edge('issn', 'notes')
        G.add_edge('issn', 'self-uri')
        G.add_edge('issn', 'accept')
        G.add_edge('issn-l', 'isbn')
        G.add_edge('issn-l', 'permissions')
        G.add_edge('issn-l', 'notes')
        G.add_edge('issn-l', 'self-uri')
        G.add_edge('issn-l', 'accept')
        G.add_edge('isbn', 'isbn')
        G.add_edge('isbn', 'permissions')
        G.add_edge('isbn', 'notes')
        G.add_edge('isbn', 'self-uri')
        G.add_edge('isbn', 'accept')
        G.add_edge('permissions', 'notes')
        G.add_edge('permissions', 'self-uri')
        G.add_edge('permissions', 'accept')
        G.add_edge('notes', 'notes')
        G.add_edge('notes', 'self-uri')
        G.add_edge('notes', 'accept')
        G.add_edge('self-uri', 'self-uri')
        G.add_edge('self-uri', 'accept')
        G.add_edge('pub-date', 'issn')
        G.add_edge('pub-date', 'issn-l')
        G.add_edge('pub-date', 'isbn')
        G.add_edge('pub-date', 'permissions')
        G.add_edge('pub-date', 'notes')
        G.add_edge('pub-date', 'self-uri')
        G.add_edge('pub-date', 'accept')
        G.add_edge('pub-date', 'date')
        G.add_edge('pub-date', 'string-date')
        G.add_edge('article-version', 'pub-date')
        G.add_edge('article-version-alternatives', 'pub-date')
        G.add_edge('date', 'issn')
        G.add_edge('date', 'issn-l')
        G.add_edge('date', 'isbn')
        G.add_edge('date', 'permissions')
        G.add_edge('date', 'notes')
        G.add_edge('date', 'self-uri')
        G.add_edge('date', 'accept')
        G.add_edge('string-date', 'issn')
        G.add_edge('string-date', 'issn-l')
        G.add_edge('string-date', 'isbn')
        G.add_edge('string-date', 'permissions')
        G.add_edge('string-date', 'notes')
        G.add_edge('string-date', 'self-uri')
        G.add_edge('string-date', 'accept')
        return G