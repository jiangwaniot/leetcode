# Array



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
