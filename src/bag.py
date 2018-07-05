'''
Created on Jul 3, 2018

@author: fantana
'''
from linkedlist import StringLinkedNode
from linkedlist import list_search
from linkedlist import list_length


class BagOfStrings:
    ''' This is the 'random bag' data structure implemented 
        using the linked list we created in linkedlist.py
    '''
    number_items = 0
    head_node = None
    
    def __init__(self):
        self.head_node = None
        self.number_items = 0
    
    def update_head(self, bag_data_string):
        if self.head_node is None:
            self.head_node = StringLinkedNode(None, bag_data_string)
        else:
            self.head_node = StringLinkedNode(self.head_node, bag_data_string)
        self.number_items = self.number_items + 1
        
    def remove(self, bag_data_string):
        ''' find the string and remove the link that has the string data
            return true if removal was successful.  If the string cannot 
            be found or if the list is None, return false.
        '''
        if self.head_node is None:
            return False
        node_to_remove = list_search(self.head_node, bag_data_string)
        
        if node_to_remove is None:
            return False
        
        node_to_remove.set_data(self.head_node.get_data())
        self.head_node = self.head_node.get_link()
        self.number_items = self.number_items - 1
        return True
        
        
        '''
        else:
            the_count = 0
            bag_list = self.head_node
            while bag_list is not None:
                if bag_list.get_data() == bag_data_string:
                    break
                else:
                    the_count = the_count + 1
                    bag_list = bag_list.get_link()
            return False #none of the list elements matched the String
        element_before = list_search(self.head_node, the_count -1)
        element_before.remove_node_after()
        return True
    '''
    
    
    
    def add(self, bag_data_string=""):
        ''' Add the string to the bag at the head
        '''
        self.head_node = StringLinkedNode(self.head_node, bag_data_string)
        self.number_items = self.number_items + 1
              
    def print_data(self):
        print_head = self.head_node
        for data in range(list_length(print_head)+1):
            print(print_head.get_data())
            print_head = print_head.get_link()
    
if __name__ == '__main__':
    
    new_bag = BagOfStrings()
    new_bag.add("first")
    new_bag.add("second")
    new_bag.add("third")
    new_bag.add("fourth")
    new_bag.print_data()
    print(new_bag.remove("third"))#there is a bug here    
    new_bag.print_data()
    
    pass