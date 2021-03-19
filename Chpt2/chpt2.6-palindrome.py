#! /usr/bin/env python

from LinkedList import Node, LinkedList

node1 = Node(2)
node2 = Node(8)
node3 = Node(5)
node4 = Node(3)
node5 = Node(10)
node6 = Node(4)

link1 = LinkedList()

link1.insert(node1)
link1.insert(node2)
link1.insert(node2)
link1.insert(node3)
link1.insert(node4)
link1.insert(node5)
link1.insert(node6)
link1.insert(Node(4))
link1.insert(Node(10))
link1.insert(Node(3))
link1.insert(Node(5))
link1.insert(Node(8))
link1.insert(Node(2))

print(link1)

def is_palindrome(list1):
    ar1 = []

    for n in list1:
        if n.data == None:
            continue
        ar1.append(n.data)
    leng = len(ar1)-1
    ret = True
    print(ar1)
    for i,c in enumerate(ar1):
        #print("c: {}, ar1[i]: {},\
        #    ar1[leng - i]: {}".format(c, ar1[i],
        #    ar1[leng - i]))
        if ar1[i] != ar1[leng -i]:
            ret = False
    return ret

print(link1)
print(is_palindrome(link1))