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
        self.link = StringLinkedNode(self.get_link(), node_data)
        
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
    the_count = 0    
    if node is  None: 
        return the_count
    else:
        while (node.get_link() is not None):
            the_count = the_count + 1
            node = node.get_link()
        return the_count
    
def list_search(starting_node, search_string):
    ''' This function returns the node that contains the search_string
    '''   
    if starting_node is None:
        return None
    else:
        while starting_node.get_link() is not None:
            if starting_node.get_data() == search_string:
                return starting_node
                break
            else:
                starting_node = starting_node.get_link()
    return None    
   
def get_node_from_position(starting_node, position):
    ''' Returns the node at the integer position
    '''         
    
    if starting_node is None:
        return None
    else:
        node_at_position = starting_node
        for reps in range(position):
            if node_at_position.get_link() is None:
                return None
            else:
                node_at_position = node_at_position.get_link()
            
    return node_at_position

def copy_list(input_list):
    ''' Makes a copy of the list, returns the head node
    '''
    if input_list is None:
        return None
    else:
        copied_list_head_node = StringLinkedNode(None, input_list.get_data())
        copied_list = copied_list_head_node
        while input_list.get_link() is not None:
            input_list = input_list.get_link()
            copied_list.add_node_after(input_list.get_data())
            copied_list = copied_list.get_link()
    return copied_list_head_node    

def copy_list_with_tail(input_list):
    ''' returns an array with a copy of the head of the list in element 0 
        and the tail of the list in element 1
    '''
    if input_list is None:
        return None
    else:
        copied_list_head_node = StringLinkedNode(None, input_list.get_data())
        copied_list = copied_list_head_node
        while input_list.get_link() is not None:
            input_list = input_list.get_link()
            copied_list.add_node_after(input_list.get_data())
            copied_list = copied_list.get_link()
    
    return [copied_list_head_node, copied_list]        

if __name__ == '__main__':
    
    """
    
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
    prev_node = None
    for i in range(4):
        new_node = StringLinkedNode(prev_node, str(i+1))
        prev_node = new_node

    print(new_node.get_data())
    print(new_node.get_link().get_data())
    print(new_node.get_link().get_link().get_data())
    print(list_length(new_node))
    
    seventh = list_search(new_node, "2")
    
    print(seventh.get_data())
    
    
    eighth = get_node_from_position(new_node, 2)
    print(eighth.get_data())
    
    
    copy_of_new_node = copy_list_with_tail(new_node)
    print(copy_of_new_node[0].get_data())
    print(copy_of_new_node[0].get_link().get_data())
    print(copy_of_new_node[0].get_link().get_link().get_data())
    print(copy_of_new_node[1].get_data())   
    print(list_length(copy_of_new_node[0]))
    """
    pass