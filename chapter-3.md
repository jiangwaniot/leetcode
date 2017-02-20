# [chapter 3](https://leetcode.com/courses/chapters/4)
## [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
>

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#BFS
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        depth = 0
        stk = [root]
        while stk:
            depth += 1
            tmp = []
            for i in stk:
                if i.left:
                    tmp.append(i.left)
                if i.right:
                    tmp.append(i.right)
            stk = tmp
        return depth

# dfs
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        stack = [(root, 1)]
        result = 1
        while stack:
            node, depth = stack.pop()
            result = max(depth, result)
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
        return result
        
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```
* Solution




## [100. Same Tree](https://leetcode.com/problems/same-tree/)
>Given two binary trees, write a function to check if they are equal or not.

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

#bfs
    def isSameTree2(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        queue = [(p, q)]
        while queue:
            node1, node2 = queue.pop(0)
            if node1 == None and node2 == None:
                continue
            elif node1 == None or node2 == None:
                return False
            else:
                if node1.val != node2.val:
                    return False
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))
        return True 

#dfs
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if node1 == None and node2 == None:
                continue
            elif node1 == None or node2 == None:
                return False
            else:
                if node1.val != node2.val:
                    return False
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))
        return True
```
* Solution


## [112. Path Sum](https://leetcode.com/problems/path-sum/)
>Given the below binary tree and sum = 22,
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

```python
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        stack = [(root, root.val)]
        while stack:
            node, val = stack.pop()
            if node.left == None and node.right == None:
                if val == sum:
                    return True
            if node.right:
                stack.append((node.right, val + node.right.val))
            if node.left:
                stack.append((node.left, val + node.left.val))
        return False
```
* Solution


## [257. Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/?tab=Description)
>Given a binary tree, return all root-to-leaf paths.

```python
# dfs + stack
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        stack = [(root, str(root.val))]
        result = []
        while stack:
            node, path = stack.pop()
            if node.left == None and node.right == None:
                result.append(path)
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))
        return result 

# dfs recursively
    def binaryTreePaths(self, root):
        if not root:
            return []
        result = []
        self.dfs(root, str(root.val), result)
        return result
        
    def dfs(self, node, path, res):
        if node.left == None and node.right == None:
            res.append(path)
        if node.right:
            self.dfs(node.right, path + "->" + str(node.right.val), res)
        if node.left:
            self.dfs(node.left, path + "->" + str(node.left.val), res)
```
* Solution

## [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
>Given a binary tree, determine if it is a valid binary search tree (BST).

```python
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = [(float('-inf'), root, float('inf'))]
        while stack:
            node_min, node, node_max = stack.pop()
            if node.left == None and node.right == None:
                pass
            
            if node.right:
                min = node.val
                if node_max > node.right.val > node.val:
                    stack.append((min, node.right, node_max))
                else:
                    return False
            if node.left:
                max = node.val
                if node_min < node.left.val < node.val:
                    stack.append((node_min, node.left, max))
                else:
                    return False
        return True
```
* Solution

<br>
<br>
<br>
***
#[Tree](https://leetcode.com/tag/tree/)
<br>
<br>
<br>

##easy

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

## [107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)
>

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
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
        return [result[level] for level in sorted(result.keys(), reverse = True)]
```
* Solution



## [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
>

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [(0, root)]
        while queue:
            level, node = queue.pop(0)
            if node:
                if node.left:
                    queue.append((level + 1, node.left))
                if node.right:
                    queue.append((level + 1, node.right))
                if node.left == None and node.right == None:
                    return level + 1
            else:
                return level

```
* Solution



## [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
>Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

```python

class Solution(object):
    def lowestCommonAncestor(self, root, node1, node2,):
        if node1 is None or node2 is None or root is None:
            return None
        while root != None:
            if node1.val <= root.val <= node2.val or node2.val <= root.val <= node1.val:
                return root.val
            elif node1.val > root.val and node2.val > root.val:
                root = root.right
            else:
                root = root.left
        return False
```
* Solution

## [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
>Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
```python
class Solution(object):
    def lowestCommonAncestor(self, root, node1, node2):
        def find_path(root, target):
            stack = [(root, [root])]
            while stack:
                node, path = stack.pop()
                
                if node == target:
                    return path
                if node.right:
                    stack.append((node.right, path + [node.right]))
                if node.left:
                    stack.append((node.left, path + [node.left]))
            return None
        path1 = find_path(root, node1)

        path2 = find_path(root, node2)

        i = 0
        while path1[i] is path2[i]:
            if i == min(len(path1), len(path2)) - 1:
                return path1[i]
            i += 1
        return path1[i - 1]
```
* Solution

## [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)
>Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
```python
class Solution(object):
    def isSymmetric(self, root):
        def isSymmetrical(root1, root2):
            if root1 is None and root2 is None:
                return True
            elif root1 is None or root2 is None:
                return False
            elif root1.val != root2.val:
                return False
            return isSymmetrical(root1.left, root2.right) and isSymmetrical(root1.right, root2.left)
        if root is None:
            return True
        else:
            return isSymmetrical(root.left, root.right)

    def isSymmetric2(self, root):
        if root is None:
            return True
        queue = [(root.left, root.right)]
        while queue:
            left, right = queue.pop(0)
            if left is None and right is None:
                continue
            elif left is None or right is None:
                return False
            elif left.val != right.val:
                return False
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        return True

```
* [Solution](https://leetcode.com/articles/symmetric-tree/)

## [103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)
>Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

```python
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        flag = 1 
        queue = [root]
        result = []
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(tmp[::flag])
            flag *= -1
        return result
```
* Solution

## [297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
#### hard
>

```python
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def do(node):
            if node:
                tmp.append(str(node.val))
                do(node.left)
                do(node.right)
            else:
                tmp.append('null')
        tmp = []
        do(root)
        return ','.join(tmp)
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def do():
            val = next(vals)
            if val == 'null':
                return None
            node = TreeNode(val)
            node.left = do()
            node.right = do()
            return node
        vals = iter(data.split(','))
        return do()
```
* Solution

## [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)
#### hard
>

```python
from heapq import *
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heaps = [], []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))
        

    def findMedian(self):
        """
        :rtype: float
        """
        small, large = self.heaps
        if len(large) > len(small):
            return large[0]
        else:
            return (large[0] - small[0]) / 2.0
```
* [Solution](https://leetcode.com/articles/find-median-from-data-stream/)


## [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
#### hard
>Given nums = [1,3,-1,-3,5,3,6,7], and k = 3. Therefore, return the max sliding window as [3,3,5,5,6,7].

```python
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = deque()
        result = []
        for i in range(len(nums)):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if i >= k and dq and dq[0] <= i - k:
                dq.popleft()
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result 
```
* Solution


## []()
>

```python

```
* Solution
