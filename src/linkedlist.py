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
    
    def __init__(self, data = "", link = None):
        self.data = data
        self.link = link
        
    def get_data(self):
        return self.data
    
    def get_link(self):
        return self.link
    
    def set_data(self, updated_data = ""):
        self.data = updated_data
        
    def set_link(self, updated_link = None):
        self.link = updated_link
        


if __name__ == '__main__':
    
    head = StringLinkedNode("this is the HEAD", None)
    
    print(head.get_data())
    pass