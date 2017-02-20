# [CHAPTER 2. LINKED LIST](https://leetcode.com/courses/chapters/3)
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

class Solution2(object):
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



# [Linked List](https://leetcode.com/tag/linked-list/)
## [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        a = headA
        b = headB
        while a != b:
            a = a.next if a != None else headB
            b = b.next if b != None else headA
        return a

```
* [Solution](https://leetcode.com/articles/intersection-two-linked-lists/#approach-1-brute-force-time-limit-exceeded)


## [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
> Given linked list: 1->2->3->4->5, and n = 2.  After removing the second node from the end, the linked list becomes 1->2->3->5.

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        fast, slow = dummy, dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
```
* [Solution](https://leetcode.com/articles/remove-nth-node-end-list/)


## [83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)
>Given 1->1->2->3->3, return 1->2->3.

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur and cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
```
* [Solution](https://leetcode.com/articles/remove-duplicates-sorted-list/)

## [203. Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)
>Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6   Return: 1 --> 2 --> 3 --> 4 --> 5

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
```
* Solution

## [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)
>Given a singly linked list, determine if it is a palindrome.

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        stack = []
        while fast and fast.next:
            fast = fast.next.next
            stack.append(slow.val)
            slow = slow.next
        if fast != None:
            slow = slow.next 
        
        while slow:
            if stack.pop() != slow.val:
                return False
            slow = slow.next
        return True
```
* Solution


## [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
>Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = [0]
        while l1 or l2:
            if l1 == None:
                l1 = ListNode(0)
            if l2 == None:
                l2 = ListNode(0)
            tmp = l1.val + l2.val 
            result.append(0)
            if tmp + result[-2] > 9:
                result[-2] = tmp - 10 + result[-2]
                result[-1] = 1
            else:
                result[-2] = tmp + result[-2] 
            l2 = l2.next
            l1 = l1.next
            
        if result[-1] == 0:
            result = result[ : -1]
        return result
            
```


## [61. Rotate List](https://leetcode.com/problems/rotate-list/)
>Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None or k == 0:
            return head
        fast = head 
        count = 1
        while fast.next:
            count += 1
            fast = fast.next
        fast.next = head
            
        slow, fast = fast, head
        for _ in range(count - k % count):
            slow = slow.next
            fast = fast.next
        slow.next = None
        
        return fast  
```
* [Solution]()



## [82. Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)
>Given 1->2->3->3->4->4->5, return 1->2->5.

```python
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        left, right = dummy, head
        while right:
            if right.next and right.next.val == right.val:
                val = right.val
                while right and right.val == val:
                    right = right.next
                left.next = right
            else:
                left, right = left.next, right.next
        return dummy.next
        
```
* [Solution]()




## []()
>

```python

```
* [Solution]()



## []()
>

```python

```
* [Solution]()




## []()
>

```python

```
* [Solution]()




## []()
>

```python

```
* [Solution]()



## []()
>

```python

```
* [Solution]()


## []()
>

```python

```
* [Solution]()


## []()
>

```python

```
* [Solution]()


## []()
>

```python

```
* [Solution]()



## []()
>

```python

```
* [Solution]()



## []()
>

```python

```
* [Solution]()
