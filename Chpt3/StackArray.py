#! /usr/bin/env python

class StackArray:
    ''' A stack implemented as an array
    '''
    def __init__(self):
        self.stack_array = []
        self.min = None

    def __repr__(self):
        return str(self.stack_array)

    def __str__(self):
        return str(self.stack_array)

    def top_index(self):
        return (len(self.stack_array) -1)
    def is_empty(self):
        return (self.top_index() == 0)

    def push(self,obj):
        self.stack_array.append(obj)

    def pop(self):
        return self.stack_array.pop()

    def peek(self):
        return self.stack_array[self.top_index()]
