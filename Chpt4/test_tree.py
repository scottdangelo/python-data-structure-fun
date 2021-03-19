#! /usr/bin/env python

import pytest
from Tree import Node, Tree, BinaryTree

@pytest.fixture
def new_tree():
    node = Node(1)
    return Tree(node)

@pytest.fixture
def new_binary_tree():
    node = Node(1)
    return BinaryTree(node)

@pytest.fixture
def built_tree():
    node = Node(1)
    ret_tree = Tree(node)
    one_node = Node(1)
    two_node = Node(2)
    ret_tree.insert(one_node)
    ret_tree.insert(two_node)
    return ret_tree

@pytest.fixture
def built_binary_tree():
    node = Node(1)
    ret_tree = BinaryTree(node)
    two_node = Node(2)
    three_node = Node(3)
    ret_tree.insert(ret_tree.root, two_node)
    ret_tree.insert(ret_tree.root, three_node)
    return ret_tree
@pytest.fixture
def build_ten_tree():
    node = Node(7)
    ret_tree = BinaryTree(node)
    one_node = Node(1)
    two_node = Node(2)
    three_node = Node(3)
    four_node = Node(4)
    five_node = Node(5)
    six_node = Node(6)
    seven_node = Node(7)
    eight_node = Node(8)
    nine_node = Node(9)
    ten_node = Node(10)
    ret_tree.insert(ret_tree.root, two_node)
    ret_tree.insert(ret_tree.root, three_node)
    ret_tree.insert(ret_tree.root, nine_node)
    ret_tree.insert(ret_tree.root, six_node)
    ret_tree.insert(ret_tree.root, one_node)
    ret_tree.insert(ret_tree.root, ten_node)
    ret_tree.insert(ret_tree.root, eight_node)
    return ret_tree

def test_in_order_traversal(build_ten_tree):
    build_ten_tree.in_order_traversal(build_ten_tree.root)
def test_get_tree(new_tree):
    assert(new_tree.root.data == 1)

def test_insert1(built_tree):
    assert(built_tree.root.data == 1)

def test_get_binary_tree(new_binary_tree):
    assert(new_binary_tree.root.data == 1)

# def test_in_order_transversal(new_binary_tree):
    # new_binary_tree.in_order_traversal(new_binary_tree.root)
    # assert(1 ==1)
# def test_binary_repr(built_binary_tree):
    # assert(built_binary_tree.__repr__ == "[1, 2, 3]")