#! /usr/bin/env python

import pytest
from ThreeStack import ThreeStack

@pytest.fixture
def new_stack():
    return ThreeStack

@pytest.fixture
def setup_stack():
    my_stack = ThreeStack()

    my_stack.push(2,1)
    my_stack.push(8,1)
    my_stack.push(9,1)
    my_stack.push(2,1)
    my_stack.push(4,1)
    my_stack.push(5,1)
    my_stack.push(1,1)

    my_stack.push(22,2)
    my_stack.push(24,2)
    my_stack.push(25,2)
    my_stack.push(21,2)

    return my_stack


def test_top1(setup_stack):
    assert setup_stack.top1 == 7

def test_get_spot(setup_stack):
    assert ThreeStack.get_spot(setup_stack, 2) == 11

def test_peek(setup_stack):
    assert setup_stack.peek(1) == 1

def test_pop(setup_stack):
    assert setup_stack.pop(1) == 1