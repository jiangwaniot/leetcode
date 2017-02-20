# [CHAPTER 4. STACK AND QUEUE](https://leetcode.com/courses/chapters/5)

## [225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)
>

```python
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._queue = collections.deque()
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self._queue.append(x)
        for _ in range(len(self._queue) - 1):
            self._queue.append(self._queue.popleft())
            
            
    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self._queue.popleft()
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self._queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self._queue) == 0
```
* [Solution](https://leetcode.com/articles/implement-stack-using-queues/)


## [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
>The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        lookup = {"(": ")", "{": "}", "[": "]"}
        for i in s:
            if i in lookup:
                stack.append(i)
            elif len(stack) == 0 or lookup[stack.pop()] != i:
                return False
        return len(stack) == 0
```
* Solution

## [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
>

```python
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.A = []
        self.B = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.A.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.move()
        return self.B.pop()
        
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.move()
        return self.B[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.A and not self.B

    def move(self):
        if not self.B:
            while self.A:
                self.B.append(self.A.pop())
```
* [Solution](https://leetcode.com/articles/implement-queue-using-stacks/)


## [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
>

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = {}
        queue = [(0, root)]
        while queue:
            level, node = queue.pop(0)
            if node:
                result[level] = result.get(level, []) + [node.val]
                if node.left:
                    queue.append(((level + 1), node.left))
                if node.right:
                    queue.append(((level + 1), node.right))
        return [result[level] for level in sorted(result.keys())]
```
* Solution
