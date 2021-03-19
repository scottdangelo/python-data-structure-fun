#! /usr/bin/env python

from LinkedList import Node, LinkedList

def is_intersect(list1, list2):
    for n in list1:
        for n2 in list2:
            if n == n2:
                return True
    return False

node1 = Node(2)
node2 = Node(8)
node3 = Node(5)
node4 = Node(3)
node5 = Node(10)
node6 = Node(4)

nodeA = Node(3)
nodeB = Node(10)
nodeC = Node(4)

link1 = LinkedList()
link2 = LinkedList()

link1.insert(node1)
link1.insert(node2)
link1.insert(node2)
link1.insert(node3)
link1.insert(node4)
link1.insert(node5)
link1.insert(node6)

link2.insert(nodeA)
link2.insert(nodeB)
link2.insert(nodeC)
link2.insert(node4)
link2.insert(node5)
link2.insert(node6)

print(link1)
print(link2)
print(is_intersect(link1,link2))