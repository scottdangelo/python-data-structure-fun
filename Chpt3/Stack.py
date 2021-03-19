#! /usr/bin/env python

class Node():
    ''' Container for data'''
    def __init__(self, my_data):
        super().__init__()
        self.data = my_data
        self.next = None
    def __repr__(self):
        return(str(self.data))
    def __str__(self):
        return(str(self.data))

class Stack():
    '''Data structure with LIFO'''
    def __init__(self):
        self.top = None
        self.min = None
    
    def __repr__(self):
        return(str(self.top.data))
    def __str__(self):
        return(str(self.top.data))

    def push(self, my_node):
        '''Push node to top of Stack'''
        if my_node == None:
            raise Exception("Cannot insert None")
        my_node.next = self.top
        self.top = my_node
        if self.min == None:
            self.min = my_node
        elif my_node.data < self.min.data:
            self.min = my_node

    def pop(self):
        ret_node = self.top
        if ret_node == None:
            self.top = None
        else:
            self.top = ret_node.next
        return(ret_node)

    def peek(self):
        if self.top == None:
            ret = None
        else:
            ret = self.top.data
        return(ret)

    def is_empty(self):
        return(self.top == None)

    def ret_min(self):
        return self.min