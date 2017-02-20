# [Array](https://leetcode.com/tag/array/)
## [485. Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/)
>Input: [1,1,0,1,1,1] Output: 3

```python
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, ans = 0, 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                ans = max(count, ans)
                count = 0
        return max(ans, count)
```
* Solution

## [189. Rotate Array](https://leetcode.com/problems/rotate-array/)
>For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

```python
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k:] + nums[:n - k]
```
* [Solution](https://leetcode.com/articles/rotate-array/)

## [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)
>For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

```python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        nums[i:] = [0] * (j - i + 1)
```
* [Solution](https://leetcode.com/articles/move-zeroes/)


## [66. Plus One](https://leetcode.com/problems/plus-one/)
>Given a non-negative number represented as an array of digits, plus one to the number.

```python
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        nums = reduce(lambda x, y: 10 * x + y, digits) + 1
        return [int(i) for i in str(nums)]
```



## [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)
>Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        while j >=0 and i >= 0:
            if nums1[i] >= nums2[j]:
                nums1[i + j + 1] = nums1[i]
                i -= 1
            else:
                nums1[i + j + 1] = nums2[j]
                j -= 1
        if i+1 >= 0:
            nums1[:j + 1] = nums2[:j + 1]
```


## [229. Majority Element II](https://leetcode.com/problems/majority-element-ii/)
>Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        count1, count2, maj1, maj2 = 0, 0, 0, 0
        for i in nums:
            if i == maj1:
                count1 += 1
            elif i == maj2:
                count2 += 1
            elif count1 == 0:
                maj1, count1 = i, 1
            elif count2 ==0:
                maj2, count2 = i, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in set([maj1, maj2]) if \
                nums.count(n) > len(nums)//3]
```


## [169. Majority Element](https://leetcode.com/problems/majority-element/)
>Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times. You may assume that the array is non-empty and the majority element always exist in the array.

```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return nums[int(len(nums)/2)]

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        count = 0
        for i in nums:
            if count == 0:
                res = i
                count = 1
            elif res == i:
                count += 1
            else:
                count -= 1
        return res
```

* Solution

## [27. Remove Element](https://leetcode.com/problems/remove-element/)
>Given input array nums = [3,2,2,3], val = 3
Your function should return length = 2, with the first two elements of nums being 2.

```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        n = len(nums)
        # for i in range(n):
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n
```
* [Solution](https://leetcode.com/articles/remove-element/)

## [448. Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)
>
```python
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(0, len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])
        return [ i + 1 for i in range(len(nums)) if nums[i] > 0]
```
* Solution

## [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
>For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) < 0:
            return max(nums)
        global_max = 0
        local_max = 0
        for i in nums:
            local_max = max(0, local_max + i)
            global_max = max(local_max, global_max)
        return global_max
```
* Solution

## [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profile = 0
        min_prices = float('inf')
        for i in prices:
            if i < min_prices:
                min_prices = i
            elif i - min_prices > max_profile:
                max_profile = i - min_prices
        return max_profile
```
* [Solution](https://leetcode.com/articles/best-time-buy-and-sell-stock/#approach-1-brute-force-time-limit-exceeded)

## [219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)

```python
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        lookup = {}
        for i, num in enumerate(nums):
            if num not in lookup:
                lookup[num] = i
            elif i - lookup[num] <= k:
                return True
            else:
                lookup[num] = i
        return False
```

## [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
>Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

```python
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sn = sorted(nums)
        for i in range(len(sn) -1):
            if sn[i] == sn[i + 1]:
                return True
        return False
```
## [119. Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/)
>For example, given k = 3,  Return [1,3,3,1].

```python
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y : x + y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]
```

## [118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)
>For example, given numRows = 5,
>Return
```
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```

```python
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y : x + y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]
```
##[11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        result = 0
        while i < j:
            result = max(result, (j - i) * min(height[i], height[j]))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return result
```

##[414. Third Maximum Number](414. Third Maximum Number)
```
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.

```

```python
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = set(nums)
        if len(a) < 3:
            return max(a)
        a.remove(max(a))
        a.remove(max(a))
        return max(a)
```


## []()
>

```python
class Solution(object):

#xor
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import operator.xor
        return reduce(operator.xor, range(len(nums) + 1) + nums)

#sum
    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(range(len(nums) + 1)) - sum(nums)

#set
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = set(nums)
        for i in range(len(set_nums) + 1):
            if i not in set_nums:
                return i
```
* Solution



## []()
>

```python

```
* Solution




## []()
>

```python

```
* Solution




## []()
>

```python

```
* Solution

