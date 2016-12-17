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

## [ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)

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

## [Roman to Integer](https://leetcode.com/problems/roman-to-integer/)
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

## [Integer to Roman](https://leetcode.com/problems/integer-to-roman/)
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
