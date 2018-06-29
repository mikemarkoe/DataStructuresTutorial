'''
Created on Jun 28, 2018

@author: fantana
'''

class StringLinkedNode:
    """ Linked List node containing string data.

        Attributes:
        data: string data contained in this node
        link: connection to linked StringLinkedNode.
    """
    data = ""
    link = None
    
    def __init__(self, link = None, node_data = ""):
        self.data = node_data
        self.link = link
        
    def get_data(self):
        return self.data
    
    def get_link(self):
        return self.link
    
    def set_data(self, updated_data = ""):
        self.data = updated_data
        
    def set_link(self, updated_link = None):
        self.link = updated_link
        
    def add_node_after(self, node_data):
        ''' Add a node after this node.
            If it is "None" it will become the tail of the list.
        '''
        current_next_node = self.get_link()
        self.link = StringLinkedNode(current_next_node, node_data)


if __name__ == '__main__':
    
    next2 = StringLinkedNode(None, "Next Next one")        
    next1 = StringLinkedNode(next2, "Next one")
    head = StringLinkedNode(next1, "this is the HEAD")
    head = StringLinkedNode(head, "the new head")
    head.add_node_after("I'm new data, I just jumped in here!")
    print(head.get_data())
    print(head.get_link().get_data())
    print(head.get_link().get_link().get_data())
    pass