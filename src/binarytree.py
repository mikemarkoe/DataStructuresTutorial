'''
Created on Jun 24, 2018


'''

class StringBinaryTreeNode:
    """This is the Binary Tree node containing string data.

    Attributes:
        data: string data contained in this node
        left: connection to left side StringBinaryTreeNode.
        right: connection to right side StringBinaryTreeNode.

    """
    node_data = ""
    left = None
    right = None
    
    def __init__(self, node_data, left=None, right=None):
        """ The initialization method defaults the left and right
        StringBinaryTreeNodes to None.
        """
        self.node_data = node_data
        self.left = left
        self.right = right
    
    def get_node_data(self):
        return self.node_data
    
    def get_left_node(self):
        return self.left
    
    def get_right_node(self):
        return self.right
    
    def set_data(self, node_data):
        self.node_data = node_data
        
    def set_left_node(self, left):
        self.left = left
        
    def set_right_node(self, right):
        self.right = right
        
    def is_leaf(self):
        return (self.left is None and self.right is None)            
            
    def get_leftmost_data(self):
        if (self.left is None):
            return self.node_data
        else:            
            return self.left.get_leftmost_data()
        
    def remove_leftmost_node(self):
        if (self.left is None):
            return self.right
        else:
            the_left = self.get_left_node()
            return the_left.remove_leftmost_node()
        
if __name__ == '__main__':
    
    left_righty = StringBinaryTreeNode("I'm instantiated as the right below the left")
    left_lefty = StringBinaryTreeNode("I'm a lower left lefty.")
    left_tree = StringBinaryTreeNode("I'm a lefty", left_lefty, left_righty)
    my_tree = StringBinaryTreeNode("I AM ROOT", left_tree, None)
    print(my_tree.is_leaf())
    print(my_tree.get_leftmost_data())
    my_tree.remove_leftmost_node()
    print(my_tree.get_leftmost_data())#fix this it doesn't work

    
    pass