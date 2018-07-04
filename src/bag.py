'''
Created on Jul 3, 2018

@author: fantana
'''
from linkedlist import StringLinkedNode
from linkedlist import list_search


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
        else:
            the_count = 0
            bag_list = self.head_node
            while bag_list is not None:
                if bag_list.getData() == bag_data_string:
                    break
                else:
                    the_count = the_count + 1
            return False #none of the list elements matched the String
        element_before = list_search(self.head_node, the_count -1)
        self.head_node.remove_node_after(element_before)
        return True
                    
    
if __name__ == '__main__':
    pass