#! /usr/bin/env python

from Stack import Stack, Node

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

my_stack = Stack()

my_stack.push(node1)
my_stack.push(node2)
my_stack.push(node3)
my_stack.push(node4)
my_stack.push(node5)
my_stack.push(node6)
my_stack.push(node7)

print("Test peek")
print(my_stack.peek())

print("Test pop")
ret_node = my_stack.pop()
print("Test node: {}".format(ret_node))
print("New top: {}".format(my_stack.peek()))

print("Find Min")
print(my_stack.min)