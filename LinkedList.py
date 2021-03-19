#! /usr/bin/env python

class Node:
    def __init__(self, data ):
        super().__init__()
        self.data = data
        self.next_node = None

    def __repr__(self) -> str:
        return str(self.data)
    def __str__(self) -> str:
        return str(self.data)

class LinkedListIterator:
    '''Iterator class for LinkedList '''
    def __init__(self, linkedList):
        self.linkedList = linkedList
        self.index = 0
        self.currentNode = linkedList.head

    def __next__(self):
        if self.currentNode and self.currentNode.next_node != None:
            ret_node = self.currentNode
            self.currentNode = self.currentNode.next_node
            return ret_node
        elif self.currentNode:
            ret_node = self.currentNode
            self.currentNode = None
            return ret_node
        else:
            raise StopIteration

class LinkedList:

    def __init__(self):
        super().__init__()
        self.head = Node(None)

    def __repr__(self) -> str:
       ret_list = []
       for node in self:
          ret_list.append(node)
       return str(ret_list)
    def __str__(self) -> str:
       ret_list = []
       for node in self:
          ret_list.append(node)
       return str(ret_list)

    def __iter__(self):
        return LinkedListIterator(self)

    def insert(self, in_node):
        nodes = []
        current_node = self.head
        while current_node.next_node:
            nodes.append(current_node)
            current_node = current_node.next_node
        current_node.next_node = in_node
        if in_node in nodes:
            raise Exception("Cannot create a loop with {}".format(in_node))
               
        in_node.next_node = None

    def insert_after(self, in_node, after_node):
        '''Inserts in_node after after_node'''
        
        current_node = self.head
        while current_node.next_node and current_node != after_node:
            current_node = current_node.next_node
        # current_node now points to after node
        in_node.next_node = current_node.next_node
        current_node.next_node = in_node
        return

    def search(self, find_data):
        current = self.head
        while current.next_node and current.next_node.data != find_data:
            current = current.next_node
            
        return current

    def remove(self, node):
        ''' Returns node, if found
            return None if node is head
            returns None if not found '''

        if node == self.head:
            # Cannot remove head node
            return None

        current = self.head
        previous = self.head

        while current.next_node and current.next_node != node:
            previous = current
            current = current.next_node
            
        if current.next_node == node:
            # Node found. Set next and return it
            ret_node = current.next_node
            previous = current
            if ret_node.next_node:
                current.next_node = ret_node.next_node
            else:
                #ret_node is last in list
                current.next_node = None
            return ret_node
        if current.next_node == None:
            # Node Not found.
            return None
