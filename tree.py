from __future__ import annotations
from typing import Optional, Any

class Tree:
    """
    A plain tree
    """
    _root: Optional[Any]
    _subtrees: Optional[list[Tree]]

    def __init__(self, root: Optional[Any], subtree: Optional[list[Tree]]) -> None:
        if root is None:
            self._root = root
            self._subtrees = None
        else:
            self._root = root
            self._subtrees = subtree

    def is_empty(self) -> bool:
        return self._root is None


class BinarySearchTree:
    """
    A binary search tree
    """
    _root: Optional[Any]
    _left: Optional[BinarySearchTree]
    _right: Optional[BinarySearchTree]

    def __init__(self, root: Optional[Any]) -> None:
        if root is None:
            self._root = root
            self._left = None
            self._right = None
        else:
            self._root = root
            self._left = BinarySearchTree(None)
            self._right = BinarySearchTree(None)


def bfs(t: Tree) -> list[Tree]:
    """
    return a list of nodes in the tree
    using breadth first search
    """
    # Using a queue
    if t.is_empty():
        return []
    else:
        node_list = []
        queue = []
        queue.append(t)  # appending the tree (its root)
        while not queue == []:
            root = queue.pop(0)  # pop the first root
            node_list.append(root._root)
            for subtree in root._subtrees:
                queue.append(subtree)
        return node_list

def dfs(t: Tree) -> list[Tree]:
    """
    return a list of nodes in the tree
    using depth first search
    >>> t = Tree("A", [Tree("B", [Tree("C", [Tree("D", []), Tree("E", [])])]), Tree("F", []), Tree("G", [])])
    >>> dfs(t)
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    """
    # Using a stack
    if t.is_empty():
        return []
    else:
        node_list = []
        stack = []
        stack.append(t)
        while not stack == []:
            root = stack.pop()
            node_list.append(root._root)
            for subtree in reversed(root._subtrees):
                stack.append(subtree)
        return node_lis