#! /usr/bin/env python

from LinkedList import Node, LinkedList

def find_loop(list1):
    nodes = []
    for n in list1:
        if n in nodes:
            return n
        nodes.append(n)
    return None

node1 = Node(2)
node2 = Node(8)
node3 = Node(5)
node4 = Node(3)
node5 = Node(10)
node6 = Node(4)

link1 = LinkedList()

link1.insert(node1)
link1.insert(node2)
link1.insert(node3)
link1.insert(node4)
link1.insert(node5)
link1.insert(node6)
link1.insert(node3)
