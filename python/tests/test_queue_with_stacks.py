import pytest
from queue_with_stacks.queue_with_stacks import PsuedoQueue, Stack, Node, InvalidOperationError

def test_enqueue():
    ps = PsuedoQueue()
    ps.enqueue(5)
    actual = ps.first_stack.top.value
    expected = 5
    assert actual == expected

def test_dequeue():
    ps = PsuedoQueue()
    ps.enqueue(20)
    ps.enqueue(15)
    ps.enqueue(10)
    ps.enqueue(5)
    actual = ps.dequeue()
    expected = 20
    assert actual == expected

def test_peek():
    pass