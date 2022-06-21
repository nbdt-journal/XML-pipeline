import networkx as nx 
import xml.etree.ElementTree as ET

from element import Element 

class Node:
    def __init__(self, element, graph, start_node=False, end_node=False):
        self.element = element 
        self.graph = graph 
        self.start_node = start_node
        self.end_node = end_node

    def check(self, element_tree_node):
        # no check for start or end nodes
        if self.start_node or self.end_node:
            return True 
        print(self.element.name)
        # element verification failed
        if not self.element.check(element_tree_node):
            print('Element Verification Failed')
            return False
        # element verification passed
        else:
            for node in self.graph.nodes:
                # marking the start-node
                if node.start_node:
                    start_node = node
                # marking the end-node 
                if node.end_node:
                    end_node = node 
            curr_node = start_node
            curr_connections = list([each[1] for each in self.graph.edges(curr_node)]) 
            # iterating through each child of the tag
            for child in element_tree_node: 
                found_connection = False 
                # looking for a connection
                for connected_node in curr_connections:
                    # if a connection is found
                    if connected_node.element.name == child.tag:
                        found_connection = True
                        # error in verification of child tag 
                        if not connected_node.check(child):
                            return False
                        # no errors detected in verification of child tag
                        else:
                            curr_node = connected_node 
                            curr_connections = list([each[1] for each in self.graph.edges(curr_node)])
                # if no connection was found
                if found_connection is False:
                    print('Error!')
                    print('Expected Tag: ', end = '')
                    for each in curr_connections:
                        if each is curr_connections[-1]:
                            print(each.element.name)
                        else:
                            print(each.element.name, end = ' | ')
                    print('Received Tag: ' + child.tag)
            # traversing through all child-nodes
            if end_node not in curr_connections:
                print('Error!')
                print('Expected Tag: ', end = '')
                for each in curr_connections:
                    if each is curr_connections[-1]:
                        print(each.element.name)
                    else:
                        print(each.element.name, end = ' | ')
                print('Received Tag: None')
                return False 
        return True 
            

def printGraph(graph):
    print('Nodes: ', end = '')
    for node in graph.nodes:
        if node.start_node:
            print('First-Node', end = ', ')
        elif node.end_node:
            print('Last-Node')
        else:
            print(node.element.name, end = ', ')

def get_first_node():
    return Node(element=Element('first'), graph=None, start_node=True)

def get_last_node():
    return Node(element=Element('last'), graph=None, end_node=True)

def get_leaf_graph():
    G = nx.DiGraph()
    G.add_edge(get_first_node(), get_last_node())
    return G 

if __name__ == '__main__':
    ''' Building a graph for Front Matter ''' 
    # Defining Elements
    front = Element('front')
    journal_meta = Element('journal-meta')
    article_meta = Element('article-meta')
    notes = Element('notes')
    # Defining the Nodes
    journal_meta_node = Node(element=journal_meta, graph=get_leaf_graph())
    article_meta_node = Node(element=article_meta, graph=get_leaf_graph())
    notes_node = Node(element=notes, graph=get_leaf_graph())
    # Defining the Graph 
    G_front = nx.DiGraph()
    # creating the first and last node
    first_node = get_first_node()
    last_node = get_last_node()
    # adding the first-node
    G_front.add_node(first_node)
    # adding element nodes
    G_front.add_nodes_from([article_meta_node, journal_meta_node, notes_node])
    # adding the last-node
    G_front.add_node(last_node)
    # adding the edges
    G_front.add_edge(first_node, journal_meta_node)
    G_front.add_edge(journal_meta_node, article_meta_node)
    G_front.add_edge(article_meta_node, notes_node)
    G_front.add_edge(article_meta_node, last_node)
    G_front.add_edge(notes_node, last_node)
    # Defining the front node 
    front_node = Node(element=front, graph=G_front)
    # printGraph(G_front)

    tree = ET.parse('sample.xml')
    root = tree.getroot()
    for child in root:
        if child.tag == 'front':
            front = child 
    print(front_node.check(front))
    