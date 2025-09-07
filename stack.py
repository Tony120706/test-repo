"""CSC148 Lab 4: Abstract Data Types

=== CSC148 Winter 2025 ===
Department of Mathematical and Computational Sciences,
University of Toronto Mississauga

=== Module Description ===
In this module, you will write two different functions that operate on a Stack.
Pay attention to whether or not the stack should be modified.
"""
from typing import Any


###############################################################################
# Task 1: Practice with stacks
###############################################################################
class Stack:
    """A last-in-first-out (LIFO) stack of items.

    Stores data in a last-in, first-out order. When removing an item from the
    stack, the most recently-added item is the one that is removed.
    """
    # === Private Attributes ===
    # _items:
    #     The items stored in this stack. The end of the list represents
    #     the top of the stack.
    _items: list

    def __init__(self) -> None:
        """Initialize a new empty stack."""
        self._items = []

    def is_empty(self) -> bool:
        """Return whether this stack contains no items.

        >>> s = Stack()
        >>> s.is_empty()
        True
        >>> s.push('hello')
        >>> s.is_empty()
        False
        """
        return self._items == []

    def push(self, item: Any) -> None:
        """Add a new element to the top of this stack."""
        self._items.append(item)

    def pop(self) -> Any:
        """Remove and return the element at the top of this stack.

        Raise an EmptyStackError if this stack is empty.

        >>> s = Stack()
        >>> s.push('hello')
        >>> s.push('goodbye')
        >>> s.pop()
        'goodbye'
        """
        if self.is_empty():
            raise EmptyStackError
        else:
            return self._items.pop()


class EmptyStackError(Exception):
    """Exception raised when an error occurs."""
    pass


def size(s: Stack) -> int:
    """Return the number of items in s.

    >>> s = Stack()
    >>> size(s)
    0
    >>> s.push('hi')
    >>> s.push('more')
    >>> s.push('stuff')
    >>> size(s)
    3
    """
    side_stack = Stack()
    count = 0
    # Pop everything off <s> and onto <side_stack>, counting as we go.
    while not s.is_empty():
        side_stack.push(s.pop())
        count += 1
    # Now pop everything off <side_stack> and back onto <s>.
    while not side_stack.is_empty():
        s.push(side_stack.pop())
    # <s> is restored to its state at the start of the function call.
    # We consider that it was not mutated.
    return count


# TODO: implement this function!
def remove_big(s: Stack) -> None:
    """Remove the items in <stack> that are greater than 5.

    Do not change the relative order of the other items.

    >>> s = Stack()
    >>> s.push(1)
    >>> s.push(29)
    >>> s.push(8)
    >>> s.push(4)
    >>> remove_big(s)
    >>> s.pop()
    4
    >>> s.pop()
    1
    >>> s.is_empty()
    True
    """
    s1 = Stack()
    while not s.is_empty():
        item = s.pop()
        if item <= 5:
            s1.push(item)
    while not s1.is_empty():
        s.push(s1.pop())


# TODO: implement this function!
def double_stack(s: Stack) -> Stack:
    """Return a new stack that contains two copies of every item in <stack>.

    We'll leave it up to you to decide what order to put the copies into in
    the new stack.

    >>> s = Stack()
    >>> s.push(1)
    >>> s.push(29)
    >>> new_stack = double_stack(s)
    >>> s.pop()  # s should be unchanged.
    29
    >>> s.pop()
    1
    >>> s.is_empty()
    True
    >>> new_items = []
    >>> new_items.append(new_stack.pop())
    >>> new_items.append(new_stack.pop())
    >>> new_items.append(new_stack.pop())
    >>> new_items.append(new_stack.pop())
    >>> sorted(new_items)
    [1, 1, 29, 29]
    """
    s1 = Stack()
    result = Stack()
    while not s.is_empty():
        item = s.pop()
        result.push(item)
        result.push(item)
        s1.push(item)
    while not s1.is_empty():
        s.push(s1.pop())
    return result

def merge_max(stack1: Stack, stack2: Stack) -> Stack:
    """
    >>> s1 = Stack()
    >>> s2 = Stack()
    >>> s1.push(1)
    >>> s1.push(2)
    >>> s1.push(3)
    >>> s2.push(10)
    >>> s2.push(-5)
    >>> s2.push(7)
    >>> s3 = merge_max(s1, s2)
    >>> s3.pop()
    7
    >>> s3.pop()
    2
    >>> s3.pop()
    10
    >>> s1.pop()
    3
    >>> s2.pop()
    7
    >>> s1 = Stack()
    >>> s2 = Stack()
    >>> s3 = merge_max(s1, s2)
    >>> s3.is_empty()
    True
    >>> s1.is_empty()
    True
    >>> s2.is_empty()
    True
    """
    s3 = Stack()
    hold_s1 = Stack()
    hold_s2 = Stack()
    while not stack1.is_empty() and not stack2.is_empty():
        item1 = stack1.pop()
        item2 = stack2.pop()
        hold_s1.push(item1)
        hold_s2.push(item2)
        if item1 <= item2:
            s3.push(item2)
        else:
            s3.push(item1)
    result = Stack()
    while not s3.is_empty():
        result.push(s3.pop())
    while not hold_s1.is_empty() and not hold_s2.is_empty():
        stack1.push(hold_s1.pop())
        stack2.push(hold_s2.pop())
    return result


class MyQueue:
    """
    Queue implemented by stack
    """
    _items: Stack
    def __init__(self) -> None:
        self._items = Stack()

    def is_empty(self) -> bool:
        """
        Return True if the queue is empty.
        """
        return self._items.is_empty()

    def enqueue(self, items: Any) -> None:
        """
        Enqueue an item into the queue.
        >>> q = MyQueue()
        >>> q.enqueue(3)
        >>> q.enqueue(5)
        >>> q.enqueue(7)
        >>> q.enqueue(3)
        >>> q.enqueue(10)
        >>> q.dequeue()
        3
        >>> q.dequeue()
        5
        >>> q.dequeue()
        7
        >>> q.is_empty()
        False
        """
        met = False
        hold = Stack()
        if self._items.is_empty():
            self._items.push(items)
        else:
            while not self._items.is_empty():
                value = self._items.pop()
                if value == items:
                    met = True
                hold.push(value)
            while not hold.is_empty():
                self._items.push(hold.pop())
            if not met:
                self._items.push(items)

    def dequeue(self) -> Any:
        """
        Dequeue an item from the queue.
        """
        if self._items.is_empty():
            return None
        else:
            hold = Stack()
            while not self._items.is_empty():
                hold.push(self._items.pop())
            item = hold.pop()
            while not hold.is_empty():
                self._items.push(hold.pop())
            return item


if __name__ == '__main__':
    import doctest
    doctest.testmod()
