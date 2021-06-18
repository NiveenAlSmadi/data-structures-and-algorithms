from stacks_and_queues import __version__
import stacks_and_queues
from stacks_and_queues.stacks_and_queues import (Node,Stack,Queue)

def test_version():
    assert __version__ == '0.1.0'

# Can successfully push onto a stack
def test_push():
    stack=Stack()
    stack.push(22)
    excepted=stack.top.value
    assert excepted == 22

# Can successfully push multiple values onto a stack
def test_push2():
    stack=Stack()
    stack.push(22)
    stack.push(1)
    excepted=stack.top.value
    assert excepted == 1

# Can successfully pop off the stack
def test_pop():
    stack = Stack()
    stack.push(22)
    stack.push(1)
    actual = stack.pop()
    expected = 1
    assert actual == expected

# Can successfully empty a stack after multiple pops
def test_pop2():
    stack = Stack()
    stack.push(1)
    stack.push(20)
    stack.pop()
    stack.pop()
    actual = stack.top
    expected = None
    assert actual == expected


# Can successfully peek the next item on the stack
def test_peek():
    stack=Stack()
    stack.push(7)
    stack.push(5)
    expected = 5
    actual=stack.peek() 
    assert actual == expected


# Can successfully instantiate an empty stack
def test_init_empty():
   stack=Stack()
   expected=None
   assert expected==stack.top


# Calling pop or peek on empty stack raises exception
def test_raise_stack():
   stack=Stack()
   expected="This is Empty stack"
   assert expected==stack.peek()


# Can successfully enqueue into a queue
def test_enqueue():
    queue =Queue()
    queue.enqueue(1)
    actual = queue.front.value
    expected = 1
    assert expected == actual

# Can successfully enqueue multiple values into a queue
def test_enqueue2():
    queue =Queue()
    queue.enqueue('niveen')
    queue.enqueue('nivee')
    actual = queue.front.next.value
    expected = 'nivee'
    assert expected == actual

# Can successfully dequeue out of a queue the expected value
def test_dequeue():
    queue =Queue()
    queue.enqueue(3)
    queue.enqueue(100)
    queue.dequeue()
    actual = queue.front.value
    expected = 100
    assert expected == actual


# Can successfully peek into a queue, seeing the expected value
def test_peek_dedueue():
    queue=Queue()
    queue.enqueue(51)
    queue.enqueue(11)
    expected =51
    actual=queue.peek() 
    assert actual == expected



# Can successfully empty a queue after multiple dequeues
def test_empty_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(20)
    queue.dequeue()
    queue.dequeue()
    actual =  queue.front
    expected = None
    assert actual == expected

    

# Can successfully instantiate an empty queue
def test_init_empty_queue():
  queue=Queue()
  expected=None
  assert expected==queue.front



# Calling dequeue or peek on empty queue raises exception
def test_raise_queue():
   queue= Queue()
   expected="This is Empty queue"
   assert expected==queue.peek()
