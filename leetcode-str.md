# [String](https://leetcode.com/tag/string/)

## [189. Rotate Array](https://leetcode.com/problems/rotate-array/)
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
## [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]
```

## [165. Compare Version Numbers](https://leetcode.com/problems/compare-version-numbers/)
> 0.1 < 1.1 < 1.2 < 13.37
```python
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        lv1 = version1.split(".")
        lv2 = version2.split(".")
        i = 0
        if len(lv1) > len(lv2):
            lv2 += ['0' for _ in range(len(lv1) - len(lv2))]
        if len(lv1) < len(lv2):
            lv1 += ['0' for _ in range(len(lv2) - len(lv1))]
        while i < min(len(lv1), len(lv2)):
            if int(lv1[i]) < int(lv2[i]):
                return -1
            if int(lv1[i]) > int(lv2[i]):
                return 1
            else:
                i += 1
        return 0
```

## [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
>"()" and "()[]{}" are all valid but "(]" and "([)]" are not.

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

## [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

>"A man, a plan, a canal: Panama" is a palindrome.

```python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0 
        j = len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -=1
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True
```

## [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

>Given a string, find the length of the longest substring without repeating characters.

>Given "abcabcbb", the answer is "abc", which the length is 3.

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        up = 0
        down = 0
        index = {}
        ans = 0

        for down in range(len(s)):
            if s[down] in index:
                up = max(up, index[s[down]])

            ans = max(ans, down - up + 1)
            index[s[down]] = down + 1

        return ans
```

## [344.Reverse String](https://leetcode.com/problems/reverse-string/)
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
## [67.Add Binary](https://leetcode.com/problems/add-binary/)
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

## [459.Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/)
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

## [6.ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)

```python
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= s:
            return s

        L = [''] * numRows
        step = 1
        index = 0
        for i in s:
            L[index] += i
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step
        return ''.join(L)
```

## [13.Roman to Integer](https://leetcode.com/problems/roman-to-integer/)
>Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.

```python
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]
```

## [12.Integer to Roman](https://leetcode.com/problems/integer-to-roman/)
>Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.

```python
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ["", "M", "MM", "MMM"];
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
        return M[num / 1000] + C[num % 1000 / 100] + X[num % 100 / 10 ] + I[num % 10]
```
## [273. Integer to English Words](https://leetcode.com/problems/integer-to-english-words/)
>Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
```python
class Solution(object):

    def __init__(self):
        self.lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        self.thousands = ["","Thousand","Million","Billion"]

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        res = ""
        for i in range(len(self.thousands)):
            if num % 1000 != 0:
                res = self.helper(num % 1000) + self.thousands[i] +" "+ res
            num /= 1000
        return res.strip()

    def helper(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return self.lessThan20[num] + " "
        elif num < 100:
            return self.tens[num/10] + " " + self.helper(num%10)
        else:
            return self.lessThan20[num/100] + " Hundred " + self.helper(num%100)
```
## [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
>Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
```python
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generateParenthesisRecu(result, "", n, n)
        return result

    def generateParenthesisRecu(self, result, current, left, right):
        if left == 0 and right == 0:
            result.append(current)
        if left > 0:
            self.generateParenthesisRecu(result, current + "(", left - 1, right)
        if left < right:
            self.generateParenthesisRecu(result, current + ")", left, right - 1)
```


## [38. Count and Say](https://leetcode.com/problems/count-and-say/)
```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(n-1):
            count = 1
            temp = []
            for index in range(0, len(s) - 1):
                if s[index] == s[index + 1]:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(s[index])
                    count = 1
            temp.append(str(count))
            temp.append(s[-1])
            s = ''.join(temp)
        return s
```
