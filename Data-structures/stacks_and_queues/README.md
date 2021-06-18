# Stacks and Queues
A stack is a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous.

Queue is a container of objects (a linear collection) that are inserted and removed according to the first-in first-out (FIFO) principle.

## Challenge
deal with new Data Structures `(stack&queue)` how to make multiple input and remove or peek 

## Approach & Efficiency

## Stacks

* push >>> O(1)
* pop >>> O(1)
* peek >>> O(1)
* is_empty >>> O(1)

## Queues

* enqueue >>> O(1)
* dequeue >>> O(1)
* peek >>> O(1)
* is_empty >>> O(1)


## API
- ` push  `to push onto a stack and  push multiple values onto a stack
- `pop` to pop off the stack or empty a stack after multiple pops
- `peek`  you will view the value of the top Node in the stack. When you attempt to peek an empty stack an exception will be raised.
- `is_empty` returns true when stack is empty otherwise returns false.
______________________________________________________________________________
- `enqueue ` Nodes or items that are added to the queue.
- `dequeue`Nodes or items that are removed from the queue. If called when the queue is empty an exception will be raised.

- `peek `When you peek you will view the value of the front Node in the queue. If called when the queue is empty an exception will be raised.

- `is_empty `returns true when queue is empty otherwise returns false.