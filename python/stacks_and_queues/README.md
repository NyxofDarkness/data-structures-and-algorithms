# Stacks and Queues

## Challenge

1. Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
2. Create a Stack class that has a top property. It creates an empty Stack when instantiated.
3. This object should be aware of a default empty value assigned to top when the stack is created.
4. Define a method called push which takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.
5. Define a method called pop that does not take any argument, removes the node from the top of the stack, and returns the node’s value.
6. Should raise exception when called on empty stack
7. Define a method called peek that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.
8. Should raise exception when called on empty stack
9. Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the stack is empty.
10. Create a Queue class that has a front property. It creates an empty Queue when instantiated.
11. This object should be aware of a default empty value assigned to front when the queue is created.
12. Define a method called enqueue which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.
13. Define a method called dequeue that does not take any argument, removes the node from the front of the queue, and returns the node’s value.
14. Should raise exception when called on empty queue
15. Define a method called peek that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.
16. Should raise exception when called on empty queue
17. Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the queue is empty.

## Approach & Efficiency

Write tests to prove the following functionality:

1. Can successfully push onto a stack
2. Can successfully push multiple values onto a stack
3. Can successfully pop off the stack
4. Can successfully empty a stack after multiple pops
5. Can successfully peek the next item on the stack
6. Can successfully instantiate an empty stack
7. Calling pop or peek on empty stack raises exception
8. Can successfully enqueue into a queue
9. Can successfully enqueue multiple values into a queue
10. Can successfully dequeue out of a queue the expected value
11. Can successfully peek into a queue, seeing the expected value
12. Can successfully empty a queue after multiple dequeues
13. Can successfully instantiate an empty queue
14. Calling dequeue or peek on empty queue raises exception

## Solution

![stacks_and_queues White Board](../assets/stacks_and_queues.png)

[PR for stacks_and_queues]()