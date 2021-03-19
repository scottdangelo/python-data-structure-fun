#! /usr/bin/env python
# import pytest
from ThreeStack import ThreeStack

my_stack = ThreeStack()

my_stack.push(2,1)
my_stack.push(8,1)
my_stack.push(9,1)
my_stack.push(2,1)
my_stack.push(4,1)
my_stack.push(5,1)
my_stack.push(1,1)

my_stack.push(22,2)
my_stack.push(24,2)
my_stack.push(25,2)
my_stack.push(21,2)

print("top1: {}".format(my_stack.top1))
print(ThreeStack.get_spot(my_stack, 2))

# print(my_stack)
print("peek: {}".format(my_stack.peek(1)))
ret = my_stack.pop(1)
print("pop: {}".format(ret))
print("my_stack: {}".format(my_stack))
print("find_top: {}".format(my_stack.find_top(1)))

print("get_spot: {}".format(my_stack.get_spot(2)))

