#[ Dynamic Programming](https://leetcode.com/tag/dynamic-programming/) 

## [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
>Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [-1 for _ in range(n + 1)]
        return self.climb_Stairs(0, n, memo)
        
    def climb_Stairs(self, i, n, memo):
        if i > n:
            return 0
        elif i == n:
            return 1
        elif memo[i] > 0:
            return memo[i]
        else:
            memo[i] = self.climb_Stairs(i + 1, n, memo) + self.climb_Stairs(i + 2, n, memo);
            return memo[i]

class Solution2(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [-1 for _ in range(n + 1)]
        return self.climb_Stairs(n, memo)
        
    def climb_Stairs(self, n, memo):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        elif memo[n] > 0:
            return memo[n]
        else:
            memo[n] = self.climb_Stairs(n - 1, memo) + self.climb_Stairs(n - 2, memo);
            return memo[n]
```
* [Solution](https://leetcode.com/articles/climbing-stairs/)
