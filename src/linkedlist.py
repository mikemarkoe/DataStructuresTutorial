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
            
        '''
        current_next_node = self.get_link()
        self.link = StringLinkedNode(current_next_node, node_data)
        
    def remove_node_after(self):
        ''' Remove a node after this node.
        '''
        if (self.get_link() is not None):
            new_next_node = self.get_link().get_link()
            self.set_link(new_next_node)
        else:
            print("no node to remove")
            
def list_length(node):
    ''' This is a function to get the length of a list
        takes a node as input and returns an integer
    '''           
    if node is not None: 
        the_count = 0    
        while (node.get_link() is not None):
            the_count = the_count + 1
            node = node.get_link()
        return the_count
    else:
        return 0
    

if __name__ == '__main__':
    
    next2 = StringLinkedNode(None, "Next Next one")        
    next1  = StringLinkedNode(next2, "Next one")
    head = StringLinkedNode(next1, "this is the HEAD")
    head = StringLinkedNode(head, "the new head")
    head.add_node_after("I'm new data, I just jumped in here!")
    print(head.get_data())
    print(head.get_link().get_data())
    print(head.get_link().get_link().get_data())
    head.remove_node_after()
    print(head.get_data())
    print(head.get_link().get_data())
    print(head.get_link().get_link().get_data())    
    print(head.get_link().get_link().get_data())    
    
    only_one_node = StringLinkedNode(next1, "I'm just one node")
    only_one_node.remove_node_after()
    print(only_one_node.get_data())
    prev_node = StringLinkedNode(None)
    for i in range(20):
        new_node = StringLinkedNode(prev_node, str(i))
        prev_node = new_node

    print(new_node.get_data())
    print(new_node.get_link().get_data())
    print(new_node.get_link().get_link().get_data())
    print(list_length(new_node))
    
    pass