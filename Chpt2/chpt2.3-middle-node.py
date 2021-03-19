#! /usr/bin/env python

from LinkedList import Node, LinkedList

def remove_middle(my_list, mid_node):
    '''Removes the mid_node.
       If only the head exists, return None'''

    my_list.remove(mid_node)

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

print(new_linked)
remove_middle(new_linked, node3)
print(new_linked)
