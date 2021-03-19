#! /usr/bin/env python

from LinkedList import Node, LinkedList

op1 = LinkedList()
op2 = LinkedList()

node1 = Node(7)
node2 = Node(1)
node3 = Node(6)
node4 = Node(5)
node5 = Node(9)
node6 = Node(2)

op1.insert(node1)
op1.insert(node2)
op1.insert(node3)
op2.insert(node4)
op2.insert(node5)
op2.insert(node6)

def sum_list(list1, list2):
    '''Sum 2 linked lists.
       First node is 1s digit,2nd is 10s,
       etc.'''
    num1 = []
    num2 = []
    ret1 = 0
    ret2 = 0
    for n in list1:
        if n.data == None:
            continue
        num1.append(n.data)
    for n in list2:
        if n.data == None:
            continue
        num2.append(n.data)
    for i in range(0,len(num1)):
        ret1 += num1[i]*(10**(i))
    for i in range(0,len(num2)):
        ret2 += num2[i]*(10**(i))
    return (ret1 + ret2)

print(op1)
print(op2)
print(sum_list(op1, op2))