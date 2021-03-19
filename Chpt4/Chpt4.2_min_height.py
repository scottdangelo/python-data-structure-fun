#! /usr/bin/env python

from Tree import Node, BinaryTree

tarray = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
mid = int(len(tarray)/2)
print("Mid: {}".format(mid))

rootnode = Node(tarray[mid])
print("rootnode: {}".format(rootnode))

bintree = BinaryTree(rootnode)
for j,item in enumerate(tarray):
    if item == tarray[mid]:
        continue
    in_node = Node(tarray[j])
    bintree.insert(bintree.root, in_node)

print("bintree in_order_traversal from root:")
bintree.in_order_traversal(bintree.root)