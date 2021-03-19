#! /usr/bin/env python

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None
    def __repr__(self):
        return str(self.data)
    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self, node):
        self.root = node
        self.children = []
        self.root.parent = Node("root parent")

    def insert(self,node):
        if self.root == None:
            self.root = node
        self.root.children.append(node)
    
class BinaryTree(Tree):
    def __init__(self, node):
        super().__init__(node)
        self.root.right_child = None
        self.root.left_child = None
    
    def __repr__(self) -> str:
        return str(self.in_order_traversal(self.root))

    # def swap_nodes(self, nodeh, nodel):
        # nodel.parent = nodeh.parent
        # nodel.left_child = nodeh
        
    def insert(self, start_node, insert_node):
        if insert_node == None:
            raise Exception("Cannot insert None")
        else:
            if start_node.left_child == None and\
                insert_node.data < start_node.data:
                    start_node.left_child = insert_node
                    insert_node.parent = start_node
            elif start_node.right_child == None and \
                insert_node.data >= start_node.data:
                    if start_node.left_child == None:
                        if insert_node.data < start_node.parent.data:
                            start_node.parent.left_child = insert_node
                        else: # insert_node >= start_node.parent
                            start_node.parent.right_child = insert_node
                        insert_node.parent = start_node.parent
                        insert_node.left_child = start_node
                        start_node.parent = insert_node

                    else:
                        start_node.right_child = insert_node
                        insert_node.parent = start_node
        
            elif insert_node.data < start_node.data:
                self.insert(start_node.left_child, insert_node)
            else: # insert_node.data >= start_node.data:
                self.insert(start_node.right_child, insert_node)
    
    def in_order_traversal(self, node):
        if (node != None):
            self.in_order_traversal(node.left_child)
            print(str(node.data) + " " + (str(node.parent.data)))
            self.in_order_traversal(node.right_child)

    def rebalance(self, node):
        if (node != None):
            self.in_order_traversal(node.left_child)
            print(str(node.data) + " " + (str(node.parent.data)))
            self.in_order_traversal(node.right_child)
    def post_order_traversal(self, node):
        if (node != None):
            self.in_order_traversal(node.left_child)
            self.in_order_traversal(node.right_child)
            print(str(node.data) + " " + (str(node.parent.data)))

    def get_successor(self, node):
        if node.parent.data == "root parent":
            root_ret = "poop"
            return root_ret
        if node.parent.left_child == node:
            return node.parent.data
        if node.parent.right_child == node and \
            node.right_child is not None:
            return node.right_child.data
        if node.parent.right_child == node and \
            node.right_child is None:
            if node.parent.parent.left_child == node.parent:
                return node.parent.parent.data
            else: # node is parent's right child, node is max
                return node.data
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root==None: return True
        if abs(self.maxDepth(root.left)-self.maxDepth(root.right))<=1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else: return False
         
    def maxDepth(self, root):
        if root==None: return 0
        if root.left==None and root.right==None: return 1
        return max(self.maxDepth(root.left)+1,self.maxDepth(root.right)+1)