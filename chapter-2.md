# [chapter 2](https://leetcode.com/courses/chapters/3)
## [237. Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/)
>Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
```

* [Solution](https://leetcode.com/articles/delete-node-linked-list/)

## [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        while head:
            cur = head
            head = head.next
            cur.next = pre
            pre = cur
        return pre

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self._reverse(head)
    def _reverse(self, node, pre = None):
        if node == None:
            return pre
        n = node.next
        node.next = pre
        return self._reverse(n, node)

```
* [Solution](https://leetcode.com/articles/reverse-linked-list/)


## [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
>Given a linked list, determine if it has a cycle in it.

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        slow = head
        fast = head.next
        while slow != None:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```
* [Solution](https://leetcode.com/articles/linked-list-cycle/)

## [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)


```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = cur = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        cur.next = l1 or l2
        return res.next


```
* Solution


## [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)
>Given 1->2->3->4, you should return the list as 2->1->4->3.

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            pre.next, pre.next.next, pre.next.next.next = \
                        pre.next.next, pre.next, pre.next.next.next
            pre = pre.next.next
        return self.next
# tip pre -> a -> b -> b.next to pre -> b -> a -> b.next
```
* Solution
