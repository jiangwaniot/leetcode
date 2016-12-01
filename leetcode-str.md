# String
## [Reverse String](https://leetcode.com/problems/reverse-string/)
>Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
```python
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str

        :rtype: str
        """
        return s[::-1]
```
## [Add Binary](https://leetcode.com/problems/add-binary/)
>Given two binary strings, return their sum (also a binary string).

Example: Given
a = "11"
b = "1",
Return "100".

```python
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        indexa = len(a) -1
        indexb = len(b) -1
        carry = 0
        sum = ''
        while indexa >=0 or indexb >=0:
            x = int(a[indexa]) if indexa >=0 else 0
            y = int(b[indexb]) if indexb >=0 else 0
            if (x + y + carry) % 2 == 0:
                sum = '0' + sum
            else:
                sum = '1' +sum
            carry = (x +y + carry) / 2
            indexa, indexb = indexa -1, indexb -1
        if carry == 1:
            sum = '1' + sum
        return sum
```

## [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/)
>Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example: 

Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)


```python
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        indexa = len(a) -1
        indexb = len(b) -1
        carry = 0
        sum = ''
        while indexa >=0 or indexb >=0:
            x = int(a[indexa]) if indexa >=0 else 0
            y = int(b[indexb]) if indexb >=0 else 0
            if (x + y + carry) % 2 == 0:
                sum = '0' + sum
            else:
                sum = '1' +sum
            carry = (x +y + carry) / 2
            indexa, indexb = indexa -1, indexb -1
        if carry == 1:
            sum = '1' + sum
        return sum
```


