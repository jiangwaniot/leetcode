# [CHAPTER 5. BIT MANIPULATION](https://leetcode.com/courses/chapters/6)

## [136. Single Number](https://leetcode.com/problems/single-number/)
>Given an array of integers, every element appears twice except for one. Find that single one.

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in nums:
            result = i ^ result
        return result
```
* Solution


## [190. Reverse Bits](https://leetcode.com/problems/reverse-bits/)
>For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

```python
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(bin(n)[2:].zfill(32)[::-1], 2)
```
* Solution

## [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)
>For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n)[2:].count('1')

# 
    def hammingWeight2(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n = n & (n -1)
            count += 1
        return count
```
* [Solution](https://leetcode.com/articles/number-1-bits/)


## [231. Power of Two](https://leetcode.com/problems/power-of-two/)
>AND of nn and n - 1n−1 flips the least-significant 11-bit in nn to 00

```python
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and  bin(n).count('1') == 1


    def isPowerOfTwo2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and n & (n - 1) == 0

```
* Solution
