class Element:
    def __init__(self, name):
        self.name = name 
    
    def check(self, element_tree_node):
        if element_tree_node.tag == self.name:
            return True 
        else:
            print('Expected Tag: ', element_tree_node.tag)
            print('Received Tag: ', self.name)
            return False