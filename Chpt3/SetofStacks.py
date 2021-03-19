#! /usr/bin/env python

from Chpt3.Stack import Node, Stack

class SetofStacks:
    def __init__(self, max_size):
        self.stacks = []
        if self.max_size == 0:
            raise Exception("max size cannot be zero.")
        self.max = max_size
        self.total_nodes = 0
        for i in range(max_size):
            self.stacks[i] = Stack()

    def get_stack_num(self):
        stack_num = self.total_nodes/self.max
        is_full = self.total_nodes % self.max == 0
        if is_full:
            return stack_num +1
        else:
            return stack_num

    def push(self, node):
        this_stack = self.stacks[(self.get_stack_num())]        
