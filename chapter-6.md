# [CHAPTER 6. BINARY SEARCH](https://leetcode.com/courses/chapters/7)

## [278. First Bad Version](https://leetcode.com/problems/first-bad-version/)
>Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

```python
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = (right + left) / 2 
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
```
* [Solution](https://leetcode.com/articles/first-bad-version/)


## [374. Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)
>You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0)

```python
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) / 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                right = mid - 1
            elif result == 1:
                left = mid + 1
```
* [Solution](https://leetcode.com/articles/guess-number-higher-or-lower/)


## [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)
>Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
>Here are few examples.
>[1,3,5,6], 5 → 2
>[1,3,5,6], 2 → 1

```python
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return left

```
* Solution


## [34. Search for a Range](https://leetcode.com/problems/search-for-a-range/)
>Given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4].

```python
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.search_left(nums, target), self.search_right(nums, target) - 1] if self.search_left(nums, target) <= self.search_right(nums, target) - 1 else [-1, -1]
    
    def search_left(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) / 2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left
    def search_right(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) / 2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left
```
* Solution


## [367. Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)
>Given a positive integer num, write a function which returns True if num is a perfect square else False.

```python
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 0, (num >> 1) + 1
        while left <= right:
            mid = left + (right - left) / 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            elif mid * mid > num:
                right = mid - 1
        return False
```
* Solution


## []()
>

```python

```
* Solution
