#! /usr/bin/env python

from LinkedList import Node, LinkedList
new_linked  = LinkedList()

node1 = Node("first")
node2 = Node("second")
node3 = Node("third")
node4 = Node("fourth")

new_linked.insert(node1)
new_linked.insert(node2)
new_linked.insert(node3)
new_linked.insert(node4)

print(new_linked)
for i in new_linked:
    print(i)

new_linked.remove(node3)
print(new_linked)

node5 = Node("fifth")
node6 = Node("sixth")
new_linked.insert(node5)
new_linked.insert(node6)

print(new_linked)
new_linked.remove(node6)
print(new_linked)