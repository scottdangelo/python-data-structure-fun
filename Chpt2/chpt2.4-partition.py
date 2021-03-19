#! /usr/bin/env python

from LinkedList import Node, LinkedList

def partition(my_list, part_node):
    #rt_node = part_node
    #lft_node = my_list.head
    #last_node = None
    last_left = None
    last_right = None
    first_right = None
    previous = my_list.head

    n = my_list.head
    while n != None:
        if n == my_list.head:
            n = n.next_node
            continue
        if n.data < part_node.data:
            if last_right == None:
                # Haven't found a last right
                last_left = n
                n = n.next_node
            else:
                last_right.next_node = n.next_node
                last_left.next_node = n
                n.next_node = first_right
                last_left = n
                n = last_right.next_node
        else:
            # n belongs in rt half
            if first_right == None:
                first_right = n
            last_right = n
            n = n.next_node
                

new_linked = LinkedList()
node1 = Node(2)
node2 = Node(8)
node3 = Node(5)
node4 = Node(3)
node5 = Node(10)
node6 = Node(4)

new_linked.insert(node1)
new_linked.insert(node2)
new_linked.insert(node3)
new_linked.insert(node4)
new_linked.insert(node5)
new_linked.insert(node6)
    
print(new_linked)
partition(new_linked, node3)
print(new_linked)