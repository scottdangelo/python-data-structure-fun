#! /usr/bin/env python

from LinkedList import Node, LinkedList

def ret_kth(in_list, kth):
    '''Input a linked list and the kth to last
       element to find.
       Return: Node for kth to last, kth>0
       If kth>length of list,return None'''

    node_array = []
    len_list = 0

    if kth < 0:
        return None

    for i,current in enumerate(in_list):
        node_array.append(current)
        len_list = i

    kth_from_last = len_list - kth
    if kth_from_last <0:
        return None
    return node_array[kth_from_last] 

new_linked = LinkedList()
node1 = Node("first")
node2 = Node("second")
node3 = Node("third")
node4 = Node("fourth")
node5 = Node("fifth")
node6 = Node("sixth")

new_linked.insert(node1)
new_linked.insert(node2)
new_linked.insert(node3)
new_linked.insert(node4)
new_linked.insert(node5)
new_linked.insert(node6)

test1 = ret_kth(new_linked, 3)
print(test1)

test2 = ret_kth(new_linked, 0)
print(test2)

test3 = ret_kth(new_linked, 5)
print(test3)

test4 = ret_kth(new_linked, 8)
print(test4)

test5 = ret_kth(new_linked, -8)
print(test5)