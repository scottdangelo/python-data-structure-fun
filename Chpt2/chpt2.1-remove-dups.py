#! /usr/bin/env python

from LinkedList import Node, LinkedList

def remove_dups(test_list):
    '''Removes duplicate nodes from a linked list '''
    for node in test_list:
        unique_data = node.data
        current = node
        while current and current.next_node:
            if unique_data == current.next_node.data:
                # We've found a dup. Delete it
                dup = current.next_node
                test_list.remove(dup)
            current = current.next_node

new_linked = LinkedList()

node1 = Node("first")
node2 = Node("second")
node3 = Node("third")
node4 = Node("fourth")
node5 = Node("second")
node6 = Node("third")

new_linked.insert(node1)
new_linked.insert(node2)
new_linked.insert(node3)
new_linked.insert(node4)
new_linked.insert(node5)
new_linked.insert(node6)

print(new_linked)
remove_dups(new_linked)
print(new_linked)