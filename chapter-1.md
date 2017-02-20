# [CHAPTER 1. ARRAY / STRING](https://leetcode.com/courses/chapters/1)
## [I. Two-pointer technique](https://leetcode.com/articles/two-pointer-technique/)

### [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

>Given input array nums = [1,1,2],

>our function should return length = 2, with the first two elements of nums being 1 and 2

```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i+1
```
### [167. Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
>Input: numbers={2, 7, 11, 15}, target=9

>Output: index1=1, index2=2


```python
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) -1
        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] < target:
                i += 1
            if numbers[i] + numbers[j] > target:
                j -= 1
        return [i+1, j+1]
```

## [II. Hash Table:](https://leetcode.com/articles/hash-table/)
### [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)
>s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

```python
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.constructDic(s) == self.constructDic(t)
        
    def constructDic(self, s):
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        return dic
    
    def isAnagram2(self, s, t):
        return sorted(s) == sorted(t)
```
[solution](https://leetcode.com/articles/valid-anagram/)

### [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

>Given "abcabcbb", the answer is "abc", which the length is 3.

```python

```

## [III. String Manipulation:](https://leetcode.com/articles/string-manipulation/)

###[28. Implement strStr():](https://leetcode.com/problems/implement-strstr/)
>Implement strStr().Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

```python 

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1
```

###[8. String to Integer (atoi):](https://leetcode.com/problems/string-to-integer-atoi/)

```python 
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        temp = str.strip()
        if not temp:
            return 0
        if len(temp) == 1 and not '0' <= temp[0] <= '9':
            return 0
        result = 0
        flag = 1
        i = 0
        if temp[i] == "+":
            i += 1
        elif temp[i] == "-":
            i += 1
            flag = -1
        while  i < len(temp) and '0' <= temp[i] <= '9':
            if result > (INT_MAX - ord(temp[i]) + ord('0')) / 10:
                if flag > 0:
                    return INT_MAX
                else:
                    return INT_MIN
            result = result * 10 + ord(temp[i]) - ord('0')
            i += 1
        return result * flag
```
