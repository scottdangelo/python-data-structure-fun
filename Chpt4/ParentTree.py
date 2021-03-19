#! /usr/bin/env python

from Tree import Node, BinaryTree

class ParentTree(BinaryTree):
    def __init__(self, node):
        super().__init__(self, node)
        node.parent = None