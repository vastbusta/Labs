# -*- coding: utf-8 -*-
"""

Author:Ruben Bustamante
Instructor: Diego Aguirre
TA:Gerarado Barraza
Course: CS 2302
Assigment: Lab 3B
Date of last modification: 10/14/2019
Purpose of program: AVL tree file for lab 3
"""

class Node:
    # AVL Node constructor
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0

    
    def get_balance(self):
        # Find current height of left subtree, or -1 if None
        left_height = -1
        if self.left is not None:
            left_height = self.left.height

        # Find right subtree's current height, or -1 if None
        right_height = -1
        if self.right is not None:
            right_height = self.right.height


        return left_height - right_height

    # Updates the height if needed
    def update_height(self):
        # Find current height of left subtree, or -1 if None
        left_height = -1
        if self.left is not None:
            left_height = self.left.height

        # Find current height of right subtree, or -1 if None
        right_height = -1
        if self.right is not None:
            right_height = self.right.height

        # Assign self.height with calculated node height.
        self.height = max(left_height, right_height) + 1
        
        
    def set_child(self, which_child, child):
        # check which_child is properly assigned.
        if which_child != "left" and which_child != "right":
            return False

        # Assign the left or righ child.
        if which_child == "left":
            self.left = child
        else:
            self.right = child

        # if child is not None, Assign the new child's parent
        if child is not None:
            child.parent = self

        # Update the node's height, if needed
        self.update_height()
        return True

    # Replace a current child with a new child. 
    def replace_child(self, current_child, new_child):
        if self.left is current_child:
            return self.set_child("left", new_child)
        elif self.right is current_child:
            return self.set_child("right", new_child)

        return False


class AVLTree:
    def __init__(self):
        #AVL Tree constructor
        self.root = None

    # Performs a left rotation 
    def rotate_left(self, node):
        #the node's right, left child
        right_left_child = node.right.left

        if node.parent is not None:
            node.parent.replace_child(node, node.right)
        else:  # node is root
            self.root = node.right
            self.root.parent = None

        node.right.set_child('left', node)

        node.set_child('right', right_left_child)

        return node.parent

    # Performs a right rotation at the given node
    def rotate_right(self, node):
        #The node's left, right child
        left_right_child = node.left.right

        
        if node.parent is not None:
            node.parent.replace_child(node, node.left)
        else:  # node is root
            self.root = node.left
            self.root.parent = None

        
        node.left.set_child('right', node)

        node.set_child('left', left_right_child)

        return node.parent

    # Updates the node's height and rebalances the tree
    def rebalance(self, node):

        node.update_height()

       
        if node.get_balance() == -2:

        
            if node.right.get_balance() == 1:
                # Double rotation case.
                self.rotate_right(node.right)

            # A left rotation will now make the subtree balanced.
            return self.rotate_left(node)

        elif node.get_balance() == 2:

            if node.left.get_balance() == -1:
                # Double rotation case. 
                self.rotate_left(node.left)

            # A right rotation will now make the subtree balanced.
            return self.rotate_right(node)

        # No imbalance, so just return the original node.
        return node

    # Insert a new node into the Tree
    def insert(self, node):

        #if the tree is empty set the root to the new node
        if self.root is None:
            self.root = node
            node.parent = None

        else:
          
            current_node = self.root
            while current_node is not None:
        
                if node.key < current_node.key:
                   
                    if current_node.left is None:
                        current_node.left = node
                        node.parent = current_node
                        current_node = None
                    else:
                      
                        current_node = current_node.left
                else:
                  
                    if current_node.right is None:
                        current_node.right = node
                        node.parent = current_node
                        current_node = None
                    else:
                       
                        current_node = current_node.right

            node = node.parent
            while node is not None:
                self.rebalance(node)
                node = node.parent

    # Searches for a key in the tree
    def search(self, key):
        current_node = self.root
        while current_node is not None:
            # Compare the current node's key to key that we are looking for
            if current_node.key == key:
                return True
            elif current_node.key < key:
                current_node = current_node.right
            else:
                current_node = current_node.left

        return False

    # Attempts to remove a node with a matching key
    def remove_key(self, key):
        node = self.search(key)
        if node is None:
            return False
        else:
            return self.remove_node(node)

    # Removes the given node from the tree. 
    def remove_node(self, node):
        # Base case:
        if node is None:
            return False

        # Parent needed for rebalancing.
        parent = node.parent

     
        if node.left is not None and node.right is not None:
          
            successor_node = node.right
            while successor_node.left != None:
                successor_node = successor_node.left

            node.key = successor_node.key

            self.remove_node(successor_node)

            
            return True

        elif node is self.root:
            if node.left is not None:
                self.root = node.left
            else:
                self.root = node.right

            if self.root is not None:
                self.root.parent = None

            return True

       
        elif node.left is not None:
            parent.replace_child(node, node.left)

     
        else:
            parent.replace_child(node, node.right)

        node = parent
        while node is not None:
            self.rebalance(node)
            node = node.parent

        return True