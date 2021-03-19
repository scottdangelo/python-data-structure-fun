#! /usr/bin/env python

from StackArray import StackArray

my_stack = StackArray()

my_stack.push(2)
my_stack.push(8)
my_stack.push(9)
my_stack.push(2)
my_stack.push(4)
my_stack.push(5)
my_stack.push(1)

print(my_stack)
print("peek: {}".format(my_stack.peek()))
ret = my_stack.pop()
print("pop: {}".format(ret))
print("my_stack: {}".format(my_stack))